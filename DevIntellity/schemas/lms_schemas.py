from typing import List, Union

from pydantic import BaseModel


class CourseCategoryBase(BaseModel):
    title: str
    description: Union[str, None] = None

class CourseCategoryCreate(CourseCategoryBase):
    pass


class CourseCategory(CourseCategoryBase):
    id: int

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    category: int
    teacher_id: int
    title: str
    description: Union[str, None] = None
    technologicals: Union[str, None] = None

class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True


class ChapterBase(BaseModel):
    category: int
    teacher_id: int
    title: str
    description: Union[str, None] = None
    technologicals: Union[str, None] = None

class ChapterCreate(ChapterBase):
    pass


class Chapter(ChapterBase):
    id: int

    class Config:
        orm_mode = True