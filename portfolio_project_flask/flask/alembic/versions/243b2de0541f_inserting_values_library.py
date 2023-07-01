"""inserting values games

Revision ID: 243b2de0541f
Revises: cc038e879ecf
Create Date: 2023-06-08 16:06:55.543828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '243b2de0541f'
down_revision = 'cc038e879ecf'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO games(id, game_title, genre, developer_name)
        VALUES (1,'Dota 2', 'MOBA', 'Valve'), (2,'CSGO', 'FPS', 'Valve'), (3,'Elden Ring', 'RPG', 'Fromsoft');
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM games;
        """
    )
