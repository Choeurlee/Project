"""empty message

Revision ID: bc9299911eea
Revises: d8014fe1e711
Create Date: 2020-03-10 15:47:40.748056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bc9299911eea'
down_revision = 'd8014fe1e711'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('question', sa.String(length=160), nullable=True))
    op.drop_column('questions', 'questions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('questions', mysql.VARCHAR(length=160), nullable=True))
    op.drop_column('questions', 'question')
    # ### end Alembic commands ###
