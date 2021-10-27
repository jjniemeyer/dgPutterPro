"""new fields in user model

Revision ID: 5711c7ea2f96
Revises: 31f178ee4544
Create Date: 2021-10-26 13:09:33.913504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5711c7ea2f96'
down_revision = '31f178ee4544'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('current_goal', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'current_goal')
    # ### end Alembic commands ###