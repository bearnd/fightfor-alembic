"""added mesh descriptor definitions table

Revision ID: 90684829fdc2
Revises: 7e89359a7aad
Create Date: 2018-11-10 09:07:40.347937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90684829fdc2'
down_revision = '7e89359a7aad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('descriptor_definitions',
    sa.Column('descriptor_definition_id', sa.BigInteger(), nullable=False),
    sa.Column('descriptor_id', sa.BigInteger(), nullable=False),
    sa.Column('source', sa.Enum('AIR', 'ALT', 'AOT', 'CCC', 'CHV', 'CSP', 'FMA', 'GO', 'HL7V30', 'HPO', 'ICF', 'ICF_CY', 'JABL', 'LNC', 'MCM', 'MDR', 'MDRCZE', 'MDRDUT', 'MDRFRE', 'MDRGER', 'MDRHUN', 'MDRITA', 'MDRJPN', 'MDRPOR', 'MDRSPA', 'MEDLINEPLUS', 'MSH', 'MSHCZE', 'MSHFRE', 'MSHNOR', 'MSHPOR', 'MSHSCR', 'MSHSPA', 'NANDA_I', 'NCI', 'NCI_BRIDG', 'NCI_BioC', 'NCI_CDISC', 'NCI_CRCH', 'NCI_CTCAE', 'NCI_CTEP_SDC', 'NCI_CareLex', 'NCI_DICOM', 'NCI_FDA', 'NCI_GAIA', 'NCI_KEGG', 'NCI_NCI_GLOSS', 'NCI_NICHD', 'NDFRT', 'NIC', 'NOC', 'NUCCPT', 'OMS', 'PDQ', 'PNDS', 'PSY', 'SCTSPA', 'SNOMEDCT_US', 'SOP', 'SPN', 'UMD', 'UWDA', name='descriptordefinitionsourcetype'), nullable=False),
    sa.Column('definition', sa.UnicodeText(), nullable=False),
    sa.ForeignKeyConstraint(['descriptor_id'], ['mesh.descriptors.descriptor_id'], name=op.f('fk_descriptor_definitions_descriptor_id_descriptors')),
    sa.PrimaryKeyConstraint('descriptor_definition_id', name=op.f('pk_descriptor_definitions')),
    sa.UniqueConstraint('descriptor_id', 'source', name=op.f('uq_descriptor_definitions_descriptor_id')),
    schema='mesh'
    )
    op.create_index(op.f('ix_mesh_descriptor_definitions_descriptor_id'), 'descriptor_definitions', ['descriptor_id'], unique=False, schema='mesh')
    op.create_index(op.f('ix_mesh_descriptor_definitions_source'), 'descriptor_definitions', ['source'], unique=False, schema='mesh')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_mesh_descriptor_definitions_source'), table_name='descriptor_definitions', schema='mesh')
    op.drop_index(op.f('ix_mesh_descriptor_definitions_descriptor_id'), table_name='descriptor_definitions', schema='mesh')
    op.drop_table('descriptor_definitions', schema='mesh')
    # ### end Alembic commands ###
