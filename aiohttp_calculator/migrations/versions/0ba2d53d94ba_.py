"""empty message

Revision ID: 0ba2d53d94ba
Revises: 235db9ed991c
Create Date: 2020-03-22 09:57:31.489125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba2d53d94ba'
down_revision = '235db9ed991c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('string', sa.String(length=200), nullable=False),
    sa.Column('result', sa.String(length=200), nullable=False),
    sa.Column('error', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_result_id'), 'result', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_result_id'), table_name='result')
    op.drop_table('result')
    # ### end Alembic commands ###
