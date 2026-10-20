# Unresolved Rough.txt block review queue

**Prepared:** 21 October 2026  
**Source:** [Machine-readable queue](../research/rough-block-review-queue.json)  
**Original notes:** [Rough.txt](../Rough.txt) — unchanged.

## Current crosswalk status

The line-by-line crosswalk covers **443 extracted entries**. The latest mutually exclusive status labels are:

| Status | Count | Interpretation |
|---|---:|---|
| Exact normalized label or documentation-title match in old mirror | 306 | Candidate lookup hit only; not a current support guarantee. |
| Current official reference found | 23 | Official page mapped; exact editor sockets and runtime remain separate. |
| Approximate candidate needs review | 92 | Similarity lead only; do not generate code from this alone. |
| No exact match in old library mirror | 18 | Could be newer, editor-native, a constructor/flow-control node, or different wording. |
| Likely editor-native rather than runtime API | 1 | Inspect the editor block itself. |
| Likely explanatory notes | 3 | Preserve as author notes rather than runtime APIs. |

The pre-official comparison counted 113 approximate candidates and 21 old-mirror misses. A later targeted pass mapped 23 entries to official current references, leaving **111 review entries**: 92 approximate, 18 no-match, and one likely editor-native. The machine-readable source retains provenance and candidates for each line.

## Capture these first

These old-mirror misses are the clearest prompts to inspect the current editor UI/MCP or collect current Mobile screenshots. The mirror is version 1.5.0 and does not define the current support boundary.

| Rough.txt line | Observed label | Why inspect it |
|---:|---|---|
| 132 | Progressive Movement Property | Action-like node absent from old mirror; verify target/property/value slots and movement semantics. |
| 451 | Multi-slot arithmetic/operator node | Capture operator choices (+, -, *, /, %) and add-slot behavior. |
| 500 | Quaternion Rotate Toward | Verify current declaration, parameter types, units and output. |
| 511 | Modify (List) | Establish which mutation operation the block performs and how index/value sockets are typed. |
| 541–543 | Vector X/Y/Z component getters | Capture labels and output types; do not silently normalize the rough spelling. |
| 145 | Add Comment | Likely editor-native rather than a runtime function; capture the visible node schema separately. |

## Likely block syntax rather than ordinary API symbols

These remain in the queue because they describe the *shape* of data/control blocks; a runtime-library search is a weak test for them:

- Lines 436, 437, 439 and 442: string, Vector3, Boolean and NULL literal/constructor blocks.
- Lines 660, 662 and 664–667: if/if-else, conditional loop, integer-range loop, for-each, and break/continue control-flow blocks.
- Line 647: the old label “Phase And Round Enum”. Official Workflow documentation describes Phase/Round as configured entities with IDs/indices, scripts and separate lifecycle events; a fixed enum is **not confirmed**. See [Workflow documentation](https://ffcraftland.garena.com/en/tutorial/fe/1-14/).

The full queue also retains the other 92 fuzzy candidate lines with up to three closest old-library names/signatures and a line-specific review action.

## Recommended review protocol

1. Find the block in the current target editor. Record editor version, Mobile/PC, script type, scope and category.
2. Capture the entire block with connected sockets, then expand each dropdown and photograph every scrolled segment.
3. Record visible labels separately from internal IDs/script names; preserve defaults, output types, platform and server/client annotations.
4. Compare with official docs and the old mirror only after recording the editor observation.
5. Mark runtime-tested only after compilation/playtest output is captured. Do not expose a private MCP endpoint or tokens; share exported JSON/screenshots instead.

## What this queue does not mean

It is **not** a list of 111 broken or unsupported blocks. Approximate rows can be typos, different display wording, constructors or different concepts; old-mirror misses may exist in the live editor. This is a focused capture queue, not proof of absence.

## Related evidence

- [Rough block-symbol crosswalk](24-block-symbol-crosswalk.md)
- [Current official dropdown option cross-checks](30-current-official-dropdown-option-crosschecks.md)
- [Official Mobile scripting source map](29-official-mobile-scripting-source-map.md)
- [Current editor capture playbook](27-current-editor-capture-playbook.md)
- [Public PC library catalog](20-pc-library-catalog.md)
