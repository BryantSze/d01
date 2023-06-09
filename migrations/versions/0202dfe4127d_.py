"""empty message

Revision ID: 0202dfe4127d
Revises: 56f0509b3aec
Create Date: 2023-04-25 13:27:54.217473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0202dfe4127d'
down_revision = '56f0509b3aec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_constraint('booking_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('booking_user_id_fkey', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###
