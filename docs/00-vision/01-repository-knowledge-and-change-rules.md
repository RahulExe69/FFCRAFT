# Repository knowledge and change workflow

This document explains how knowledge should be captured and reused across FFCRAFT projects.

The binding repository-wide rules are in [AGENTS.md](../../AGENTS.md). This file provides the human-readable workflow and folder guidance.

## Working loop

1. **Orient:** read `AGENTS.md`, the root README, the relevant project README, existing decisions, and recent audits.
2. **Inventory:** identify relevant assets and formats before interpreting them.
3. **Inspect:** trace readable code or decode serialized project data. Follow references and dependencies, not just strings or screenshots.
4. **Record:** separate confirmed facts, direct observations, inferences, and unknowns.
5. **Propose:** describe the evidence, likely cause, suggested change, risks, and test plan.
6. **Change safely:** preserve originals; use a separate copy/branch for experiments.
7. **Validate:** test the change where possible and record the exact result. If it cannot be tested, say so.
8. **Carry forward:** update the project docs and link the commit so future sessions can continue without redoing discovery.

## Suggested per-project structure

```text
projects/
  templates/
    Map1/                 # pristine imported source/export; don't experiment here
      README.md
      <original export files>
  maps/
    <map-name>/
      README.md
      docs/
        vision.md
        source-inventory.md
        architecture.md
        logic-audit.md
        decisions.md
        issues-and-improvements.md
        testing.md
      assets/             # only if useful; keep exports/raw data distinct
```

Not every project needs every document. Start with a concise README and source inventory, then split documentation when it improves navigation. Avoid copying large binary source files into explanatory documents.

## Evidence labels

- **Confirmed** — source/format decoded, behaviour reproduced, or authoritative documentation directly supports it.
- **Observed** — directly visible in a screenshot, file, log, or user report.
- **Inferred** — a reasoned but unverified explanation.
- **Unknown** — not enough evidence yet.

Each audit should state which files and revision it covers. Where feasible, include file sizes and SHA-256 hashes so later changes can be detected.

## Project documentation responsibilities

- Vision documents preserve the creator's goals and deliberate choices.
- Inventories describe files and formats, not guessed semantics.
- Architecture documents explain how systems relate.
- Logic audits trace events, block graphs, data/state transitions, and failure paths.
- Decisions record agreed choices and trade-offs.
- Issues documents distinguish symptoms from root causes and list the next verification step.
- Testing documents contain reproducible scenarios and results actually obtained.

## Important boundary

Documentation is the durable memory for the repository, but it is not proof that a proprietary export has been decoded. If a format remains opaque, record the decoding limitation and do not invent block-by-block behaviour.
