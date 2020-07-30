from db import models


# 老师选择课程
def choose_course_interface(course_name, teacher_name):
    # 获取老师对象--->获取老师对象中的已教学的课程列表
    teacher_obj = models.Teacher.select_obj(teacher_name)
    teacher_course_list = teacher_obj.course_list
    # 判断该课程是否已经存在，不存在则调用添加课程方法添加
    if course_name in teacher_course_list:
        return False, '该课程已经存在'
    # 调用接口，添加课程
    teacher_obj.add_course(course_name)
    return True, f'添加【{course_name}】课程成功！'


# 查看老师下的所有课程
def check_course(teacher_name):
    # 获取老师对象
    teacher_obj = models.Teacher.select_obj(teacher_name)
    # 获取老师对象中的课程列表---老师已教授
    teacher_course_list = teacher_obj.course_list

    if not teacher_course_list:
        return False, '该老师还没有选择教授课程！'
    return True, teacher_course_list


# 查看课程下的所有学生
def check_student(course_name, teacher_name):
    # 获取老师对象
    teacher_obj = models.Teacher.select_obj(teacher_name)
    # 调用查看学生的方法
    student_list = teacher_obj.check_course_student(course_name)

    if not student_list:
        return False, '课程中没有学生'

    return True, student_list


# 老师修改分数接口
def change_score(student_name, course_name, score, teacher_name):
    # 1.获取老师对象
    teacher_obj = models.Teacher.select_obj(teacher_name)
    # 2.通过老师对象，调用修改分数方法
    # 学生名字传入，为了获取学生对象，并修改学生中的课程成绩
    teacher_obj.change_score(student_name, course_name, score)

    return True, f'【{student_name}】学生分数修改成功, 课程[{course_name}]分数为[{score}]分'































