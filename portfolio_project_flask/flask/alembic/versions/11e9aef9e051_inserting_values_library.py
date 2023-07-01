"""inserting values library

Revision ID: 11e9aef9e051
Revises: 243b2de0541f
Create Date: 2023-06-08 16:12:44.673769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11e9aef9e051'
down_revision = '243b2de0541f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO library(id, genre, game_id)
        VALUES (1,'MOBA',1), (2,'FPS',2), (3,'RPG',3);
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM library;
        """
    )
