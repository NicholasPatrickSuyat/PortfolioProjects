"""create foreign keys users_store

Revision ID: 4a0de3f2558f
Revises: f1163afc0bda
Create Date: 2023-06-08 15:48:56.235831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a0de3f2558f'
down_revision = 'f1163afc0bda'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE users
        ADD CONSTRAINT fk_users_store
        FOREIGN KEY (store_id)
        REFERENCES store(id);
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE users
        DROP CONSTRAINT fk_users_store;
        """
    )