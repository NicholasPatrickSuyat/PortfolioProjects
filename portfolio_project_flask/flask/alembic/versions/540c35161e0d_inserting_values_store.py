"""inserting values store

Revision ID: 540c35161e0d
Revises: 11e9aef9e051
Create Date: 2023-06-08 16:15:54.680824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '540c35161e0d'
down_revision = '11e9aef9e051'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO store(id, genre, game_id)
        VALUES (1,'MOBA', 1), (2,'FPS', 2), (3,'RPG', 3);
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM store;
        """
    )
