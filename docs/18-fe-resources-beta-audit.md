# Audit: nexosstudio/FE_RESOURCES_BETA

**Reviewed:** 20 October 2026  
**Repository:** [nexosstudio/FE_RESOURCES_BETA](https://github.com/nexosstudio/FE_RESOURCES_BETA)  
**Latest observed commit:** 7 March 2026 (feat: official ffcl skybox)  
**Repository metadata:** public, CC0-1.0 declared, approximately 67 MB according to GitHub repository metadata at review time.

## Verdict

This is more valuable as a sample-project/package resource than as a text documentation source. Unlike the sibling repository, it includes actual .package files for skyboxes and small feature packages that appear to target Craftland map projects. It is worth testing in Studio, but we must not call any package compatible or working until it has been imported and exercised in the intended editor version.

## Observed contents

| Path | Contents observed | Value for FFCRAFT | Current evidence status |
|---|---|---|---|
| Official_SkyBox/ | 22 .package files, including Sky_Day, Sky_Night, Sky_Eve, Sky_City, Sky_ColorfulSky, Sky_Snow, plus themed skies | Candidate visual resources; six filenames align with documented base skybox enum names | Enum identifiers verified separately; package files untested |
| All_Skybox/ | 44 numbered files sky_01.package–sky_44.package | Potential additional skybox variants | Names/appearance/importability not verified |
| Dynamic_Weather/ | v1.package and notes.png | High-value candidate for weather changes and timing logic | Must inspect notes and import/test package before deriving implementation |
| Voting_System/ | Pkg_01.package and Pkg_02.package | High-value candidate for voting UI/state/decision logic | Package contents and security/round behavior unverified |
| .github/ | Preview images for Dynamic Weather and All Skybox | Useful for visual orientation, not implementation proof | Preview only |
| README.md | Short overview and a YouTube demo link | Leads to creator context | Not a technical specification |

The four directories contain 68 package files in total: 22 named skybox packages, 44 numbered skybox packages, one weather package, and two voting packages. The skybox package collection alone is tens of megabytes, so FFCRAFT should link to upstream files rather than duplicate all binaries.

## Useful next targets

1. **Dynamic Weather** — likely the best next sample to inspect because it can teach how a reusable map mechanic is packaged and configured. Read the notes/preview first and import the package before claiming its implementation.
2. **Voting System** — useful for a complete gameplay mechanic, but inspect its package structure and server/client boundaries before reusing it. Votes should be validated and tallied authoritatively; never assume a client-side count is cheat-resistant.
3. **Named skyboxes** — start with the six exact base types already listed in [the curated asset reference](17-curated-asset-reference.md). Other named skyboxes and the numbered collection need individual identification and current-version testing.

## Caveats

- The repository's CC0 declaration does not prove the repository author owns every included game asset or that Garena-origin assets can be redistributed without restriction. Treat binary provenance separately from the repository-level license.
- A .package filename and preview screenshot do not establish the editor version, internal dependencies, whether the package is importable on Mobile, or whether the feature works on current Studio PC.
- The name “Official_SkyBox” is the upstream folder name, not independent proof that each bundled binary is official.
- The latest commit we observed updates the skybox collection in March 2026. This is newer than the sibling resource repository's observed September 2025 commit, but still predates the September 2026 Studio 1.19.0 patch-note snapshot.
- We have not extracted, executed, decompiled, or imported any package. No code from this repository has been copied into FFCRAFT.

## Verification checklist

For each package, record:
- SHA/file URL and upstream commit.
- Craftland Studio version and target platform.
- Import success/failure and any missing dependencies.
- Visible editor objects/blocks/UI elements created by the package.
- Script names, events, parameters, and server/client placement confirmed in the editor.
- Runtime behavior, including reconnect/round reset/leave cases where relevant.
- Whether the sample is a useful design pattern or safe to reuse.

## Links

- [Repository](https://github.com/nexosstudio/FE_RESOURCES_BETA)
- [README](https://github.com/nexosstudio/FE_RESOURCES_BETA/blob/main/README.md)
- [Dynamic Weather](https://github.com/nexosstudio/FE_RESOURCES_BETA/tree/main/Dynamic_Weather)
- [Voting System](https://github.com/nexosstudio/FE_RESOURCES_BETA/tree/main/Voting_System)
- [Named skyboxes](https://github.com/nexosstudio/FE_RESOURCES_BETA/tree/main/Official_SkyBox)
- [Numbered skyboxes](https://github.com/nexosstudio/FE_RESOURCES_BETA/tree/main/All_Skybox)
- [Official Garena enum reference](https://ffcraftland.garena.com/en/docs/enum/)
