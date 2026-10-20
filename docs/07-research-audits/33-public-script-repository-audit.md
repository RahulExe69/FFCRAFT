# Public Craftland script repository audit

**Checked:** 21 October 2026  
**Purpose:** assess newly discovered public GitHub results for reusable Craftland scripts or additional authoritative metadata.

## Findings at a glance

The latest repository search surfaced three small script-sharing/project repositories and four extra copies of a known resource repository. None supplies an independent complete current script/block catalog.

| Repository | Inspected default-branch evidence | Assessment |
|---|---|---|
| [ateeqkm003-hash/ff-craftland-project](https://github.com/ateeqkm003-hash/ff-craftland-project) | Recursive tree SHA `4a31df3e230a9fc4650f160723d9431c70996128`; one file, a 93-byte README describing a Craftland map. | No code or reusable script data found. |
| [harshdahiya9162-coder/FF-CRAFTLAND-SCRIPT](https://github.com/harshdahiya9162-coder/FF-CRAFTLAND-SCRIPT) | Tree SHA `92a78c6acfd34b1c23d3556f48b5b25dcf183c51`; README plus a 3.6 KB `index.html`. | A small public upload/comment page, not a machine-readable script repository. It includes one informal, unverified example about setting a player's jump property. No editor export or complete script catalog was present. The page submits user-entered script text to an external form service; FFCRAFT did not submit anything to it. |
| [harshdahiya9162-coder/FF-CRAFTLAND-SCRIPTS](https://github.com/harshdahiya9162-coder/FF-CRAFTLAND-SCRIPTS) | Tree SHA `674e225c445f2c8aa983b60a6ad419941cb9004d`; a single 125-byte README. | No script contents or usable API/block metadata found. |
| [nexosstudio/CRAFTLAND_STUDIO_RESOURCES](https://github.com/nexosstudio/CRAFTLAND_STUDIO_RESOURCES) | Recursive tree SHA `aef058e70e4da56669b324ac5ba8fe8a6046e999`. | Canonical resource lead previously audited in [doc 16](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/07-research-audits/16-community-resource-audit.md). |
| [diwashghimire28-creator/CRAFTLAND_STUDIO_RESOURCES](https://github.com/diwashghimire28-creator/CRAFTLAND_STUDIO_RESOURCES), [bl4ck5hadow563-boop/CRAFTLAND_STUDIO_RESOURCES](https://github.com/bl4ck5hadow563-boop/CRAFTLAND_STUDIO_RESOURCES), [DarkShadow190922/CRAFTLAND_STUDIO_RESOURCES](https://github.com/DarkShadow190922/CRAFTLAND_STUDIO_RESOURCES), [sanchezdiego33210-del/CRAFTLAND_STUDIO_RESOURCES](https://github.com/sanchezdiego33210-del/CRAFTLAND_STUDIO_RESOURCES) | Each recursive default-branch tree returned the same SHA `aef058e70e4da56669b324ac5ba8fe8a6046e999` as the canonical repo. | Four mirrors/copies, not four independent evidence sources. Use the canonical repository for indexing and provenance. |

## Broader search result

- Searching GitHub repositories for `craftlandstudio.ffugclanguage` returned the already-inspected [Divyam999hp 1.5.0 mirror](https://github.com/Divyam999hp/craftlandstudio.ffugclanguage-1.5.0), not a second newer public library snapshot.
- A repository search for `Craftland Studio MCP` returned no results at the time checked. The existing [NiteshCraftFF MCP methodology audit](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/07-research-audits/28-live-mcp-repository-audit.md) still has generator scripts but no published raw/generated catalog to import.
- The public leads above may still host creator-submitted material over time. Their existence or titles are not evidence that their examples compile or that their contents are current.

## What to do with these findings

1. Do not count identical tree mirrors as independent source coverage.
2. Keep the Nexos repository as an asset/resource discovery lead, following the quality and license cautions in [doc 16](https://github.com/RahulExe69/FFCRAFT/blob/main/docs/07-research-audits/16-community-resource-audit.md).
3. Do not promote the informal jump-property comment into a recipe without exact block/signature evidence and a reproducible test.
4. Spend the next source effort on current installed `.fcc`/`EditorGenLib.fcc` and live Studio MCP exports, not more repository searches likely to return copies of the same resource tree.

## Provenance

The tree SHAs above were read from public GitHub recursive tree responses on 21 October 2026. Repository search is a snapshot; future commits may change a tree. This audit did not clone or run any project, submit forms, import binaries, or copy third-party code into FFCRAFT.
