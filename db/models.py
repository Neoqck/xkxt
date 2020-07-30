from db import db_handler
from lib import common


# 主父
class Base():
    # 保存
    def save_obj(self):
        db_handler.save(self)

    # 直接用类来调用，所有(以)用类绑定
    @classmethod
    def select_obj(cls, name):
        obj = db_handler.select(cls, name)
        return obj


# 管理员
class Admin(Base):

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = common.md5(pwd)

    # 管理员创建学校方法
    def create_school(self, school_name, school_addr):
        school_obj = School(school_name, school_addr)
        school_obj.save_obj()

    # 创建老师
    def create_teacher(self, teacher_name, pwd):
        teacher_obj = Teacher(teacher_name, pwd)
        teacher_obj.save_obj()

    # 创建课程
    def create_course(self, school_name, course_name):
        course_obj = Course(school_name, course_name)
        course_obj.save_obj()
        # 把课程添加到学校中
        school_obj = School.select_obj(school_name)
        school_obj.course_list.append(course_name)
        school_obj.save_obj()


# 学校类
class School(Base):
    def __init__(self, school_name, school_addr):
        self.name = school_name
        self.addr = school_addr
        # 此学校的课程列表
        self.course_list = []


# 老师类
class Teacher(Base):
    def __init__(self, teacher_name, pwd):
        self.name = teacher_name
        self.pwd = common.md5(pwd)
        self.course_list = []

    # 添加课程
    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save_obj()

    # 查看课程下的所有学生方法
    def check_course_student(self, course_name):
        # 获取课程对象
        course_obj = Course.select_obj(course_name)
        # 获取学生列表
        student_list = course_obj.student_list
        return student_list

    # 老师修改分数方法
    def change_score(self, student_name, course_name, score):
        # 1.获取学生对象
        student_obj = Student.select_obj(student_name)

        # 2.直接修改学生score属性
        student_obj.score[course_name] = score
        student_obj.save_obj()


# 课程类
class Course(Base):
    def __init__(self, school_name, course_name):
        self.school = school_name
        self.name = course_name
        # 此课程的学生列表
        self.student_list = []

    # 添加学生
    def add_student(self, student_name):
        self.student_list.append(student_name)
        self.save_obj()


# 学生类
class Student(Base):
    def __init__(self, student_name, pwd):
        self.name = student_name
        self.pwd = common.md5(pwd)
        self.school = None
        self.course_list = []
        self.score = {}
        self.save_obj()

    # 学生添加学校
    def add_school(self, school_name):
        self.school = school_name
        self.save_obj()

    # 学生添加课程
    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.score[course_name] = 0
        self.save_obj()

        # 课程对象添加学生
        course_obj = Course.select_obj(course_name)
        course_obj.add_student(self.name)




















