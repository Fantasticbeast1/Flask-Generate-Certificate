"""empty message

Revision ID: 24161eac56c6
Revises: 31e3e4a7ed93
Create Date: 2021-05-16 19:51:52.877905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24161eac56c6'
down_revision = '31e3e4a7ed93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_key',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=50), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('usage_limit', sa.Integer(), nullable=True),
    sa.Column('is_valid', sa.Boolean(), nullable=False),
    sa.Column('is_approved', sa.Boolean(), nullable=False),
    sa.Column('date_generated', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_key')
    # ### end Alembic commands ###
