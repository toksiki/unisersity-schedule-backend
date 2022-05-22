"""ondelete=cascade

Revision ID: b04a73b00266
Revises: afc6a666c4e4
Create Date: 2022-05-22 01:05:26.675873

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b04a73b00266'
down_revision = 'afc6a666c4e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('course_teacher_course_id_fkey', 'course_teacher', type_='foreignkey')
    op.drop_constraint('course_teacher_teacher_id_fkey', 'course_teacher', type_='foreignkey')
    op.create_foreign_key(None, 'course_teacher', 'teacher', ['teacher_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'course_teacher', 'course', ['course_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('schedule_item_course_id_fkey', 'schedule_item', type_='foreignkey')
    op.drop_constraint('schedule_item_type_schedule_item_id_fkey', 'schedule_item', type_='foreignkey')
    op.drop_constraint('schedule_item_bell_id_fkey', 'schedule_item', type_='foreignkey')
    op.drop_constraint('schedule_item_subgroup_id_fkey', 'schedule_item', type_='foreignkey')
    op.drop_constraint('schedule_item_group_id_fkey', 'schedule_item', type_='foreignkey')
    op.drop_constraint('schedule_item_week_id_fkey', 'schedule_item', type_='foreignkey')
    op.drop_constraint('schedule_item_classroom_id_fkey', 'schedule_item', type_='foreignkey')
    op.drop_constraint('schedule_item_teacher_id_fkey', 'schedule_item', type_='foreignkey')
    op.create_foreign_key(None, 'schedule_item', 'bell', ['bell_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'schedule_item', 'course', ['course_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'schedule_item', 'week', ['week_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'schedule_item', 'subgroup', ['subgroup_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'schedule_item', 'classroom', ['classroom_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'schedule_item', 'type_schedule_item', ['type_schedule_item_id'], ['id'],
                          ondelete='CASCADE')
    op.create_foreign_key(None, 'schedule_item', 'group', ['group_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'schedule_item', 'teacher', ['teacher_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('subgroup_group_id_fkey', 'subgroup', type_='foreignkey')
    op.create_foreign_key(None, 'subgroup', 'group', ['group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('teacher_wish_teacher_id_fkey', 'teacher_wish', type_='foreignkey')
    op.drop_constraint('teacher_wish_bell_id_fkey', 'teacher_wish', type_='foreignkey')
    op.drop_constraint('teacher_wish_week_id_fkey', 'teacher_wish', type_='foreignkey')
    op.create_foreign_key(None, 'teacher_wish', 'week', ['week_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'teacher_wish', 'teacher', ['teacher_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'teacher_wish', 'bell', ['bell_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher_wish', type_='foreignkey')
    op.drop_constraint(None, 'teacher_wish', type_='foreignkey')
    op.drop_constraint(None, 'teacher_wish', type_='foreignkey')
    op.create_foreign_key('teacher_wish_week_id_fkey', 'teacher_wish', 'week', ['week_id'], ['id'])
    op.create_foreign_key('teacher_wish_bell_id_fkey', 'teacher_wish', 'bell', ['bell_id'], ['id'])
    op.create_foreign_key('teacher_wish_teacher_id_fkey', 'teacher_wish', 'teacher', ['teacher_id'], ['id'])
    op.drop_constraint(None, 'subgroup', type_='foreignkey')
    op.create_foreign_key('subgroup_group_id_fkey', 'subgroup', 'group', ['group_id'], ['id'])
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.drop_constraint(None, 'schedule_item', type_='foreignkey')
    op.create_foreign_key('schedule_item_teacher_id_fkey', 'schedule_item', 'teacher', ['teacher_id'], ['id'])
    op.create_foreign_key('schedule_item_classroom_id_fkey', 'schedule_item', 'classroom', ['classroom_id'], ['id'])
    op.create_foreign_key('schedule_item_week_id_fkey', 'schedule_item', 'week', ['week_id'], ['id'])
    op.create_foreign_key('schedule_item_group_id_fkey', 'schedule_item', 'group', ['group_id'], ['id'])
    op.create_foreign_key('schedule_item_subgroup_id_fkey', 'schedule_item', 'subgroup', ['subgroup_id'], ['id'])
    op.create_foreign_key('schedule_item_bell_id_fkey', 'schedule_item', 'bell', ['bell_id'], ['id'])
    op.create_foreign_key('schedule_item_type_schedule_item_id_fkey', 'schedule_item', 'type_schedule_item',
                          ['type_schedule_item_id'], ['id'])
    op.create_foreign_key('schedule_item_course_id_fkey', 'schedule_item', 'course', ['course_id'], ['id'])
    op.drop_constraint(None, 'course_teacher', type_='foreignkey')
    op.drop_constraint(None, 'course_teacher', type_='foreignkey')
    op.create_foreign_key('course_teacher_teacher_id_fkey', 'course_teacher', 'teacher', ['teacher_id'], ['id'])
    op.create_foreign_key('course_teacher_course_id_fkey', 'course_teacher', 'course', ['course_id'], ['id'])
    # ### end Alembic commands ###
