from __future__ import annotations
import gzip
import struct
import zlib
from dataclasses import dataclass
from typing import Any

@dataclass
class V:
    tag: int
    val: Any = None
    raw: bytes = b""

class Obj:
    def __init__(self, fields=None):
        self.fields = fields or []
    def get(self, key, default=None):
        v = self.getv(key)
        return v.val if v is not None else default
    def getv(self, key):
        for name, value in self.fields:
            if name == key:
                return value
        return None
    def setv(self, key, value):
        for i, (name, old) in enumerate(self.fields):
            if name == key:
                self.fields[i] = (name, value)
                return
        self.fields.append((key, value))
    def set(self, key, value, tag=None):
        old = self.getv(key)
        if tag is None:
            tag = old.tag if old else (2 if isinstance(value, str) else 3 if isinstance(value, bool) else 1)
        self.setv(key, V(tag, value))

class Parser:
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0
    def take(self, n: int) -> bytes:
        if n < 0 or self.pos + n > len(self.data):
            raise ValueError(f"read {n} bytes at {self.pos} of {len(self.data)}")
        out = self.data[self.pos:self.pos+n]
        self.pos += n
        return out
    def u8(self) -> int:
        return self.take(1)[0]
    def u32(self) -> int:
        return struct.unpack("<I", self.take(4))[0]
    def string(self) -> str:
        return self.take(self.u8()).decode("utf-8", "replace")
    def fields(self, count: int, depth: int = 0) -> Obj:
        if depth > 100:
            raise ValueError("serialized object nesting limit exceeded")
        fields = []
        for _ in range(count):
            key = self.string()
            tag = self.u8()
            fields.append((key, V(tag, self.value(tag, depth + 1))))
        return Obj(fields)
    def value(self, tag: int, depth: int):
        if tag == 1: return {"__raw__": self.take(4)}
        if tag == 2: return self.string()
        if tag == 3: return self.u8()
        if tag == 4: return {"__raw__": self.take(4)}
        if tag == 5: return {"__raw__": self.take(8)}
        if tag == 6: return None
        if tag == 7: return {"__raw__": self.take(12)}
        if tag == 8:
            count = self.u32()
            if count > 200000: raise ValueError(f"unexpected list size: {count}")
            items = []
            for _ in range(count):
                item_tag = self.u8()
                items.append(V(item_tag, self.value(item_tag, depth + 1)))
            return items
        if tag == 9: return self.fields(self.u32(), depth + 1)
        raise ValueError(f"unknown serialized value tag {tag} at {self.pos - 1}")

def encode_string(value: str) -> bytes:
    b = value.encode("utf-8")
    if len(b) > 255: raise ValueError(f"string too long for compact format: {len(b)} bytes")
    return bytes([len(b)]) + b

def encode_value(value: V) -> bytes:
    tag, x = value.tag, value.val
    if tag == 1:
        return x["__raw__"] if isinstance(x, dict) and "__raw__" in x else struct.pack("<i", int(x))
    if tag == 2: return encode_string(x)
    if tag == 3: return bytes([int(x)])
    if tag in (4, 5):
        return x["__raw__"] if isinstance(x, dict) and "__raw__" in x else struct.pack("<f" if tag == 4 else "<d", float(x))
    if tag == 6: return b""
    if tag == 7: return x["__raw__"] if isinstance(x, dict) and "__raw__" in x else bytes(x)
    if tag == 8: return struct.pack("<I", len(x)) + b"".join(bytes([item.tag]) + encode_value(item) for item in x)
    if tag == 9: return encode_object(x)
    raise ValueError(f"unsupported serialized value tag {tag}")

def encode_object(obj: Obj) -> bytes:
    return struct.pack("<I", len(obj.fields)) + b"".join(encode_string(k) + bytes([v.tag]) + encode_value(v) for k, v in obj.fields)

def decode_project(blob: bytes):
    # Observed container: two nested protobuf length-delimited messages, with a gzip stream
    # beginning at byte offset 8 and additional untouched outer fields after the gzip stream.
    inflater = zlib.decompressobj(31)
    decoded = inflater.decompress(blob[8:])
    trailing_outer_fields = inflater.unused_data
    parser = Parser(decoded)
    root = parser.fields(parser.u32())
    if parser.pos != len(decoded):
        raise ValueError(f"unparsed inner bytes: {len(decoded) - parser.pos}")
    return root, trailing_outer_fields, decoded

def encode_varint(n: int) -> bytes:
    out = bytearray()
    while n > 127:
        out.append((n & 127) | 128)
        n >>= 7
    out.append(n)
    return bytes(out)

def encode_project(root: Obj, trailing_outer_fields: bytes) -> tuple[bytes, bytes]:
    inner = encode_object(root)
    compressed = gzip.compress(inner, compresslevel=9, mtime=0)
    nested_message = b"\x0a" + encode_varint(len(compressed)) + compressed
    wrapped = b"\x0a" + encode_varint(len(nested_message)) + nested_message + trailing_outer_fields
    return wrapped, inner
