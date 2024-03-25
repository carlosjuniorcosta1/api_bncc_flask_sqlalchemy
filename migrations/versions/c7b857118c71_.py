"""empty message

Revision ID: c7b857118c71
Revises: 079dd262cab6
Create Date: 2024-03-21 17:46:25.604166

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c7b857118c71'
down_revision = '079dd262cab6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activities_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_act', sa.Float(), nullable=True))
        batch_op.drop_column('total_atv')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activities_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_atv', mysql.FLOAT(), nullable=True))
        batch_op.drop_column('total_act')

    # ### end Alembic commands ###
