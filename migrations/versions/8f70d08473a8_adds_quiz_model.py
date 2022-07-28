"""adds Quiz model

Revision ID: 8f70d08473a8
Revises: 
Create Date: 2022-07-27 21:43:28.176939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f70d08473a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz',
    sa.Column('question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('correct_answer', sa.String(), nullable=True),
    sa.Column('incorrect_answer1', sa.String(), nullable=True),
    sa.Column('incorrect_answer2', sa.String(), nullable=True),
    sa.Column('incorrect_answer3', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('question_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz')
    # ### end Alembic commands ###
