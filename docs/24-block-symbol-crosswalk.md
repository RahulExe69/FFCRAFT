# Block-symbol crosswalk for Rough.txt

## Purpose

The original `Rough.txt` remains untouched. This crosswalk compares each extracted line in `research/user-observed-block-inventory.json` against both the recovered PC function/event/component/property declarations and targeted current official API/event pages.

Machine-readable result: [`research/block-symbol-crosswalk.json`](../research/block-symbol-crosswalk.json).

## Comparison result

The initial old-library pass across 443 extracted lines found 306 exact normalized matches, 113 approximate candidates, 21 lines without an exact mirror match, and 3 likely explanatory notes. A later official-doc cross-check added 34 official reference links and upgraded 23 entry statuses.

**Latest entry status (21 October 2026):**
- **306** exact normalized matches to an old-mirror symbol name or documentation title.
- **23** entries mapped to a current official reference.
- **92** approximate candidates still requiring review.
- **18** lines with no exact match in the older mirrored libraries.
- **1** likely editor-native block rather than a runtime API.
- **3** entries likely explanatory notes rather than blocks.

The older 1.5.0 mirror remains a *discovery source*, not the live support matrix. There are 111 entries in the focused review queue: the 92 fuzzy candidates, 18 mirror misses and one likely editor-native block. Neither a match nor a miss proves current availability or Mobile/PC parity. See [the prioritised review queue](31-rough-block-review-queue.md).

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

## Formerly unresolved group: current official mappings found

A subsequent pass over the current Garena module/API pages resolved the earlier ten-item **API/event identity** gap. The exact visual editor node and its socket layout are still not captured for every item, so this is a documentation mapping—not a claim that each block has been reproduced or runtime-tested.

| Rough.txt observation | Current official mapping | Important distinction |
|---|---|---|
| `On User Consumable (ConsumableID, Item, Spawned Item)` | [On Use Consumable / `OnUseConsumable`](https://ffcraftland.garena.com/en/docs/module-15) | The official Items module lists this event and the three parameters. The old mirror marks it server-side; confirm current runtime side before generating cross-platform code. |
| `On Throwable Explodes (Hit Position)` | [On Throwable Explode / `OnThrowableExplode`](https://ffcraftland.garena.com/en/docs/module-15) | Keep separate from the Level Object `On Explode` event for vehicles/explosive barrels. |
| `Enable Default Behaviour Tree` | [Enable Default Behavour Tree / `EnableDefaultBTree`](https://ffcraftland.garena.com/en/docs/module-9) | The official page itself uses “Behavour”; do not silently normalize the editor's displayed spelling. Confirm platform flags. |
| `Destroy Target: Target, Item, Count` | [Destroy Item / `DestroyItem`](https://ffcraftland.garena.com/en/docs/api-15-147) | This is deletion of a specified item quantity from a player's inventory, not generic entity destruction. |
| `Add Attachment` | [Add Attachments / `AddAttachments`](https://ffcraftland.garena.com/en/docs/api-15-605) | Official description includes slot matching and duplicate replacement behavior. |
| `Get Equipment` | [Get Equipments / `GetEquipments`](https://ffcraftland.garena.com/en/docs/api-15-607) | Official API refers to equipment in the backpack equipment column. |
| `Restore All Properties` | [Clear Formula Property Factor / `ClearFormulaPropertyFactor`](https://ffcraftland.garena.com/en/docs/api-24-182/) | Clears formula factors for all calculable properties; not a generic property reset. |
| `Modify properties` | [Set Formula Property Relative / `SetFormulaPropertyRelative`](https://ffcraftland.garena.com/en/docs/api-24-186/) | Official API says **Server Side, Only Mobile**. This modifies a formula factor using a relative operation; it is not a direct property setter. |
| `Set basic properties` | [Set Formula Property Absolute / `SetFormulaPropertyAbsolute`](https://ffcraftland.garena.com/en/docs/api-24-187/) | Official API says **Server Side, Only Mobile**. This sets the base value of a calculable property, not the generic STD Library `Set Property`. |
| `Revert to original properties` | [Remove Formula Property Factor / `RemoveFormulaPropertyFactor`](https://ffcraftland.garena.com/en/docs/api-24-188/) | Official API says **Server Side, Only Mobile**. Removes the formula modification for one property; it is distinct from clearing all formula factors. |

The machine-readable [crosswalk](../research/block-symbol-crosswalk.json) now records these official references, canonical identifiers, and platform/context caveats. The previous ten-item unresolved-after-official-check group is no longer unresolved at the **official reference** level. Remaining work is to capture the current editor's actual block labels, sockets, dropdown values and runtime behavior where relevant.

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
