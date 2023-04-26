"""empty message

Revision ID: 2da1e34e1eda
Revises: 1f08f3f7f97b
Create Date: 2023-04-26 15:07:40.474990

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2da1e34e1eda'
down_revision = '1f08f3f7f97b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
