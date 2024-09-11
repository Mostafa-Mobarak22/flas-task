"""create book table

Revision ID: 7951b618a1bd
Revises: 
Create Date: 2024-09-09 19:13:59.221466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7951b618a1bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('image', sa.String(length=250), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
