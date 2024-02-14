from typing import List, Union
import mimetypes
from fastapi import (
    APIRouter,
    Depends,
    WebSocket,
    Form,
    Query,
    File,
    UploadFile,
    Response,
    HTTPException
)
from datetime import datetime
from typing import List, Optional
import asyncio
from sqlalchemy import and_, func
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, validator
from sqlalchemy.orm import Session

import json
from DevIntellity.models import lms_models

from DevIntellity.models.lms_models import Course, CourseCategory

from ..db import SessionLocal
from ..crud import lms_crud
from ..schemas import lms_schemas

lms_views = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# pydantic:

# class SuggData(BaseModel):
#     # date: datetime
#     reason: int
#     author: str
#     receiver_depart: int
#     message: str
#     is_hidden: bool


@lms_views.get("/category/", response_model=List[lms_schemas.CourseCategory])
def read_course_categoryies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    
    categories = lms_crud.get_categoryes(db, skip=skip, limit=limit)

    categories = [
        {
            "id": category.id,
            "title": category.title,
            "description": category.description,
            "count": db.query(Course).filter(Course.category == category.id).count()
        }
        for category in categories
    ]

    return JSONResponse(
        content={
            "status": True,
            "data": categories,
        },
        status_code=200,
    )

@lms_views.post("/category/", response_model=lms_schemas.CourseCategory)
def create_course_category(category: lms_schemas.CourseCategoryCreate, db: Session = Depends(get_db)):
    db_category = lms_crud.get_category_by_title(db, title=category.title)
    if db_category:
        raise HTTPException(status_code=400, detail="категория уже существует")
    return lms_crud.create_category(db=db, category=category)


@lms_views.get("/courses/")
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    
    courses = lms_crud.get_courses(db, skip=skip, limit=limit)
    
    # categories = [
    #     {
    #         "id": category.id,
    #         "title": category.title,
    #         "description": category.description,
    #         "count": db.query(Course).filter(Course.category == category.id).count()
    #     }
    #     for category in categories
    # ]

    # return JSONResponse(
    #     content={
    #         "status": True,
    #         "data": categories,
    #     },
    #     status_code=200,
    # )
    return courses



@lms_views.get("/course/")
def read_courses(course_id:int, db: Session = Depends(get_db)):
    
    course = lms_crud.get_get_course_by_id(db,course_id=course_id)
    chapters=db.query(lms_models.Chapter).filter(lms_models.Chapter.course == course_id).all()
    print(chapters)
    data=[]
    chapters = [
        {
            "id": category.id,
            "title": category.title,
            "description": category.description,

        }
        for category in chapters
    ]
    data.append(course_id)
    data.append(chapters)
    return JSONResponse(
        content={
            "status": True,
            "chapters": chapters,
        },
        status_code=200,
    )


@lms_views.post("/course/", response_model=lms_schemas.Course)
def create_course_category(course: lms_schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = lms_crud.get_course_by_title(db, title=course.title)
    if db_course:
        raise HTTPException(status_code=400, detail="курс уже существует")
    return lms_crud.create_course(db=db, course=course)


@lms_views.get("/chapter/")
def read_chapter(chapter_id:int, db: Session = Depends(get_db)):
    
    chapter = lms_crud.get_get_chapter_by_id(db,chapter_id=chapter_id)

    return { "data": chapter}


@lms_views.get("/module/")
def read_module(module_id:int, db: Session = Depends(get_db)):
    
    module = lms_crud.get_get_module_by_id(db,module_id=module_id)

    return { "data": module}




@lms_views.post("/add_chapter_to_course/")
def add_chapter_to_course(course_id:int,title:str,description:str,db: Session = Depends(get_db)):
    chapter_create = lms_models.Chapter(
            course=course_id,
            title=title,
            description=description

        )
    db.add(chapter_create)
    db.commit()

@lms_views.post("/add_module_to_chapter/")
def add_module_to_chapter(course_id:int,chapter_id:int,title:str,description:str,db: Session = Depends(get_db)):
    module_create = lms_models.Module(
            course=course_id,
            chapter=chapter_id,
            title=title,
            description=description

        )
    db.add(module_create)
    db.commit()