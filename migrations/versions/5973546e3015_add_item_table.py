"""add item table

Revision ID: 5973546e3015
Revises: aa6acf467226
Create Date: 2021-04-02 11:33:00.393748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5973546e3015'
down_revision = 'aa6acf467226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('list_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###
