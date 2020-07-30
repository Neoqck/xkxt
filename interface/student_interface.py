from db import models


# 注册
def register_interface(user_name, user_pwd):
    # 通过user_name 判断用户对象是否存在
    obj = models.Student.select_obj(user_name)

    # 如果对象不存在则创建
    if not obj:
        admin_obj = models.Student(user_name, user_pwd)
        admin_obj.save_obj()
        return True, f'用户【{user_name}】注册成功！'

    return False, '用户已存在！'


# 选择学校接口
def choose_school_interface(school_name, student_name):
    # 获取学生对象
    student_obj = models.Student.select_obj(student_name)
    # 判断学生是否已经选择了学校
    if student_obj.school:
        return False, '已经选择过学校了！'
    # 若不存在，则调用学生对象中的选择学校的方法，添加学校
    student_obj.add_school(school_name)
    return True, f'【{school_name}】学校添加成功！'


# 获取当前学生中学校的所有课程
def select_course_list(student_name):
    # 获取当前学生对象 ----》看学生是否已经选择学校
    student_obj = models.Student.select_obj(student_name)
    school_name = student_obj.school

    # # 判断学校是否存在
    if not school_name:
        return False, '请先选择学校！'

    # 拿到了学校名字--->获取学校对象--->拿到学校对象中的课程列表
    school_obj = models.School.select_obj(school_name)
    course_list = school_obj.course_list
    # 判断课程列表是否存在
    if course_list:
        return True, course_list
    else:
        return False, '该学校还没有课程！'


# 选择课程
def choose_course(course_name, student_name):
    # 获取学生对象--->拿到学生中的课程列表
    student_obj = models.Student.select_obj(student_name)
    course_list = student_obj.course_list

    # 判断当前选择的课程，是否已经存在课程列表中
    if course_name in course_list:
        return False, '该课程已经存在！'

    # 若不存在，则添加到课程列表中，让学生对象调用添加课程方法
    student_obj.add_course(course_name)
    return True, f'【{course_name}】课程添加成功！'


# 查看分数
def check_score(student_name):
    # 获取学生对象
    student_obj = models.Student.select_obj(student_name)
    # 拿到分数字典
    score_dict = student_obj.score
    return score_dict

















































