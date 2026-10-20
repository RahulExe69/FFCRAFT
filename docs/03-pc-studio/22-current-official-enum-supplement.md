# Current official enum and type supplement

This supplement records current official documentation findings that are missing from, or more specific than, the third-party Craftland Studio language-library mirror cataloged in [doc 20](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/03-pc-studio/20-pc-library-catalog.md).

Machine-readable form: [`research/current-official-enum-supplement.json`](https://github.com/RahulExe69/FFCRAFT/blob/main/research/pc-studio/current-official-enum-supplement.json).

## Fixed enum options recovered from current official docs

| Official identifier | User-facing label | Documented entries |
|---|---|---|
| `RenderQualityType` | Render Quality Type | `Low=0`, `Medium=1`, `High=2`, `Ultra=3` |
| `EntityFlag` | Entity Flag | `Default=0`, `Static=1`, `Local=2`, `RenderOnly=4` |
| `DebugCommandType` | Debug Command Type | Invulnerable, Restore HP, Self-Eliminated, Teleport to Spawn Point, Add Bot, Change Viewport, End Current Phase |
| `FilterType` | Filter Type | None, Comic Book, Sketch, Pixel, RGB Split, Golden Era, Cyberpunk |
| `DistanceSourceType` | Distance Source Type | Player Camera, Player Character, Custom Entity |
| `DistanceSpaceType` | Distance Space Type | 3D World, Horizontal XZ, Screen Space |
| `DismemberType` | Torn Limb Type | None, Head, Left Arm, Right Arm, Left Leg, Right Leg |

The value/name/script-name details are preserved in the JSON, with the official source URL for each. These are **currently documented** values; exact editor availability still depends on module, platform, and context.

## Type selector versus fixed enum

The official Enum reference identifies `TypeEnum` (“Type Enum”) as a list of all available types. That is a type-system selector, not a small hard-coded set of scalar values. It should not be treated as “missing values” in the same way as a fixed enum.

The official Level Object module also documents these selectors:

- `WeaponSkinType` — Weapon Skin ID
- `VehicleSkinType` — Vehicle Skin ID
- `ClothType` — Outfit ID
- `BagSkinType` — Backpack Skin ID
- `TextureType` — Texture ID
- `LevelObjectType` — automatically generated based on the type of level object

For the skin types, the official reference confirms the category/type mapping, but this audit has **not** recovered a complete current list of all possible skin IDs. Those likely need dedicated current asset catalogues or project/editor-generated data. The old mirror's missing a type is not proof that it doesn't exist.

## Verification and sources

- [Official enum reference](https://ffcraftland.garena.com/en/docs/enum/)
- [Official Type reference](https://ffcraftland.garena.com/en/docs/type)
- [Official Level Object module](https://ffcraftland.garena.com/en/docs/module-26)
- [Official Get Render Quality API](https://ffcraftland.garena.com/en/docs/api-40-940)

The current Get Render Quality page labels the API **Client Side** and **Both Mobile and PC**, a useful reminder that current official API documentation can expose new enums absent from the older PC language-library mirror. This page does not claim every new enum is available as a dropdown in every visual script context.
