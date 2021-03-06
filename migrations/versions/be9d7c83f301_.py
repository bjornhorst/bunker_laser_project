"""empty message

Revision ID: be9d7c83f301
Revises: 2f50eee237ef
Create Date: 2021-11-29 11:34:05.986602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be9d7c83f301'
down_revision = '2f50eee237ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('data1', sa.String(length=120), nullable=True))
    op.add_column('video', sa.Column('videoPunten1', sa.String(length=500), server_default='[{"time":0,"laserOnOff":"begin"}]', nullable=True))
    op.drop_index('ix_video_videoPunten', table_name='video')
    op.create_index(op.f('ix_video_data1'), 'video', ['data1'], unique=False)
    op.create_index(op.f('ix_video_videoPunten1'), 'video', ['videoPunten1'], unique=False)
    op.drop_column('video', 'videoPunten')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('videoPunten', sa.VARCHAR(length=500), server_default='[{"time":0,"laserOnOff":"begin"}]', nullable=True))
    op.drop_index(op.f('ix_video_videoPunten1'), table_name='video')
    op.drop_index(op.f('ix_video_data1'), table_name='video')
    op.create_index('ix_video_videoPunten', 'video', ['videoPunten'], unique=False)
    op.drop_column('video', 'videoPunten1')
    op.drop_column('video', 'data1')
    # ### end Alembic commands ###
