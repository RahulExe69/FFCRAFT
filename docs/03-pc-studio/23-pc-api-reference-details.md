# Detailed PC API/event/component reference

## What has been extracted

Machine-readable reference: [`research/pc-library-api-reference.json`](https://github.com/RahulExe69/FFCRAFT/blob/main/research/pc-studio/pc-library-api-reference.json).

The parser now covers all **42** `.fcc` libraries available in the public 1.5.0 mirror. Current extraction totals:

- 681 function declarations, including parsed signatures, parameters text, return text, descriptions, documented parameter/return/output metadata where comments were available, attributes and source blob SHAs.
- 259 event declarations, including descriptions, owner-type metadata when documented, attributes and source blob SHAs.
- 470 component declarations, including partial/abstract declarations, with 3,219 candidate property declarations and labels/types/attributes when parseable.
- 232 functions flagged as deprecated by a mirrored annotation/comment or documentation text.
- 376 functions marked server-side and 54 marked client-side in the mirrored declarations.

These are **extraction counts and candidate metadata**, not unique-current API counts. Partial components, duplicate/alias/compatibility functions, deprecated entries and parser edge cases remain. Some source declarations have incomplete comments, and the property extractor is heuristic. Review exact signatures and argument names in the current editor/official docs before using them in code.

## Why this is useful for the original Rough.txt gap

This is much closer to the underlying PC API reference than a tutorial-only search: a lookup can find the likely function/event/component name, input parameter types, output/return shape, docs text, server/client hints, component properties and whether the old source marks an item deprecated. It complements the smaller enum/member catalog rather than replacing it.

- [Symbol/enum-only catalog](https://github.com/RahulExe69/FFCRAFT/blob/main/research/pc-studio/pc-library-symbol-catalog.json)
- [Dropdown crosswalk against your 65 observed labels](https://github.com/RahulExe69/FFCRAFT/blob/main/research/crosswalks/enum-dropdown-crosswalk.json)
- [Current official enum/type supplement](https://github.com/RahulExe69/FFCRAFT/blob/main/research/pc-studio/current-official-enum-supplement.json)

## Critical compatibility warning

The mirror identifies as extension version **1.5.0**, while the official release notes found for this research snapshot show Craftland Studio **1.19.0 (September 2026)**. The official patch notes for Studio 1.17.0 also say TYPE-related APIs were migrated to ID-based APIs, removing the need for additional `as` casting. That makes it especially risky to use old type signatures as current code without checking the current definition.

The official 1.19.0 notes also say the editor's MCP server supports Blocks, Scripts, Scenes, UI, Animation Controllers, and more. If the target editor exposes its MCP server in an environment we can reach, it may be a stronger route to enumerate live blocks and current script/API structures than old public files alone. This repository pass has not connected to a user's local editor MCP server.

## Sources

- [Public mirror, library/release](https://github.com/Divyam999hp/craftlandstudio.ffugclanguage-1.5.0/tree/main/library/release)
- [Official extension listing](https://marketplace.visualstudio.com/items?itemName=craftLandstudio.ffugclanguage)
- [Official code-script guide](https://ffcraftland.garena.com/en/tutorial/fe/1-9)
- [Official patch notes](https://ffcraftland.garena.com/en/patch-notes/)
- [Official API reference](https://ffcraftland.garena.com/en/docs/api)

The mirror's `LICENSE.md` is empty. FFCRAFT stores parsed identifiers and descriptive metadata with provenance hashes; it does not redistribute the raw `.fcc` files or extension binaries. This is a secondary reference and does not prove exact parity with Craftland Mobile visual blocks.
