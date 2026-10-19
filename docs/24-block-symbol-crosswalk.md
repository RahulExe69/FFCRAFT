# Block-symbol crosswalk for Rough.txt

## Purpose

The original `Rough.txt` remains untouched. This crosswalk compares each extracted line in `research/user-observed-block-inventory.json` against both the recovered PC function/event/component/property declarations and targeted current official API/event pages.

Machine-readable result: [`research/block-symbol-crosswalk.json`](../research/block-symbol-crosswalk.json).

## Comparison result

The old-library comparison across 443 extracted lines found:
- **306** exact normalized matches to a mirrored symbol name or API documentation title.
- **113** approximate candidates, retained only as search leads.
- **21** lines with no exact match in the older mirrored libraries.
- **3** entries likely to be explanatory prose or section notes rather than blocks.

These numbers describe the comparison with the **older 1.5.0 mirror**, not the live official docs. They do not tell us the number of current working visual blocks.

## Current official review already filled some gaps

Targeted checks on the current official documentation now confirm useful labels that the old mirror didn't match exactly:

| Rough label | Current official reference | Finding |
|---|---|---|
| `Set Property` | [Set property API](https://ffcraftland.garena.com/en/docs/api-1-871/) and [Mobile block tutorial](https://ffcraftland.garena.com/en/tutorial/cl/3-48/) | Mobile tutorial explicitly demonstrates a visual block. The PC API page labels the API **Only PC**. Keep the Mobile visual block and PC code API as separate records with separate scopes. |
| `Get Property` | [Get property API](https://ffcraftland.garena.com/en/docs/api-1-872/) and [Mobile block tutorial](https://ffcraftland.garena.com/en/tutorial/cl/3-48/) | Mobile tutorial demonstrates a visual property lookup; the PC API page is marked **Only PC**. |
| `Wait for Milliseconds` | [STD Library API index](https://ffcraftland.garena.com/en/docs/api-1-26) | Official label is singular: **Wait for Millisecond**. |
| `This Entity` / `Get Global` | [STD Library API index](https://ffcraftland.garena.com/en/docs/api-1-26) | Both names are present in current PC code-script documentation. |
| `Get Children By Index` | [Get Child By Index](https://ffcraftland.garena.com/en/docs/api-1-540/) | Current label is singular; the page lists Both Server and Client, Both Mobile and PC. |
| `Get Parnt` | [Get Parent](https://ffcraftland.garena.com/en/docs/api-1-542/) | Correct label is Get Parent; current page lists Both Server and Client, Both Mobile and PC. |
| `Get Type Name` | [Get Type Name](https://ffcraftland.garena.com/en/docs/api-1-978/) | Current official API confirms the label and says Both Server/Client, Both Mobile/PC. |
| `Filter Level Object` | [Level Object API](https://ffcraftland.garena.com/en/docs/api-26-124) | Current label is Filter Level Objects. |
| `On Player Quit Midway` | [Event reference](https://ffcraftland.garena.com/en/docs/type-11) | Listed as a current Global entity event. |
| `On User Quit or User Match End` | [Event reference](https://ffcraftland.garena.com/en/docs/type-11) | Listed as a current Global entity event. |
| `On User Portal` | [Level Object module](https://ffcraftland.garena.com/en/docs/module-26) | A related official event is **On Use Portal**; verify the exact visual label on the target editor before treating the wording as identical. |
| `Type As` | [Official patch notes](https://ffcraftland.garena.com/en/patch-notes/) | Studio 1.17.0 notes describe the TYPE-to-ID API migration and say extra `as` casting is no longer required in that context; treat an old casting block as version/context-sensitive. |

The current Mobile tutorial gives an unusually concrete example: On Player Join → Get Property (Player) → Get Property (Rig) → Get Property (Head) → Set Property (Skeleton Scale) with a Vector3 value of (3,3,3). See the [wide screenshot of the connected blocks](https://dl.dir.freefiremobile.com/common/OB46/CSH/OfficialWeb/CLtutorial/009_BlockScript_New/image-20250402192733907.png). This proves that the visual sequence exists in that tutorial, but it **does not enumerate every value in each dropdown**.

The crosswalk JSON retains official URL/evidence/platform notes beside each reviewed entry. Some current-source hits were approximate wording/likely translation matches; those remain explicitly distinguished from exact-name matches.

## Still unresolved after targeted current-doc checks

These labels do not yet have an unambiguous current API/event mapping in this pass:
- `On User Consumable`
- `On Throwable Explodes` — do not assume this equals the separately documented `On Explode` event for other object types.
- `Enable Default Behaviour Tree`
- `Destroy Target`, `Add Attachment`, and `Get Equipment`
- `Restore All Properties`, `Modify properties`, `Set basic properties`, and `Revert to original properties`

Some could be editor-native blocks or module-specific controls rather than ordinary function declarations. Their wording/category needs comparison with the current editor. We should not invent replacements based on similar names.

## Stronger next sources

The [public multilingual tutorial corpus audit](25-public-tutorial-corpus-audit.md) adds PC Block/Element Script, Code Script, Script Additional Notes, formula property and many Mobile template examples. Its [Mobile recipe index](../research/mobile-block-recipe-index.json) records 13 example mechanisms. It is a translated snapshot and is not authoritative for current dropdowns.

For a complete *current* visual-block and dropdown inventory, the highest-value remaining source is a current Studio editor export/editor MCP response or screenshots from its block search/property dropdowns. Studio-generated `EditorGenLib.fcc` may also hold project-specific graph scripts and asset ID enums. We have not yet connected to a running user's editor, so exact current socket/dropdown inventory is still incomplete.

## Required separation in future work

Every item should be classified separately as:
1. current PC code API,
2. current PC visual block and its exact input/output socket types,
3. current Mobile visual block and dropdown values,
4. server/client side restriction,
5. platform restriction,
6. current, deprecated, legacy or unknown,
7. source link and verification status.

A PC function match alone is never enough to infer Mobile block availability or exact visual-block wiring.
