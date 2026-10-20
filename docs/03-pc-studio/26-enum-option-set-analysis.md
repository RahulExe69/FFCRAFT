# Enum option-set duplication analysis

Machine-readable result: [`research/pc-enum-option-set-analysis.json`](https://github.com/RahulExe69/FFCRAFT/blob/main/research/pc-studio/pc-enum-option-set-analysis.json).

## Result

The 42-file public extension-library mirror includes 144 enum declarations and 144 distinct enum names. Among those, **42 groups of differently named enums have the exact same ordered name/value member list**, accounting for 759 member rows that would be repetitive if displayed in a single browsing interface.

Examples include:
- `DynamicCreateLevelObjectType` and `DynamicCreateItemID` — 155 values each.
- `SoundEffectType` and `SoundEffects` — 102 values each.
- `VFXType` and `EffectType` — 71 values each.
- `PlayerUISwitchType` and `PlayerHudSwitchType` — 63 values each.
- `BuiltInUIType` and `InternalHudType` — 61 values each.
- `WidgetType` and `HudWidgetType` — 32 values each.

## How to use this

When looking up a dropdown, we can inspect an identical member list once for efficiency, then store that list under every original type name with its source module and API context. **Do not merge or rename the types**: different names can have different semantic roles, availability and deprecation status even when their options match in this old mirror.

These are exact matches in a third-party extension snapshot—not proof of current API equivalence, and not proof every list is a visual dropdown on both Mobile and PC. Verify changed lists against current official docs and the installed editor.
