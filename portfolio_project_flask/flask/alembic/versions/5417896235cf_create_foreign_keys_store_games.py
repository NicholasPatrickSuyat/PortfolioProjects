"""create foreign keys store_games

Revision ID: 5417896235cf
Revises: 4a0de3f2558f
Create Date: 2023-06-08 15:51:46.079699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5417896235cf'
down_revision = '4a0de3f2558f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE store
        ADD CONSTRAINT fk_store_games
        FOREIGN KEY (game_id)
        REFERENCES games(id);
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE store
        DROP CONSTRAINT fk_store_games;
        """
    )