"""Second  Migration

Revision ID: 0e72d126f4db
Revises: 1536cd2b3f39
Create Date: 2018-09-14 13:54:51.284424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e72d126f4db'
down_revision = '1536cd2b3f39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('blogpost_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogposts', 'users', ['blogpost_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogposts', type_='foreignkey')
    op.drop_column('blogposts', 'blogpost_id')
    # ### end Alembic commands ###
