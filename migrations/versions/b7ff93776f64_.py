"""empty message

Revision ID: b7ff93776f64
Revises: 1a742eba48eb
Create Date: 2022-08-01 01:45:03.192824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7ff93776f64'
down_revision = '1a742eba48eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'date')
    # ### end Alembic commands ###