"""empty message

Revision ID: 3a619afb5b27
Revises: e7962b48a63b
Create Date: 2023-04-26 18:01:09.133762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a619afb5b27'
down_revision = 'e7962b48a63b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=True))
        batch_op.create_index(batch_op.f('ix_booking_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_booking_email'))
        batch_op.drop_column('email')

    # ### end Alembic commands ###
