"""Third  Migration

Revision ID: 3ab7ccf78df7
Revises: 0e72d126f4db
Create Date: 2018-09-14 14:08:41.528559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ab7ccf78df7'
down_revision = '0e72d126f4db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('author_id', sa.Integer(), nullable=True))
    op.drop_constraint('blogposts_blogpost_id_fkey', 'blogposts', type_='foreignkey')
    op.create_foreign_key(None, 'blogposts', 'users', ['author_id'], ['id'])
    op.drop_column('blogposts', 'blogpost_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('blogpost_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blogposts', type_='foreignkey')
    op.create_foreign_key('blogposts_blogpost_id_fkey', 'blogposts', 'users', ['blogpost_id'], ['id'])
    op.drop_column('blogposts', 'author_id')
    # ### end Alembic commands ###
