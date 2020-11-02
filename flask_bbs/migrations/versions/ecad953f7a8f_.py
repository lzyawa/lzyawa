"""empty message

Revision ID: ecad953f7a8f
Revises: 7959cb143803
Create Date: 2018-12-24 09:51:29.378000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecad953f7a8f'
down_revision = '7959cb143803'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_star_user', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_star_user')
    # ### end Alembic commands ###
