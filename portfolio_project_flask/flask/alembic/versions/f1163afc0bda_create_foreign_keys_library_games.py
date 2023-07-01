"""create foreign keys library_games

Revision ID: f1163afc0bda
Revises: 952836572e05
Create Date: 2023-06-08 15:46:49.476599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1163afc0bda'
down_revision = '952836572e05'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE library
        ADD CONSTRAINT fk_library_games
        FOREIGN KEY (game_id)
        REFERENCES games(id);
        """
    )



def downgrade():
    op.execute(
        """
        ALTER TABLE library
        DROP CONSTRAINT fk_library_games;
        """
    )
