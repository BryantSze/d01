"""empty message

Revision ID: 8c049157418a
Revises: 840be43245ef
Create Date: 2023-04-25 13:31:32.724140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c049157418a'
down_revision = '840be43245ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_constraint('booking_cinema_id_fkey', type_='foreignkey')
        batch_op.drop_column('cinema_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cinema_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('booking_cinema_id_fkey', 'cinema', ['cinema_id'], ['id'])

    # ### end Alembic commands ###