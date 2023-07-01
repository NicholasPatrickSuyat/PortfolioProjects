"""create foreign keys users_library

Revision ID: 952836572e05
Revises: ad82f95639b3
Create Date: 2023-06-08 14:47:39.259509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '952836572e05'
down_revision = 'ad82f95639b3'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE users
        ADD CONSTRAINT fk_users_library
        FOREIGN KEY (library_id)
        REFERENCES library(id);
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE users
        DROP CONSTRAINT fk_users_library;
        """
    )
        
