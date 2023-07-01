"""create games

Revision ID: ad82f95639b3
Revises: 617c2f85b220
Create Date: 2023-06-08 14:44:52.425215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad82f95639b3'
down_revision = '617c2f85b220'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE games(
            id SERIAL PRIMARY KEY,
            game_title TEXT NOT NULL,
            genre TEXT NOT NULL,
            developer_name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE games;
        """
    )
