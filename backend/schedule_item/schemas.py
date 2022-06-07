from datetime import date

from pydantic import BaseModel

from backend.bell.schemas import BellPydantic
from backend.classroom.schemas import ClassroomPydantic
from backend.course.schemas import CoursePydantic
from backend.group.schemas import GroupPydantic, SubgroupPydantic
from backend.teacher.schemas import TeacherPydantic
from backend.type_schedule_item.schemas import TypeScheduleItemPydantic
from backend.week.schemas import WeekPydantic


class ScheduleItemBasePydantic(BaseModel):
    date: date


class ScheduleItemPydantic(ScheduleItemBasePydantic):
    id: int
    course: CoursePydantic
    teacher: TeacherPydantic
    bell: BellPydantic
    group: GroupPydantic | None
    subgroup: SubgroupPydantic | None
    type_schedule_item: TypeScheduleItemPydantic
    classroom: ClassroomPydantic
    week: WeekPydantic

    class Config:
        orm_mode = True


class ScheduleItemInCreatePydantic(ScheduleItemBasePydantic):
    course_id: int
    teacher_id: int
    bell_id: int
    group_id: int
    subgroup_id: int | None
    type_schedule_item_id: int
    classroom_id: int
    week_id: int


class ScheduleItemInUpdatePydantic(ScheduleItemBasePydantic):
    course_id: int | None
    teacher_id: int | None
    bell_id: int | None
    group_id: int | None
    subgroup_id: int | None
    type_schedule_item_id: int | None
    classroom_id: int | None


class ScheduleItemFilterPydantic(BaseModel):
    classroom_id: int | None
    course_id: int | None
    group_id: int | None
    subgroup_id: int | None
    teacher_id: int | None
    date_beg: date | None
    date_end: date | None
    week_number: int | None
