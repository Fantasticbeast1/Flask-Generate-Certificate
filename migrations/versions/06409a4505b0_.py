"""empty message

Revision ID: 06409a4505b0
Revises: 7806c64d4f43
Create Date: 2021-06-03 15:17:07.600196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06409a4505b0'
down_revision = '7806c64d4f43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group', schema=None) as batch_op:
        batch_op.add_column(sa.Column('textColor', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group', schema=None) as batch_op:
        batch_op.drop_column('textColor')

    # ### end Alembic commands ###