from __future__ import annotations
import copy, hashlib, uuid, zipfile
from pathlib import Path
from collections import Counter
from typed_graph import V, Obj, decode_project, encode_project

MAP_DIR = Path(__file__).resolve().parent
REPO_ROOT = MAP_DIR.parents[2]
TEMPLATE_DIR = REPO_ROOT / 'projects' / 'templates' / 'Map1'
OUTDIR = REPO_ROOT / 'build' / 'colourbridge-fixed-export'
OUTZIP = REPO_ROOT / 'build' / 'colourbridge-fixed-export.zip'
SOURCE_FILES = [
    'DataStorageFile_Server_Slot1.json', 'ProjectData_slot_1.meta',
    'ProjectEditRecord_slot_1.meta', 'ProjectEditRecord_slot_1.meta.json',
    'SceneReview_1.bytes', 'UserLevelData_1.bytes', 'UserLevelData_C_1.bytes',
]
missing = [name for name in ['ProjectData_slot_1.bytes', *SOURCE_FILES] if not (TEMPLATE_DIR / name).is_file()]
if missing:
    raise SystemExit('Template source file(s) missing: ' + ', '.join(missing))
files = {name: (TEMPLATE_DIR / name).read_bytes() for name in SOURCE_FILES}
original = (TEMPLATE_DIR / 'ProjectData_slot_1.bytes').read_bytes()
root, tail, decoded = decode_project(original)

# Deterministic IDs let repeated builds produce the same result from the same template.
_next_id = 0
def uid():
    global _next_id
    _next_id += 1
    return 'FC_' + str(uuid.uuid5(uuid.NAMESPACE_URL, f'FFCRAFT/ColourBridge/fix-v1/{_next_id}'))

# Access helpers for typed AST (Obj fields hold V wrappers; list entries are V wrappers).
def field_obj(o, k):
    v = o.getv(k)
    if not v: raise KeyError(k)
    return v.val

def field_list(o, k):
    v = o.getv(k)
    if not v or v.tag != 8: raise TypeError(f'{k} is not list')
    return v.val

def set_scalar(o, k, value, tag=None):
    old = o.getv(k)
    if tag is None:
        tag = old.tag if old else (2 if isinstance(value, str) else 3 if isinstance(value, bool) else 1)
    o.setv(k, V(tag, value))

def set_slot_value(slot, value, tag=9):
    slot.setv('value', V(tag, value))

def list_values(o, k):
    return [x.val for x in field_list(o, k)]

def func_meta(o):
    return field_obj(field_list(o, 'values')[0].val, 'value')

def regenerate_ids(node):
    if isinstance(node, Obj):
        for k, v in node.fields:
            if k == 'id' and v.tag == 2 and isinstance(v.val, str) and v.val.startswith('FC_'):
                node.setv(k, V(2, uid()))
            else:
                regenerate_ids(v.val)
    elif isinstance(node, V):
        regenerate_ids(node.val)
    elif isinstance(node, list):
        for v in node:
            regenerate_ids(v)

def walk(node):
    if isinstance(node, Obj):
        yield node
        for _, v in node.fields:
            yield from walk(v.val)
    elif isinstance(node, V):
        yield from walk(node.val)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v.val)

def find_node(node, typename, node_id=None):
    for o in walk(node):
        if o.get('typeName') == typename and (node_id is None or o.get('id') == node_id):
            return o
    raise LookupError((typename, node_id))

def get_node_value(node, index):
    return field_list(node, 'values')[index].val

def get_action_list(node):
    bodies = field_list(node, 'bodies')
    return field_list(bodies[0].val, 'actions')

def get_actions(node):
    return [v.val for v in get_action_list(node)]

def disable(node):
    set_scalar(node, 'Enabled', 0, tag=3)

def set_value_in_nested_const(action, slot_index, new_value):
    slot = get_node_value(action, slot_index)
    const = field_obj(slot, 'value')
    vals = field_list(const, 'values')
    vals[0].val.set('value', str(new_value), tag=2)

# Find main graph and exact functions/events.
graphs = [v.val for v in field_list(root, 'graphs')]
graph = next(g for g in graphs if g.get('id') == 'GR_617ac097-7cff-44c2-894e-51668b4233d9')
contents = list_values(graph, 'contents')
gameloop = next(n for n in contents if n.get('typeName') == 'DefFuncWithoutReturn' and func_meta(n).get('funcName') == 'GameLoop')
loser = next(n for n in contents if n.get('typeName') == 'DefFuncWithoutReturn' and func_meta(n).get('funcName') == 'Loser')
onmatch = next(n for n in contents if n.get('typeName') == 'OnMatchStart')

# 1) Disable only the redundant temporary tip writer; retain persistent ColorHUD label.
notify = find_node(gameloop, 'NotifyShowTips', 'FC_eceaa884-6d9c-4126-8635-c8102e65b6f1')
disable(notify)

# 2) Disable the one-shot timer that expires at the end of the 15-second startup wait.
old_create = find_node(onmatch, 'CreateInternalHud', 'FC_0c3bc209-a7e5-4031-b95e-06a05be27804')
old_set = find_node(onmatch, 'SetEntityProperty', 'FC_9fbd7ca8-a382-48b4-98b3-50657c86e8af')
disable(old_create)
disable(old_set)

# 3) Add graph state for the active round-timer HUD entity.
var_def_list = field_list(graph, 'graphVarDefines')
color_var = next(v.val for v in var_def_list if v.val.get('varName') == 'ColorHUD')
round_var = copy.deepcopy(color_var)
round_var.set('index', 5, tag=1)
round_var.set('varName', 'RoundTimerHUD', tag=2)
round_var.set('isVarNameModified', 1, tag=3)
round_var.set('id', uid(), tag=2)
round_var_id = round_var.get('id')
var_def_list.append(V(9, round_var))

# Copy native PhaseCountDownHud nodes so property/component names stay editor-native.
create = copy.deepcopy(old_create)
prop = copy.deepcopy(old_set)
regenerate_ids(create)
regenerate_ids(prop)
set_scalar(create, 'Enabled', 1, tag=3)
set_scalar(prop, 'Enabled', 1, tag=3)

# Name the created local HUD entity.
create_out = field_list(create, 'values')[2].val
create_out_value = field_obj(create_out, 'value')
local_timer_id = create_out_value.get('id')
create_out_value.set('varName', 'RoundTimer', tag=2)
create_out_value.set('isVarNameModified', 1, tag=3)

# Point SetEntityProperty at the newly-created local HUD, set duration to 11 seconds.
prop_values = field_list(prop, 'values')
prop_getter = field_obj(prop_values[0].val, 'value')
field_list(prop_getter, 'values')[0].val.set('value', local_timer_id, tag=2)
set_value_in_nested_const(prop, 4, 11)

# Store the returned HUD entity in graph-level state for cleanup before the next cycle.
set_round = copy.deepcopy(get_actions(gameloop)[0])
regenerate_ids(set_round)
field_list(set_round, 'values')[0].val.set('value', round_var_id, tag=2)
local_get = copy.deepcopy(prop_getter)
regenerate_ids(local_get)
field_list(local_get, 'values')[0].val.set('value', local_timer_id, tag=2)
set_slot_value(field_list(set_round, 'values')[2].val, local_get, tag=9)

# Insert timer creation, duration assignment and graph-variable storage at GameLoop entry.
loop_action_list = get_action_list(gameloop)
loop_action_list[1:1] = [V(9, create), V(9, prop), V(9, set_round)]

# Create RemoveEntity(GetSelfGraphProperty(RoundTimerHUD)) from native template blocks.
remove = copy.deepcopy(find_node(onmatch, 'RemoveEntity', 'FC_64636de1-69e2-492a-b01e-a2f7e028d6e9'))
regenerate_ids(remove)
remove_slot = field_list(remove, 'values')[0].val
remove_slot.set('valueType', 'any', tag=2)
getter_template = None
for action in get_actions(gameloop):
    for obj in walk(action):
        if obj.get('typeName') == 'GetSelfGraphProperty':
            getter_template = obj
            break
    if getter_template:
        break
if getter_template is None:
    raise RuntimeError('No GetSelfGraphProperty template')
getter = copy.deepcopy(getter_template)
regenerate_ids(getter)
field_list(getter, 'values')[0].val.set('value', round_var_id, tag=2)
set_slot_value(remove_slot, getter, tag=9)

# Remove old timer just before Loser calls the next GameLoop.
loser_actions = get_action_list(loser)
call_idx = next(i for i, action in enumerate(loser_actions) if action.val.get('typeName') == 'CallActionFunc')
loser_actions.insert(call_idx, V(9, remove))

# Encode back into the wrapper, retaining untouched outer protobuf fields.
patched_bytes, patched_raw = encode_project(root, tail)
files['ProjectData_slot_1.bytes'] = patched_bytes

# Parse the result again and validate expected edits and node ID uniqueness.
check, check_tail, check_data = decode_project(patched_bytes)
assert check_data == patched_raw and check_tail == tail
check_graphs = [v.val for v in field_list(check, 'graphs')]
cg = next(g for g in check_graphs if g.get('id') == graph.get('id'))
cc = list_values(cg, 'contents')
cgl = next(n for n in cc if n.get('typeName') == 'DefFuncWithoutReturn' and func_meta(n).get('funcName') == 'GameLoop')
cl = next(n for n in cc if n.get('typeName') == 'DefFuncWithoutReturn' and func_meta(n).get('funcName') == 'Loser')
co = next(n for n in cc if n.get('typeName') == 'OnMatchStart')
assert find_node(cgl, 'NotifyShowTips', 'FC_eceaa884-6d9c-4126-8635-c8102e65b6f1').get('Enabled') == 0
assert find_node(co, 'CreateInternalHud', 'FC_0c3bc209-a7e5-4031-b95e-06a05be27804').get('Enabled') == 0
assert find_node(co, 'SetEntityProperty', 'FC_9fbd7ca8-a382-48b4-98b3-50657c86e8af').get('Enabled') == 0
assert sum(1 for action in get_actions(cgl) if action.get('typeName') == 'CreateInternalHud') == 2
assert any(action.get('typeName') == 'RemoveEntity' for action in get_actions(cl))
ids = []
for g in check_graphs:
    for obj in walk(g):
        if obj.get('typeName') and isinstance(obj.get('id'), str):
            ids.append(obj.get('id'))
duplicates = {key: count for key, count in Counter(ids).items() if count > 1}
assert not duplicates, f'duplicate typeName node ids: {duplicates}'

OUTDIR.mkdir(parents=True, exist_ok=True)
for name, data in files.items():
    (OUTDIR / name).write_bytes(data)
(OUTDIR / 'ProjectData_slot_1.bytes').write_bytes(patched_bytes)
readme_path = MAP_DIR / 'README.md'
if readme_path.is_file():
    (OUTDIR / 'FIX-NOTES.md').write_text(readme_path.read_text(encoding='utf-8'), encoding='utf-8')
with zipfile.ZipFile(OUTZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
    for path in sorted(OUTDIR.iterdir()):
        if path.is_file():
            archive.write(path, path.name)

print('PATCH_OK')
print('source_file_bytes', len(original), 'patched_bytes', len(patched_bytes), 'decoded_graph_bytes', len(decoded), 'reencoded_graph_bytes', len(patched_raw))
print('files', [(name, len(data), hashlib.sha256(data).hexdigest()) for name, data in files.items()])
print('RoundTimerHUD', round_var_id, 'local output', local_timer_id)
print('output_dir', OUTDIR)
print('zip', OUTZIP, OUTZIP.stat().st_size)
