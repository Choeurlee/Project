"""empty message

Revision ID: a2da868ef160
Revises: 6e3de45eb801
Create Date: 2020-03-10 14:11:03.168196

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a2da868ef160'
down_revision = '6e3de45eb801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Quiz', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'Quiz')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.Column('questions', sa.String(length=160), nullable=True),
    sa.Column('a', sa.String(length=120), nullable=True),
    sa.Column('b', sa.String(length=120), nullable=True),
    sa.Column('c', sa.String(length=120), nullable=True),
    sa.Column('d', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quizes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('questions')
    op.drop_table('users')
    op.drop_table('quizes')
    # ### end Alembic commands ###