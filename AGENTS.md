# Repository collaboration rules for AI-assisted work

These rules apply to **every project and map in this repository**, not only ColourBridge.

## Source-of-truth rule

The Git repository is the durable source of truth for this work. At the start of a task, read the relevant project docs, current decisions, source inventory, and previous audit. At the end of substantial work, commit the new findings and link the commit. Do not rely on chat history alone when project facts can be captured in the repo. Keep reusable knowledge under `docs/` and `research/`; keep pristine template exports under `projects/templates/`; keep authored maps and their working copies under `projects/maps/`. The original template folder is reference-only.

## 1. Learn before changing

- Inspect the relevant project files, existing documentation, prior decisions, and repository structure before proposing or making changes.
- Reuse existing work and conventions; do not make the user repeat information already documented here.
- Treat the repository as the durable project memory. Important discoveries, user intent, constraints, and decisions belong in version-controlled documentation.
- For follow-up work, read the relevant project overview and its latest audit/decision notes first.

## 2. Separate evidence from interpretation

Every technical claim must be categorized appropriately:
- **Confirmed:** directly supported by readable source, decoded project data, reproducible behaviour, or an authoritative reference.
- **Observed:** directly visible in supplied screenshots or other artifacts, without assuming the cause.
- **Inferred:** a plausible explanation based on evidence, but not verified.
- **Unknown / needs validation:** evidence is missing or ambiguous.

Never present a variable name, screenshot, extracted string, or plausible interpretation as proof of full program behaviour. State what was actually inspected and what remains unread.

## 3. Inspect source thoroughly

- For readable code, inspect the relevant implementation line by line, trace callers/callees, data flow, event order, state changes, and error paths before making a diagnosis.
- For binary, generated, serialized, or proprietary project formats, first identify the format and decoding method. Map IDs, parameters, nodes, references, and connections before claiming line-by-line understanding.
- If full decoding is not currently possible, document the limitation and provide the most complete evidence-based partial analysis. Do not fake a source-level audit.
- Use official/current documentation for platform-specific APIs and confirm version/platform restrictions where relevant.

## 4. Preserve the user's intent and originals

- Treat explicitly stated user goals and authored content as intentional unless the user requests a change.
- Do not label a deliberate feature as a bug simply because it looks unusual.
- Keep original imports/exports and golden templates unchanged. Perform experiments in a separate copy, branch, or clearly named project folder.
- Never overwrite, delete, or mutate user assets merely to make an experiment convenient.
- Avoid editing binary project data manually unless the format and write process are understood and safely validated.

## 5. Change discipline

Before implementation, document:
1. The problem and evidence.
2. Root cause or the confidence level if root cause is still uncertain.
3. Proposed change and why it should work.
4. Files/assets affected and possible regressions.
5. A validation/test plan.

After implementation, record what changed, commit/PR reference, tests actually run, outcomes, and any remaining risks. Never claim a test passed if it was not run.

## 6. Keep project knowledge structured

- Put repository-wide workflow, conventions, and collaboration rules here.
- Put reusable technical knowledge in topic-specific folders under `docs/`.
- Put project-specific intent, architecture, data inventories, audits, and decisions alongside the project under `projects/<project>/docs/` or an equivalent documented structure.
- Keep raw uploads/source exports separate from human-authored documentation.
- Add or update an index/README when introducing a meaningful new folder or document.
- Use descriptive, stable filenames; prefer small documents with one clear purpose over a single enormous notes file.
- Record provenance: source file/path, revision or hash where practical, date/context when relevant, and confidence/status.

## 7. Map/project knowledge standard

For every map or project, aim to maintain:
- `README.md`: purpose, status, how to navigate the project.
- `docs/vision.md`: creator intent and non-goals.
- `docs/source-inventory.md`: files, formats, roles, hashes/sizes where useful.
- `docs/architecture.md`: systems and relationships.
- `docs/logic-audit.md`: scripts/blocks, events, inputs, outputs, state transitions, dependencies, and confidence.
- `docs/decisions.md`: agreed choices and rationale.
- `docs/issues-and-improvements.md`: observed issue, evidence, hypothesis, next test, and proposed fix.
- `docs/testing.md`: reproducible test cases and actual results.

Create only the files relevant to the project; mark unknown sections as unknown rather than filling them with guesses.

## 8. End-of-task update

For any substantial task:
- Update the relevant documentation with what was learned, changed, tested, and left unresolved.
- Keep the root README or relevant folder README navigable.
- Summarize the key outcome and link the changed files/commit to the user.
- Do not claim durable memory unless the information was actually committed to the repository or otherwise saved through a supported mechanism.
