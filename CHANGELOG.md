## Changelog

### v0.13.0

- Story No. 1101: Switch `fightfor-alembic` Git deployment to GitLab.com.
- Story No. 1703: Add MedlinePlus schema migrations and privileges.

### v0.12.0

- Story CH1062: Update to Python 3.7.

### v0.11.0

Issue No.294: duplicate key value violates unique constraint "ix_mesh_supplementals_name":

- Added ffgraphql user to DB.
- Added new revision to add UNIQUE constraints.

### v0.10.0

Issue No. 201:

- Updated the Ansible role to set the PostgreSQL privileges for the different service-users.

Issue No. 202:

- Added new revision that removes the MeSH tables from the `pubmed` schema, i.e., the `descriptors`, `qualifiers`, and `chemicals` tables, and instead uses new FKs to the corresponding tables under the `mesh` schema.

### v0.9.0

- Released without merging the feature branch.

### v0.8.0

- Removed all existing revisions.
- Added a new revision file to replace all previous revisions and represent the latest state of the schema.
- Updated some PostgreSQL-related tasks not to only run in the Vagrant VM but the production server as well.

### v0.7.1

- Added a new revision to add the MD5 field to the MeSH descriptors defnitions table and include it in the unique constraint.

### v0.7.0

Issue No. 188: Design table to hold definitions for the different MeSH descriptors:

- Added revision to create the MeSH descriptor definition table.

### v0.6.0

Issue No. 166: Add tables for studies and citations saved by the user:

- Added new revision to create the user studies and citations tables.

### v0.5.0

Issue No. 156: Model a user-data schema:

- Updated Ansible to create the `app` schema in PostgreSQL.
- Added a new revision to create the new tables under the `app` schema.

### v0.4.2

- Added migration to add new indices.

### v0.4.1

- Added a new revision to change all `clinicaltrials.facilities_canonical` columns except `google_place_id` to nullable.

### v0.4.0

- Fixed bugs in Ansible role.
- Added a new revision to add new indices on columns used in clinical-trials study-filtering.

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
