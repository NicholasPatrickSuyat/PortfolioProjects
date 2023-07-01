"""create users

Revision ID: 2818b0034053
Revises: 
Create Date: 2023-06-08 14:14:21.863695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2818b0034053'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE users(
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            library_id INT,
            store_id INT

        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE users;
        """
    )
