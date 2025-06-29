"""Add year to RSession model

Revision ID: 7ec723656fb5
Revises: 
Create Date: 2025-06-22 20:33:55.288464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ec723656fb5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result_session', schema=None) as batch_op:
        batch_op.add_column(sa.Column('year', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result_session', schema=None) as batch_op:
        batch_op.drop_column('year')

    # ### end Alembic commands ###
