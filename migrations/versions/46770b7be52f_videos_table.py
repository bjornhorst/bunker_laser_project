"""videos table

Revision ID: 46770b7be52f
Revises: d05223f641e6
Create Date: 2021-10-13 13:54:55.903829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46770b7be52f'
down_revision = 'd05223f641e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('cords', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_video_putne'), 'video', ['cords'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_video_putne'), table_name='video')
    op.drop_column('video', 'putne')
    # ### end Alembic commands ###
