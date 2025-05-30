"""Add full_name column to users

Revision ID: fdb545b30f9b
Revises: 3471d03ffdd9
Create Date: 2025-05-29 20:26:19.711639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdb545b30f9b'
down_revision: Union[str, None] = '3471d03ffdd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
