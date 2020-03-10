"""empty message

Revision ID: d8014fe1e711
Revises: a2da868ef160
Create Date: 2020-03-10 15:44:27.515637

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd8014fe1e711'
down_revision = 'a2da868ef160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quizes', sa.Column('name', sa.String(length=50), nullable=True))
    op.drop_column('quizes', 'Quiz')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quizes', sa.Column('Quiz', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('quizes', 'name')
    # ### end Alembic commands ###
