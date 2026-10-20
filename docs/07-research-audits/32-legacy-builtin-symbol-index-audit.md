# Legacy BuiltinSymbol index audit

**Checked:** 21 October 2026  
**Source snapshot:** [Divyam999hp/craftlandstudio.ffugclanguage-1.5.0](https://github.com/Divyam999hp/craftlandstudio.ffugclanguage-1.5.0), file `library/release/BuiltinSymbol.json`  
**Source file blob SHA:** `977fe8d88bd83dd47061e5e4ac5349dbd16b87b1`  
**Evidence class:** `community-snapshot` — legacy extension data, not current official-editor evidence.

## Finding

The public 1.5.0 language-extension mirror contains a 681,139-byte `BuiltinSymbol.json` symbol index. Unlike a simple name/signature list, it records symbol IDs within each library file and component property IDs. It covers 42 library file spaces.

A direct read of the JSON yielded the following **raw per-library record counts**:

| Symbol family | Records | Distinct names in the combined file-space scan |
|---|---:|---:|
| Components | 590 | 555 |
| Component properties | 3,315 | Not summed as a global unique namespace |
| Enums | 150 | 150 |
| APIs | 739 | 729 |
| Events | 259 | 259 |

The component count includes repeated names in multiple libraries: `Player` occurs in 12 file spaces and `Global` in 9. Several API names also occur in more than one file space; for example, `Length` occurs three times, while `Clone`, `Sub`, `Max`, `Min`, `Clear`, `New`, `Create`, and `Remove` each occur in two records. These are not safe to merge by name alone.

## Why it matters to FFCRAFT

1. **Component/property ID leads.** The symbol index gives numeric IDs for some component/property pairs. For example, it lists `Entity` with ID `10`, and properties including `ActiveSelf` (`-10002`), `Enable` (`-10005`) and `Name` (`-10006`). It lists `Transform` with ID `97` and properties including `Position` (`-97000`) and `Rotation` (`-97001`). These demonstrate the index's shape; they are **legacy values**, not a claim that these IDs are current in Studio 1.19.x.
2. **Additional enum/type names.** This raw index contains 150 enum records, compared with 144 enum declarations in FFCRAFT's parsed symbol catalog. The difference signals a parser/schema reconciliation task, not six automatically verified new current enums.
3. **A cross-check for old API extraction.** The index records 739 API symbol entries (729 names), while the current parsed FFCRAFT mirror catalog records 681 function candidates. The categories and extraction rules may differ, so this must be reconciled by library and signature instead of subtracting totals or silently merging lists.
4. **A better audit trail.** IDs, symbol names and the originating `.fcc` library offer additional clues when reviewing approximate matches in [the 443-line Rough crosswalk](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/02-mobile-and-blocks/24-block-symbol-crosswalk.md), especially property-related labels. This is useful for search prioritization, not proof of Mobile visual-block structure.

## Cross-check against the unresolved Rough.txt queue

A direct, case-insensitive alphanumeric-normalized label comparison found **47 of 111 queued lines** with exact-name hits in this index, spanning 48 symbol records (including one name recorded with spelling/case variants). Example records include:

| Rough.txt label | Legacy library | Symbol name | ID |
|---|---|---|---:|
| Vector2 | `StdLibrary.fcc` | `Vector2` component/type symbol | 159 |
| Vector2 Sub | `Math.fcc` | `Vector2Sub` | 3245 |
| New Vector2 | `Math.fcc` | `NewVector2` | 3256 |
| Vector2 Get X | `Math.fcc` | `Vector2GetX` | 3240 |
| Vector2 Set Y | `Math.fcc` | `Vector2SetY` | 3243 |
| Damage Type | `Combat.fcc` | `DamageType` enum | 24 |
| Weapon Skin Type | `LevelObject.fcc` | `WeaponSkinType` enum | 419 |
| Vehicle Skin Type | `LevelObject.fcc` | `VehicleSkinType` enum | 420 |

The complete per-row matches are embedded in `research/rough-block-review-queue.json`. These additions give review work an indexed starting point; **none of the 111 queue rows has been marked resolved from this comparison alone**. A label-to-name match cannot prove current editor behavior, socket types, option lists or cross-platform parity.

## Count and compatibility rules

- These are records counted from the legacy JSON snapshot, not a list of distinct, currently supported game features.
- File/library context is part of a symbol's identity. Preserve the library path and original spelling/case; do not globally deduplicate names or ID values.
- `BuiltinSymbol.json` does not replace full declarations: parameter signatures, descriptions, runtime constraints, deprecations and editor sockets must be cross-checked against the corresponding `.fcc` text, current official documentation or current installed metadata.
- A PC language-extension symbol index cannot establish Craftland Mobile block parity or enumerate Mobile dropdown contents.
- FFCRAFT must not label these values `official-current-installed-library`, `official-current-editor-mcp` or `runtime-tested`. Use `community-snapshot` until corroborated by a version-matched current source.

## Provenance and reuse warning

The inspected mirror is for extension version **1.5.0**, substantially older than the Craftland Studio 1.19.0 release noted in FFCRAFT's October 2026 baseline. Its `LICENSE.md` is empty and the GitHub repository metadata does not provide an affirmative license. This audit records independently inspected counts, examples, hashes and the research implications; it does **not** copy the raw JSON, library files or compiler binaries into FFCRAFT. Review the upstream terms before redistributing derived datasets.

Source links:
- [BuiltinSymbol.json in the public 1.5.0 mirror](https://github.com/Divyam999hp/craftlandstudio.ffugclanguage-1.5.0/blob/main/library/release/BuiltinSymbol.json)
- [The mirror's library/release directory](https://github.com/Divyam999hp/craftlandstudio.ffugclanguage-1.5.0/tree/main/library/release)
- [Official PC code-script manual](https://ffcraftland.garena.com/en/tutorial/fe/1-9)
- [Current-editor capture playbook](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/06-troubleshooting/27-current-editor-capture-playbook.md)
- [PC library catalog recovery](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/03-pc-studio/20-pc-library-catalog.md)

## Next actions

1. Use this as a version-labelled comparison source for property/enum/API names referenced by `Rough.txt`.
2. Compare symbols library-by-library against FFCRAFT's existing parsed catalog, preserving original name, source path, ID and any alias/deprecation markings.
3. Confirm promising discrepancies against current Studio-installed `.fcc` data or the current editor MCP export before changing a current-status label.
4. Keep Mobile screenshot/export evidence in a separate crosswalk.
