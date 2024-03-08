"""empty message

Revision ID: 4d5521e9cca8
Revises: 7fd861782681
Create Date: 2024-03-07 20:13:41.653526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d5521e9cca8'
down_revision = '7fd861782681'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tabela_bimestres',
    sa.Column('id_bimestre', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('bimestre', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id_bimestre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tabela_bimestres')
    # ### end Alembic commands ###
