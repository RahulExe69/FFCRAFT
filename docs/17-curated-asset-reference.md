# Curated Craftland asset reference (verified subset)

**Checked:** 20 October 2026  
**Purpose:** connect natural-language asset descriptions to exact documented identifiers without bulk-copying community binary assets.

## Officially documented skybox base types

Garena's public enum reference lists these six SkyboxType values. The identifiers are officially documented; whether a specific package file is available and usable in a particular installed editor is a separate check.

| Player-facing name | Exact enum value | Script name | Community package lead | Evidence |
|---|---|---|---|---|
| Daytime | UGC_SKYENV_DAY | Day | [Sky_Day.package](https://github.com/nexosstudio/FE_RESOURCES_BETA/blob/main/Official_SkyBox/Sky_Day.package) | Official enum; package untested |
| Night | UGC_SKYENV_NIGHT | Night | [Sky_Night.package](https://github.com/nexosstudio/FE_RESOURCES_BETA/blob/main/Official_SkyBox/Sky_Night.package) | Official enum; package untested |
| Dusk | UGC_SKYENV_EVE | Dusk | [Sky_Eve.package](https://github.com/nexosstudio/FE_RESOURCES_BETA/blob/main/Official_SkyBox/Sky_Eve.package) | Official enum; package untested |
| City View | UGC_SKYENV_CITY | City | [Sky_City.package](https://github.com/nexosstudio/FE_RESOURCES_BETA/blob/main/Official_SkyBox/Sky_City.package) | Official enum; package untested |
| Colorful Sky | UGC_SKYENV_COLORFULSKY | Colorful | [Sky_ColorfulSky.package](https://github.com/nexosstudio/FE_RESOURCES_BETA/blob/main/Official_SkyBox/Sky_ColorfulSky.package) | Official enum; package untested |
| Frost Galaxy (official description: Frost Moon) | UGC_SKYENV_SNOW | FrostGalaxy | [Sky_Snow.package](https://github.com/nexosstudio/FE_RESOURCES_BETA/blob/main/Official_SkyBox/Sky_Snow.package) | Official enum; package untested |

Official source: [Garena SkyboxType enum reference](https://ffcraftland.garena.com/en/docs/enum/).

## How to interpret these records

- **Official enum verified** means the identifier, display name, and script name are present in Garena's public enum reference.
- **Package untested** means the linked .package exists in a community repository, but FFCRAFT has not imported it, inspected internal metadata, or validated it in a live project.
- A matching filename is a useful lead, not proof that the package is official, safe, current, or compatible.
- The package files are not copied into FFCRAFT. Use upstream links and verify provenance before redistributing them.
- Community-only entries such as Sky_Fantasy_Night.package, Sky_Hippo.package, Sky_Sunist_Rainy.package, and numbered sky_01.package through sky_44.package are not mapped to official enum values here. Their visual identity, package format, and support status remain unverified.

## Suggested use in future answers

If Rahul asks for “day sky”, “night sky”, “dusk”, “city sky”, “colorful sky”, or “frost galaxy”, start from the exact documented enum value above. Then check:
1. Mobile block/editor path versus Studio PC code path.
2. The current installed editor's accepted type/value and property setter.
3. Whether the requested operation is static scene configuration or a runtime change; do not invent a runtime setter.
4. Import/package availability in the project and a real editor test.

## Next verification step

Use the current installed Craftland Studio and its generated library/type information to verify the property or API that consumes SkyboxType. The enum alone does not establish that a runtime skybox-change API exists, nor that these binary packages can be imported independently.
