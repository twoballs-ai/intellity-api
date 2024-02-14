from sqlalchemy import (Boolean
                        , Column
                        , ForeignKey
                        , Integer
                        , String
                        , BigInteger
                        , Text)
from sqlalchemy.orm import relationship

from ..db import Base


class Teacher(Base):
    __tablename__ = "teacher_model"    

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    qualification = Column(String)
    skills = Column(Text)

    def __str__(self):
        return str(self.id)

    # class Meta:
    #     verbose_name = 'учитель'
    #     verbose_name_plural = 'учителя'
    #     permissions = (("sample_permission", "can change sth of sth"),)

    # def skill_list(self):
    #     skill_list=self.skills.split(',')
    #     return skill_list        

    # def total_teacher_courses(self):
    #     total_courses= lms.models.Course.objects.filter(teacher = self).count()
    #     return total_courses
    
    # def total_teacher_chapters(self):
    #     total_chapters= lms.models.Chapter.objects.filter(course__teacher= self).count()
    #     return total_chapters

    # def total_teacher_students(self):
    #     total_students= lms.models.CourseEnroll.objects.filter(course__teacher = self).count()
    #     return total_students
    


class Student(Base):
    __tablename__ = "user_model"    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    interested_categories = Column(Text)
    
    def __str__(self):
        return str(self.id)

    # class Meta:
    #     verbose_name = 'ученик'
    #     verbose_name_plural = 'ученики'
    #     permissions = (("sample_permission", "can change sth in sth"),)

    # def total_student_score(self):
    #     student_score= lms.models.TotalStudentScore.objects.get_or_create(student=self)[0]
    #     student_score = student_score.total_student_score
    #     return student_score
    
    # def total_student_energy(self):
    #     student_energy= lms.models.TotalStudentEnergy.objects.get_or_create(student=self)[0]
    #     print(student_energy)
    #     student_energy = student_energy.total_student_energy
    #     print(student_energy)
    #     return student_energy

    # def total_student_enroll_courses(self):
    #     enrolled_courses= lms.models.CourseEnroll.objects.filter(student = self).count()
    #     return enrolled_courses
    
    # def total_favorite_courses(self):
    #     favorite_course= lms.models.FavoriteCourse.objects.filter(student= self).count()
    #     return favorite_course
    
    # def total_completed_tasks(self):
    #     completed_task= lms.models.TaskForStudentsFromTeacher.objects.filter(student = self, complete_status=True).count()
    #     return completed_task    

    # def total_pending_tasks(self):
    #     pending_task= lms.models.TaskForStudentsFromTeacher.objects.filter(student = self, complete_status=False).count()
    #     return pending_task   