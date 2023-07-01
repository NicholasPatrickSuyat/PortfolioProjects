"""inserting values users

Revision ID: cc038e879ecf
Revises: 5417896235cf
Create Date: 2023-06-08 16:01:07.403813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc038e879ecf'
down_revision = '5417896235cf'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO users(id, username, password, email)
        VALUES (1,'Xaenon', 'pass12345', 'patrick@gmail.com');
        """
    )

def downgrade():
    op.execute(
        """
        DELETE FROM users
        """
    )
