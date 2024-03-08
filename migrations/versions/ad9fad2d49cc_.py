"""empty message

Revision ID: ad9fad2d49cc
Revises: 83d2f71551c4
Create Date: 2024-03-07 22:22:15.241392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad9fad2d49cc'
down_revision = '83d2f71551c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tabela_atividades',
    sa.Column('id_atividade', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('data_atividade', sa.Date(), nullable=True),
    sa.Column('descricao_atv', sa.String(length=100), nullable=True),
    sa.Column('valor_atv', sa.Float(), nullable=True),
    sa.Column('status_atv', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_atividade')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tabela_atividades')
    # ### end Alembic commands ###
