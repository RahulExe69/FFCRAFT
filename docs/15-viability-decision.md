# FFCRAFT viability decision and effort budget

**Checked:** 20 October 2026  
**Decision:** **GO — with a narrow, proof-first scope.**  
**Purpose:** avoid spending time building a duplicate of tooling that Craftland already provides.

## Executive decision

FFCRAFT is worth maintaining as a **cross-platform, evidence-backed implementation assistant** for Craftland ideas. It is not worth trying to manually reproduce the entire Craftland API reference, every asset catalogue, or a second full editor.

The useful deliverable is: describe a gameplay mechanic in normal language, then get a platform-appropriate implementation plan with exact block wiring or code, known dependencies, setup steps, and tests—with uncertain pieces clearly flagged instead of invented.

## What the research verifies

### Craftland Mobile

- Garena publishes a distinct Mobile beginner tutorial and Craftland Wiki, including a full block-scripting guide.
- The official block editor supports events, typed input slots, script contexts, block export/import and reusable templates.
- The visible block list depends on the active script context. A block that appears in search is not necessarily usable in the current script.
- Mobile is therefore a good target for **visual-block instructions**. The most useful source material is the exact current editor labels/slot shapes, exported block snippets, and version-stamped screenshots—not a guessed translation from PC code.

Official references: [Mobile block scripting](https://ffcraftland.garena.com/en/tutorial/cl/4-101), [Craftland beginner tutorial](https://ffcraftland.garena.com/en/tutorial/cl/3).

### Craftland Studio PC

- The official PC manual supports graphical logic and code scripts. The code-script guide documents `.fcg` scripts and `.fcc` libraries and points to the editor's installed release libraries.
- API reference pages explicitly identify runtime side and platform scope; some APIs are PC-only, client-only, server-only or obsolete.
- Garena's September 2026 release notes for Studio 1.19.0 say the editor includes AI Smith conversational assistance and an MCP server for working with Blocks, Scripts, Scenes, UI, Animation Controllers, and more. Earlier notes also describe improvements to AI-assisted FCC search/completion/referencing.
- This native AI capability overlaps with generic PC code-generation assistance. FFCRAFT should supplement it with portable project context, Mobile block guidance, evidence tracking, and tested mechanic recipes—not pretend the native features do not exist.

Official references: [PC manual](https://ffcraftland.garena.com/en/tutorial/fe/1), [PC code scripts](https://ffcraftland.garena.com/en/tutorial/fe/1-9), [official patch notes](https://ffcraftland.garena.com/en/patch-notes/), [API reference](https://ffcraftland.garena.com/en/docs/api).

## Where FFCRAFT adds value

1. **One mechanic, two distinct implementations.** Preserve the differences between Mobile block graphs and Studio PC code; do not force them into a false one-to-one mapping.
2. **A searchable home for author-observed blocks.** `Rough.txt` and the derived catalogue preserve labels that may be hard to find in official prose, while keeping unverified items marked as such.
3. **Reliable instructions rather than plausible-looking code.** Record exact inputs/outputs, script context, runtime side, platform availability, enum values, asset dependencies, setup steps and evidence.
4. **Recipes and failure handling.** Turn validated mechanics into reusable patterns, including reset behavior, edge cases and a small playtest checklist.
5. **A version-aware external memory.** Track source URL, editor version and verification level so old/obsolete names do not silently become the default.

## What is not proven yet

- The 443 extracted candidate lines from `Rough.txt` are **not** 443 verified/current blocks.
- The current machine-readable inventory is a heuristic transcription, not a complete parse of the editor.
- AI Smith/MCP support is documented for Craftland Studio PC; do not assume the same workflow exists in the Mobile editor.
- Public docs are enough to resolve many questions, but may not show every exact visual-block shape, asset ID, installed library declaration, or editor-only constraint.
- Nothing in this repository has been compiled or live-playtested merely because a recipe is documented.

## Do we need to install anything?

**Not for the next research step. Do not install anything just to keep this project moving.**

Use this evidence ladder:

| Goal | Minimum useful evidence | Is Studio PC install needed? |
|---|---|---|
| Explain a Mobile visual-block mechanic | Official Mobile guide plus current screenshots/exported block snippets for unclear shapes | No |
| Draft code from public documented APIs | Exact official API/event/type/enum pages and side/platform checks | No |
| Confirm exact installed `.fcc` signatures, editor-only asset registrations, or imports | Matching Studio version and its installed release libraries/project files | Usually yes, or obtain those files from the user |
| Prove a PC script compiles and behaves correctly | Target editor, compile output and controlled playtest | Yes |
| Prove Mobile blocks behave correctly in-game | Matching Mobile editor/build and controlled map test | Use Mobile; PC Studio is not a substitute |

If exact Studio PC work becomes the priority, the official manual points to the installed library folder `Craftland Studio\\resources\\LocalData\\Utilities\\UGCLanguage\\release`. Do not treat arbitrary downloaded `.fcc` files or old community snippets as authoritative without matching versions and provenance.

## Next action: a small proof of value, not a bulk scrape

Build one **vertical-slice mechanic** all the way from a natural-language request to usable instructions:

1. Choose a small, common mechanic with a clear success condition.
2. Define acceptance criteria and choose a Mobile block-graph implementation and a separate PC code implementation where both are supported.
3. Verify only the events, APIs, types, enums and inputs that mechanic actually needs against official sources.
4. Show every block's script scope and wire/slot connections, or supply the PC script with imports and server/client constraints.
5. Add setup instructions and a test matrix; leave any unavailable exact identifier as an explicit unknown.
6. Record which parts are docs-verified, editor-verified, compiled, and playtested.

After that pilot, evaluate how much detail is still missing. Expand the catalogue only where a real implementation encountered a gap. The first pilot is a **static research output** until we have editor evidence; it must not be labelled compiled or playtested prematurely.

## Stop/go criteria

Continue investing if the pilot produces actionable, non-invented steps and materially reduces the number of details the creator must look up manually. Narrow the scope if Studio's native AI/MCP handles PC work better and the repository adds little there. Keep Mobile block recipes and cross-platform caveats if those remain helpful. Do not build a custom app, external MCP client, or exhaustive bulk index until this pilot shows a real gap that requires one.

## Source links

- [Official Craftland portal and Mobile/PC entry points](https://ffcraftland.garena.com/en/)
- [September 2026 Studio 1.19.0 notes, including AI Smith and MCP](https://ffcraftland.garena.com/en/patch-notes/)
- [Mobile block scripting guide](https://ffcraftland.garena.com/en/tutorial/cl/4-101)
- [PC code-script guide and installed libraries](https://ffcraftland.garena.com/en/tutorial/fe/1-9)
- [API reference](https://ffcraftland.garena.com/en/docs/api)
