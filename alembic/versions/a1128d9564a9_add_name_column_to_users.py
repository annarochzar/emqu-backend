"""Add name column to users

Revision ID: a1128d9564a9
Revises: fdb545b30f9b
Create Date: 2025-05-29 20:56:12.558531
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# Identificadores de revisión
revision: str = 'a1128d9564a9'
down_revision: Union[str, None] = 'fdb545b30f9b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crear ENUM
    user_role_enum = sa.Enum('author', 'moderator', name='userroleenum')
    user_role_enum.create(op.get_bind(), checkfirst=True)

    # Agregar columna 'name'
    op.add_column('users', sa.Column('name', sa.String(), nullable=False))

    # Cambiar columna 'role' a ENUM, especificando cómo hacer el cast
    op.alter_column('users', 'role',
        existing_type=sa.VARCHAR(),
        type_=user_role_enum,
        postgresql_using="role::userroleenum",
        nullable=False)

    # Eliminar columna 'fullname'
    op.drop_column('users', 'fullname')


def downgrade() -> None:
    # Volver a agregar 'fullname'
    op.add_column('users', sa.Column('fullname', sa.VARCHAR(), nullable=False))

    # Revertir ENUM a VARCHAR
    op.alter_column('users', 'role',
        existing_type=sa.Enum('author', 'moderator', name='userroleenum'),
        type_=sa.VARCHAR(),
        nullable=True)

    # Eliminar columna 'name'
    op.drop_column('users', 'name')

    # Eliminar ENUM
    user_role_enum = sa.Enum('author', 'moderator', name='userroleenum')
    user_role_enum.drop(op.get_bind(), checkfirst=True)
