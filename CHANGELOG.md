## Changelog

### v0.3.0

- Updated Python dependencies.
- Refactored and cleaned-up Ansible role adding the ability to provide the service user with access to the PostgreSQL schemata created for local-testing in addition to installing the necessary extensions.
- Updated `.gitignore.`.
- Updated the Alembic `env.py` to use the new configuration file.
- Updated the initial revision script and removed the creation/deletion of schemata as those will be created by the Ansible provisioner.
- Added a new revision to add the canonicalised facilities tables and foreign-keys as well as indices for the city/state/country in the `facilities` table.


### v0.2.0

Issue No.33: Remove the `concept_synonyms` table:
- Added revision to remove the `concept_synonyms` table.

Issue No. 35: Add `pg_tgrm` index to synonym columns:
- Added revision to create the `pg_trgm` indices on the synonym tables.

### v0.1.1

- Added new revision to add the supplemental-synonyms table.

### v0.1.0

- Initial release.
