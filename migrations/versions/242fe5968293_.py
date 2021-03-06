"""empty message

Revision ID: 242fe5968293
Revises: dedd2b0fe12f
Create Date: 2021-12-20 10:29:16.512159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '242fe5968293'
down_revision = 'dedd2b0fe12f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
