"""create table posts

Revision ID: 9c1353cb3e64
Revises: 
Create Date: 2023-07-24 18:43:08.360851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c1353cb3e64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'post',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade() -> None:
    op.drop_table('post')

