# AI Craftland coding workflow

## Purpose

Turn a natural-language gameplay idea into a well-scoped Craftland implementation while using FFCRAFT as a persistent external knowledge base. This document is an operating procedure for future coding sessions; it does not claim that every current or future conversation automatically loads the repository.

## Required knowledge lookup order

1. Read the repository `README.md` and `docs/00-research-method.md` for scope and evidence rules.
2. Read `docs/01-platform-and-fundamentals.md` and the relevant runtime/block/code docs.
3. Search `research/user-observed-block-inventory.json` and `docs/12-user-observed-block-inventory.md` for the exact candidate blocks, input slots, and reported outputs.
4. Check `docs/13-official-cross-checks.md`, official API/Event/Type/Enum docs, and the current editor/library for deprecation and platform availability.
5. Inspect asset registries, `.fcc` libraries, exported project files, or editor screenshots when a required asset, enum dropdown, block shape, or signature cannot be confirmed from public references.

## Evidence states

Use these states separately. Never collapse them into a single vague claim that something is 'working'.

| State | Meaning |
|---|---|
| `user-observed-unverified` | Reported by the author or extracted from `Rough.txt`; not checked independently. |
| `official-docs-verified` | Exact current official reference located; include the URL and checked details. |
| `editor-verified` | Exact label/slot/value confirmed in the installed Craftland editor. |
| `compiled` | The relevant code/script artifact successfully parsed or compiled in the intended environment. |
| `playtested` | Behavior observed in a controlled Craftland test map or match, with version and reproduction notes. |
| `obsolete` / `deprecated` | Official or editor evidence marks the entry obsolete; do not recommend for new implementation unless there is a specific compatibility need. |

## Natural-language feature workflow

### 1. Turn the idea into acceptance criteria

Capture player-visible behavior, trigger conditions, timing, reset behavior, edge cases, and how success will be measured. If the user's intent is clear, make reasonable assumptions explicit and proceed rather than interrogating them.

### 2. Choose the runtime and script attachment

Identify the target authoring environment: Craftland Mobile, Craftland Studio PC, or both. Select a valid script context and runtime side. Distinguish global, party/team, player, individual object, trigger, and UI scopes according to the target editor; do not assume the user's `TEAM` label automatically means the official guide's `party` scope.

### 3. Design the event/state flow

Write the event sequence, authoritative state owner, variable types, object references, resets, and client/server communications before producing implementation steps. Keep scoring, inventory grants, win conditions, and other match-critical decisions on the authoritative side where the documented runtime supports that design.

### 4. Resolve exact blocks, APIs, enums, and assets

For every nontrivial dependency, record:

- Canonical name and exact displayed/editor identifier.
- Required input slot names and types.
- Return/output names and types.
- Valid script context and server/client side.
- Craftland Mobile / Studio PC availability.
- Enum values, asset IDs, registered dependencies, and import requirements.
- Source URL, editor version, deprecation state, and evidence state.

If an exact name or enum value cannot be verified, do not invent one. Use a clearly marked placeholder only in a design draft, and name the evidence required to resolve it.

### 5. Generate the form that fits the target

**For visual block scripts:** give the exact script scope, event block, execution order, nested blocks, input types/values, output wiring, and required object/UI attachment. Explain where every variable or function must be created.

**For Craftland Studio PC code scripts:** use the documented `.fcg`/`.fcc` workflow and exact current API signatures. Respect server/client boundaries, imports, static scripts, async requirements, and platform gates. Don't translate a visual block signature into code by guesswork.

**For both:** keep shared game logic conceptually aligned while allowing different implementation details where the two environments differ.

### 6. Supply a validation plan

Every generated implementation should include a compact test matrix covering expected success, missing or invalid targets, empty player/team lists, reconnects or duplicate events where relevant, round/phase resets, platform/runtime mismatches, and cleanup. Note whether validation is a static review, editor check, compile, or actual playtest.

## Standard response deliverable

For an implementation request, prefer this order:

1. **Implementation plan:** expected behavior and chosen runtime/scope.
2. **Dependencies:** verified blocks/APIs, enum values, and assets, each with evidence state.
3. **Implementation:** code files or step-by-step block graph/wiring instructions appropriate to the target.
4. **Setup:** script attachment, asset registration/import, configuration, and any editor operations.
5. **Validation:** test cases, failure modes, and known limitations.
6. **Unknowns:** only the unresolved facts that materially block correctness.

## Repository maintenance rules

- Preserve `Rough.txt` as the author's raw notes; never rewrite it as a side effect of cataloguing.
- Add canonical/verified values beside the raw transcription rather than silently replacing the source label.
- Store enum type names separately from their individual enum values, and both separately from API parameter types.
- Treat screenshots, editor exports, installed release `.fcc` libraries, and live test evidence as distinct sources, with version metadata.
- When correcting a record, record the evidence URL, checked date, editor version when available, and prior alias/transcription.
- Re-check official patch notes and deprecation pages before making claims about the latest supported API.
- Never describe a recipe as compiled or playtested unless that happened in the target environment.

## Current gap

The user-authored catalogue currently contains 65 enum-like type names and hundreds of candidate block/component signatures, but it does not yet contain all dropdown values, asset IDs, complete API parameter/return types, or test results. Public documentation can resolve many names, but installed Studio libraries and project/asset exports may be needed for a truly exhaustive inventory.
