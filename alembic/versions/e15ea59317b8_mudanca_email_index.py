"""mudanca email index

Revision ID: e15ea59317b8
Revises: 782129f1830e
Create Date: 2022-05-22 22:06:36.420896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e15ea59317b8'
down_revision = '782129f1830e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('empresas_email_key', 'empresas', type_='unique')
    op.create_index(op.f('ix_empresas_email'), 'empresas', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_empresas_email'), table_name='empresas')
    op.create_unique_constraint('empresas_email_key', 'empresas', ['email'])
    # ### end Alembic commands ###
