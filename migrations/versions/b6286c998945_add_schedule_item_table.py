"""add schedule_item table

Revision ID: b6286c998945
Revises: a973fc07ac9a
Create Date: 2022-05-14 02:51:55.616763

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b6286c998945'
down_revision = 'a973fc07ac9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher_wish',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('teacher_id', sa.Integer(), nullable=False),
                    sa.Column('bell_id', sa.Integer(), nullable=False),
                    sa.Column('week_id', sa.Integer(), nullable=False),
                    sa.Column('day_of_week', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['bell_id'], ['bell.id'], ),
                    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
                    sa.ForeignKeyConstraint(['week_id'], ['week.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher_wish')
    # ### end Alembic commands ###