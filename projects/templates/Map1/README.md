# Map1 — Pristine Craftland Template

This directory is reserved for the extracted files from the user-provided `Map1.zip`, copied from Free Fire MAX's Android workshop data.

## Role in the repository

The FFCRAFT repository is the source of truth for research, decisions, project documentation, and our created maps. This directory holds a **reference-only original export** that we may use to create separate working copies. It is not the place to build or experiment on a new map.

Map-specific documentation lives in [docs/](docs/README.md). When creating a map, copy the needed source into a separate folder under `projects/maps/<map-name>/` and document the relationship to this template.

## Status

- [x] Original extracted files added by Rahul
- [ ] File inventory and hashes recorded
- [ ] Serialization and file relationships documented
- [ ] Template restoration/import workflow verified

## Safety rules

- Treat this as the golden reference; do not modify its original files during experiments.
- Make a separate copy under `projects/maps/<map-name>/` for each experiment or new map.
- Do not assume that changing these files and copying them back into Android app data is safe or supported until tested.
- Keep any account-specific identifiers private when sharing the repository publicly.

## Expected files

Upload the extracted files from the original workshop folder here, preserving their original filenames. Do not upload the ZIP archive.
