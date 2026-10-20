# Live Craftland MCP export lead: public repository audit

**Checked:** 20 October 2026  
**Source snapshot:** [NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL, commit `4d30fcd0970074fc8c19689f747b6c6b49f93cf3`](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL/commit/4d30fcd0970074fc8c19689f747b6c6b49f93cf3)  
**Purpose:** find reusable public evidence for the current Craftland Studio MCP data model and the missing block/action/valuation/type metadata.

## Finding

A recent public repository describes a knowledge-base generator based on a live Craftland Studio MCP session. Its README reports an export dated **6 August 2026** from a session labelled `craftland-stealapet` / `user-craftland-stealapet`, and advertises these totals:

| Area | Count claimed in the source README |
|---|---:|
| Blockly block types | 145 |
| Modules | 46 |
| Events (merged unique names) | 283 |
| Actions | 450 |
| Valuations | 229 |
| Types | 657 |

These are **the repository author's reported counts**, not counts independently reproduced in FFCRAFT. They should be treated as an excellent lead, not as a verified catalog.

## What is actually public in that commit

The complete recursive tree at commit `4d30fcd0970074fc8c19689f747b6c6b49f93cf3` has only five files:

- [`README.md`](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL/blob/4d30fcd0970074fc8c19689f747b6c6b49f93cf3/README.md)
- [`_generate_kb.ps1`](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL/blob/4d30fcd0970074fc8c19689f747b6c6b49f93/_generate_kb.ps1)
- [`_enrich_from_gets.ps1`](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL/blob/4d30fcd0970074fc8c19689f747b6c6b49f93/_enrich_from_gets.ps1)
- [`_save_action_batch.ps1`](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL/blob/4d30fcd0970074fc8c19689f747b6c6b49f93/_save_action_batch.ps1)
- [`variables.md`](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL/blob/4d30fcd0970074fc8c19689f747b6c6b49f93/variables.md)

The README refers to generated folders such as `blocks/`, `events/`, `actions/`, `valuations/`, `types/`, `indexes/` and `raw/`, but those folders and the claimed per-item export pages are **not present in the inspected public tree**. So we cannot responsibly import its claimed records from GitHub as they are not actually published there.

## Useful implementation clues

The public scripts and README still tell us how to approach the current editor data:

- The author refers to `eca-block-config-list`, `eca-block-config-get`, `eca-get-event`, `eca-get-action`, `eca-get-valuation`, `eca-get-type`, and graph-variable inspection tools. These names are documented here as **reported by the community exporter**, not as an official public MCP protocol specification.
- The README describes generic Blockly node families such as `a`, `v`, `e` and `ife1`, and says generic API nodes require a valid `configId` in `extraState.X`. This is a concrete hint for preserving node identity and action configuration instead of indexing only by display label.
- The generator keeps unknown fields as `UNKNOWN` instead of making up parameter lists. FFCRAFT should follow that rule.
- It distinguishes server/client ECA targets and records deprecated API levels. Those fields could help explain why an item appears in one script context but not another.

## What this does not prove

- The public repository does not provide the raw MCP responses or generated catalog pages, so its advertised counts and per-item records are not independently auditable from the published tree.
- The exported session name suggests a specific project/context; its block graph names, registered assets and project-generated types may be project-specific rather than a complete global catalog.
- This is a **Craftland Studio PC** lead. It does not establish parity with Craftland Mobile visual blocks or their dropdown options.
- GitHub's repository metadata did not return a declared license for the source project. Link to the scripts as a methodology lead; do not copy their code or assume permission to redistribute data from the session.

## Next capture steps

1. From a current Studio 1.19.x installation, export the MCP block-config list and detailed definitions for every config, preserving raw JSON, editor version, context and source method.
2. Export event/action/valuation/type details through the available `eca-get-*` operations, retaining exact names, IDs, parameter schemas, return/output data, runtime target and deprecation markers.
3. Store raw responses separately from normalized/search indexes, and record a hash for each source payload.
4. Compare the resulting inventory against the 443 source lines in [the Rough block-symbol crosswalk](24-block-symbol-crosswalk.md).
5. Keep a separate Mobile queue for actual Mobile editor screenshots or exports. Do not fill Mobile gaps by copying PC MCP results.

## Sources

- [Craftland Studio 1.19.0 official patch notes](https://ffcraftland.garena.com/en/patch-notes/) — confirm that the editor includes an MCP server for Blocks, Scripts, Scenes, UI, Animation Controllers and more, with the URL available inside the running editor.
- [Public MCP-derived KB repository](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL)
- [Public KB generator](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL/blob/4d30fcd0970074fc8c19689f747b6c6b49f93cf3/_generate_kb.ps1)
- [Public enrichment script](https://github.com/NiteshCraftFF/CRAFTLAND-STUDIO-TUTORIAL/blob/4d30fcd0970074fc8c19689f747b6c6b49f93cf3/_enrich_from_gets.ps1)
- [Current-editor capture playbook](27-current-editor-capture-playbook.md)
