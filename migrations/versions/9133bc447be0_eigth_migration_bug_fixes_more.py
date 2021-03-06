"""Eigth  Migration bug fixes more

Revision ID: 9133bc447be0
Revises: a9b41dbc7fa4
Create Date: 2018-09-15 20:59:24.650055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9133bc447be0'
down_revision = 'a9b41dbc7fa4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('images')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='images_pkey')
    )
    op.drop_table('photos')
    # ### end Alembic commands ###
