"""create store

Revision ID: 617c2f85b220
Revises: 0646af579311
Create Date: 2023-06-08 14:31:11.498677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '617c2f85b220'
down_revision = '0646af579311'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE store(
            id SERIAL PRIMARY KEY,
            genre TEXT NOT NULL,
            game_id INT
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE store;
        """
    )

