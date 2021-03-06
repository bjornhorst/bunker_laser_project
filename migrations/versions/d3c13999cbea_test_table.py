"""test table

Revision ID: d3c13999cbea
Revises: 498172dc0e3c
Create Date: 2021-10-25 15:26:59.978982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3c13999cbea'
down_revision = '498172dc0e3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('dijk', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_test_dijk'), 'test', ['dijk'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_test_dijk'), table_name='test')
    op.drop_column('test', 'dijk')
    # ### end Alembic commands ###
