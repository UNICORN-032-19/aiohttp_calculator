import sqlalchemy as sa
from aiohttp_calculator.migrations import metadata


result = sa.Table(
    'result', metadata,
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('string', sa.String(200), nullable=False),
    sa.Column('result', sa.String(200), nullable=False),
    sa.Column('error', sa.String(200), nullable=False),
)
