from sqlalchemy.orm import Session

from ..models import lms_models
from ..schemas import lms_schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()

def get_category(db: Session, category_id: int):
    return db.query(lms_models.CourseCategory).filter(lms_models.CourseCategory.id == category_id).first()


def get_category_by_title(db: Session, title: str):
    return db.query(lms_models.CourseCategory).filter(lms_models.CourseCategory.title == title).first()

def get_categoryes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(lms_models.CourseCategory).offset(skip).limit(limit).all()


def create_category(db: Session, category: lms_schemas.CourseCategoryCreate):
    db_category = lms_models.CourseCategory(title=category.title, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(lms_models.CourseCategory).filter(lms_models.CourseCategory.id == category_id).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(lms_models.Course).offset(skip).limit(limit).all()
    
def get_course_by_title(db: Session, title: str):
    return db.query(lms_models.Course).filter(lms_models.Course.title == title).first()   

def get_get_course_by_id(db: Session, course_id: int):
    return db.query(lms_models.Course).filter_by(id = course_id).first()

def create_course(db: Session, course: lms_schemas.CourseCreate):
    db_course = lms_models.Course(technologicals=course.technologicals, teacher_id=course.teacher_id, category=course.category, title=course.title, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_get_chapter_by_id(db: Session, chapter_id: int):
    return db.query(lms_models.Chapter).filter_by(id = chapter_id).first()

def get_get_module_by_id(db: Session, module_id: int):
    return db.query(lms_models.Module).filter_by(id = module_id).first()