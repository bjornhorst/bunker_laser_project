"""empty message

Revision ID: 92ed3d2fc75c
Revises: 88290f47550f
Create Date: 2021-11-08 12:44:25.068633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92ed3d2fc75c'
down_revision = '88290f47550f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('videoPunten1', sa.String(length=500), nullable=True))
    op.drop_index('ix_video_videoPunten', table_name='video')
    op.create_index(op.f('ix_video_videoPunten1'), 'video', ['videoPunten1'], unique=False)
    op.drop_column('video', 'videoPunten')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('videoPunten', sa.VARCHAR(length=500), nullable=True))
    op.drop_index(op.f('ix_video_videoPunten1'), table_name='video')
    op.create_index('ix_video_videoPunten', 'video', ['videoPunten'], unique=False)
    op.drop_column('video', 'videoPunten1')
    # ### end Alembic commands ###