"""added pg_trgm indices

Revision ID: a2d973c2a9ab
Revises: 8da8e1d86fc7
Create Date: 2018-06-13 08:31:56.743396

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a2d973c2a9ab'
down_revision = '8da8e1d86fc7'
branch_labels = None
depends_on = None


def upgrade():

    # Create `pg_trgm` index on the `synonym` field of the
    # `descriptor_synonyms` table.
    op.create_index(
        op.f('ix_mesh_descriptor_synonyms_synonym_trgm'),
        'descriptor_synonyms',
        [sa.text('synonym gin_trgm_ops')],
        schema='mesh',
        postgresql_using='gin',
        postgresql_ops={"description": "gin_trgm_ops"},
    )

    # Create `pg_trgm` index on the `synonym` field of the
    # `qualifier_synonyms` table.
    op.create_index(
        op.f('ix_mesh_qualifier_synonyms_synonym_trgm'),
        'qualifier_synonyms',
        [sa.text('synonym gin_trgm_ops')],
        schema='mesh',
        postgresql_using='gin',
        postgresql_ops={"description": "gin_trgm_ops"},
    )

    # Create `pg_trgm` index on the `synonym` field of the
    # `supplemental_synonyms` table.
    op.create_index(
        op.f('ix_mesh_supplemental_synonyms_synonym_trgm'),
        'supplemental_synonyms',
        [sa.text('synonym gin_trgm_ops')],
        schema='mesh',
        postgresql_using='gin',
        postgresql_ops={"description": "gin_trgm_ops"},
    )


def downgrade():

    # Drop `ix_mesh_descriptor_synonyms_synonym_trgm` index.
    op.drop_index(
        'ix_mesh_descriptor_synonyms_synonym_trgm',
        table_name='descriptor_synonyms',
        schema='mesh',
    )

    # Drop `ix_mesh_qualifier_synonyms_synonym_trgm` index.
    op.drop_index(
        'ix_mesh_qualifier_synonyms_synonym_trgm',
        table_name='qualifier_synonyms',
        schema='mesh',
    )

    # Drop `ix_mesh_supplemental_synonyms_synonym_trgm` index.
    op.drop_index(
        'ix_mesh_supplemental_synonyms_synonym_trgm',
        table_name='supplemental_synonyms',
        schema='mesh',
    )
