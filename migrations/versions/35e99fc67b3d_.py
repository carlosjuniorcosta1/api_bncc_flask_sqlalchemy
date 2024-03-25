"""empty message

Revision ID: 35e99fc67b3d
Revises: b96749b99866
Create Date: 2024-03-24 16:55:43.996200

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '35e99fc67b3d'
down_revision = 'b96749b99866'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('score', sa.Float(), nullable=True))
        batch_op.alter_column('act_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('student_id',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scores', schema=None) as batch_op:
        batch_op.alter_column('student_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('act_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.drop_column('score')

    # ### end Alembic commands ###
