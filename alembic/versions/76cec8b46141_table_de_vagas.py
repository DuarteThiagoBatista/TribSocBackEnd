"""table de vagas

Revision ID: 76cec8b46141
Revises: e15ea59317b8
Create Date: 2022-05-25 21:19:12.575760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76cec8b46141'
down_revision = 'e15ea59317b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vagas',
    sa.Column('tipo', sa.String(), nullable=True),
    sa.Column('modelo', sa.String(), nullable=True),
    sa.Column('descricao', sa.String(), nullable=True),
    sa.Column('periodo', sa.String(), nullable=True),
    sa.Column('requisito', sa.String(), nullable=True),
    sa.Column('tipo_contratacao', sa.String(), nullable=True),
    sa.Column('beneficios', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_empresa', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_empresa'], ['empresas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vagas_id'), 'vagas', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vagas_id'), table_name='vagas')
    op.drop_table('vagas')
    # ### end Alembic commands ###
