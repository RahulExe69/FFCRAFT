# Audit: nexosstudio/Craftland Studio Resources

**Reviewed:** 20 October 2026  
**Repository:** [nexosstudio/CRAFTLAND_STUDIO_RESOURCES](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES)  
**Observed latest commit:** 29 September 2025  
**Classification:** useful community discovery source; not an official Garena reference and not independently verified against a current editor.

## Verdict

**Keep it in FFCRAFT's source map and mine it selectively. Do not adopt it as an authoritative API catalogue or a guaranteed working project template.**

The repository has real value because it collects several resource types in one place: asset ID/name lists, sound identifiers, skybox labels, UGC rig FBX files, project-template folders, and links to Craftland docs and the official VS Code extension. These are the kinds of details that are inconvenient to reconstruct from prose docs alone.

However, several signs mean every item must be treated as a lead until checked: the repository's last observed commit is from September 2025; some catalogues openly describe themselves as samples; its tool page points to an older Studio 1.14 installer while this FFCRAFT research snapshot has already found Studio 1.19.0 patch notes from September 2026; and the Scripts folder's README says “Updating Soon!” rather than documenting usable script examples.

## What is useful

| Area | What was observed | How FFCRAFT should use it |
|---|---|---|
| `Assets/UGC_Type` | Markdown lists for pins, banners, avatars, skyboxes, BGM, sound effects and voice/quick-chat resources | Searchable lookup leads for candidate names/IDs; verify the chosen value in the target version before use |
| `Assets/UGC_Rig` | Male and female UGC costume artist rig FBX files are listed | Potentially useful for asset/animation workflows; inspect license/provenance and compatibility before using in a project |
| `Templates` | Folders named Base Template, Bermuda, Empty and Large Island; inspected roots include `main.gproj`, metadata files, and Assets/ProjectSettings directories | Potential starting points for project structure, but must be opened in the matching Studio version before being called valid templates |
| `Tools/README.md` | Links to Studio, VS Code, Cursor and the Craftland language extension; general Blender/Maya notes | Discovery/installation reference only; use official download pages for current versions |
| `Docs/README.md` | Links back to official Mobile and PC beginner tutorials | Convenient index, not additional technical evidence |
| `Scripts/README.md` | Only says “Updating Soon!” | No usable script recipe was established from this folder during this review |

## Concrete quality and freshness warnings

1. **Stale Studio download link.** `Tools/README.md` links to a direct `CraftlandStudio_1.14.3861343.exe` download. This is older than the 1.19.0 release documented in the official September 2026 patch-note entry. Do not use that link as the recommended current installer; start at Garena's official portal instead.
2. **Explicit sample data.** `Assets/UGC_Type/Avatar IDs.md` calls its list a “sample format” and says the actual list is expected from a JSON file. Do not treat its ten example IDs as a complete or verified avatar catalogue.
3. **Likely stale sound catalogue.** `Sound BGM.md` is organized through OB50-era entries. That can still help locate older identifiers, but it cannot be assumed complete for the current game.
4. **Potential data-quality issue.** `Pin IDs.md` includes an entry rendered as `910031010b`, which is not numeric like the surrounding IDs. Preserve it as a source anomaly and verify it before using it as an ID.
5. **Misleading script extension.** `Tools/test.sh` contains PowerShell commands (`Get-ChildItem`, `Select-String`, `ForEach-Object`), not a portable Bash shell script. Do not run it as a normal `.sh` file without adapting it to the intended shell.
6. **License scope.** The repository declares CC0-1.0. That is a useful reuse signal for material the repository author can license, but it does not independently establish ownership or clearance for third-party game assets, logos, sounds, rigs, or content copied from elsewhere. Keep source attribution and check provenance before redistributing bundled assets.

## Safe workflow for using this source

1. Find a candidate name/ID in the community list.
2. Record the exact file URL and the date/version context.
3. Check the matching current official API/type/enum reference where applicable.
4. In Studio PC, inspect the matching project's generated libraries/assets and use IntelliSense/Go to Definition to confirm the identifier.
5. In Mobile, confirm the item in the current editor UI or a version-stamped export/screenshot; don't infer Mobile support from a PC resource.
6. Test the resource in a small project. Record compile status and runtime behavior separately.
7. In FFCRAFT, mark community-only items as `community-unverified` until they have independent evidence.

## What this changes in the project plan

This repository is useful enough to **index and selectively extract**, especially for asset names and IDs, but not useful enough to justify cloning its whole contents into FFCRAFT. Keep upstream URLs instead of duplicating binary assets. The next high-value extraction is a small set of asset records that are independently confirmed in official/current editor sources—not a bulk import of every sound or pin entry.

## Key links

- [Upstream repository](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES)
- [Upstream README](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES/blob/main/README.md)
- [Asset type catalogue](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES/tree/main/Assets/UGC_Type)
- [Templates](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES/tree/main/Templates)
- [Tools README](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES/blob/main/Tools/README.md)
- [Official Garena portal](https://ffcraftland.garena.com/en/)
- [Official patch notes](https://ffcraftland.garena.com/en/patch-notes/)
