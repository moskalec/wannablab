"""

Revision ID: 4a4246d6afa2
Revises: 9e9d7947342c
Create Date: 2018-10-27 15:40:34.729523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a4246d6afa2'
down_revision = '9e9d7947342c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'session', ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'session', type_='unique')
    # ### end Alembic commands ###
