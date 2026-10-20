# Map1 source inventory

## Scope

This inventory describes the user-provided Craftland Mobile export committed under `projects/templates/Map1/`. It is an inventory, not a claim that the proprietary serialized scripts have been decoded.

## Files

| File | Size (bytes) | Current understanding |
|---|---:|---|
| `ProjectData_slot_1.bytes` | 107,913 | Serialized project data; inner structure not fully decoded. |
| `ProjectData_slot_1.meta` | 38,853 | Readable metadata/string-bearing file; contains project labels and object/block references. |
| `UserLevelData_1.bytes` | 132,083 | Serialized user-level data; includes readable names for variables/systems. |
| `UserLevelData_C_1.bytes` | 74,723 | Separate serialized data group; exact role not yet verified. |
| `SceneReview_1.bytes` | 211,296 | Scene-review data; extracted embedded preview did not reveal useful map detail. |
| `DataStorageFile_Server_Slot1.json` | 135 | Small server data-storage JSON file. |
| `ProjectEditRecord_slot_1.meta` | 12 | Small edit-record metadata file. |
| `ProjectEditRecord_slot_1.meta.json` | 316 | JSON sidecar with obfuscated/opaque keys. |
| `README.md` | 933 | Template README. |

Sizes are the repository tree values at the time this inventory was written. Recheck when the export changes.

## Identifiers observed in serialized content

Names previously extracted from the user-level files include `TilesList`, `ColourList`, `TargetColour`, `PickedColour`, `ColorHUD`, `GameLoop`, `CurrentTile`, `LuckyTile`, `Loser`, `CheckedObject`, `Tile`, `FIND THE COLOUR`, and `Welcome To Colour Bridge`.

These names provide search anchors. They do not independently prove exact event wiring, types, conditions, or control flow.

## Next steps to improve this inventory

1. Compute SHA-256 for each original file from a verified local copy.
2. Identify headers, container framing, compression, serialization/protobuf schemas, or app-specific encoding for each binary.
3. Decode into a read-only intermediate representation before interpreting scripts.
4. Map node/object IDs and references to readable names.
5. Preserve decoding tools, format notes, and sample outputs in a separate tooling/docs folder if created.
6. Compare decoded nodes against official Craftland Mobile block references and validate uncertain behaviours in the editor.

Do not edit the original binaries manually while the format is unknown.
