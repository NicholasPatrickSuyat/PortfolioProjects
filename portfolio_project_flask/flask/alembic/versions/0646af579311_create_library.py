"""create library

Revision ID: 0646af579311
Revises: 2818b0034053
Create Date: 2023-06-08 14:24:17.933616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0646af579311'
down_revision = '2818b0034053'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE library(
            id SERIAL PRIMARY KEY,
            genre TEXT NOT NULL,
            game_id INT
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE library;
        """
    )
