"""inserting users part 2

Revision ID: 4d554132a138
Revises: 540c35161e0d
Create Date: 2023-06-09 21:01:44.031212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d554132a138'
down_revision = '540c35161e0d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        UPDATE users
        SET library_id = 1, store_id = 1
        WHERE id = 1;
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM users
        """
    )
