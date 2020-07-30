from db import models


# 注册
def register_interface(user_name, user_pwd):
    # 通过user_name判断用户对象是否存在
    obj = models.Admin.select_obj(user_name)
    # 如果对象不存在则创建
    if not obj:
        admin_obj = models.Admin(user_name, user_pwd)
        admin_obj.save_obj()
        return True, f'用户【{user_name}】注册成功！'

    return False, '用户已存在！'


# 创建学校
def create_school_interface(school_name, school_addr, admin_name):
    # 判断学校是否存在，不存则创建
    school_obj = models.Admin.select_obj(school_name)

    if school_obj:
        return False, '学校已存在！'
    # 获取管理员对象，调用管理员的创建学校的方法
    admin_obj = models.Admin.select_obj(admin_name)
    admin_obj.create_school(school_name, school_addr)
    return True, f'【{school_name}】学校创建成功！'


# 创建老师
def create_teacher_interface(teacher_name, admin_name):

    pwd = '123'     # 默认密码

    # 判断老师是否存在，不存在就创建
    teacher_obj = models.Teacher.select_obj(teacher_name)

    if teacher_obj:
        return False, '老师已存在！'

    # 由管理员创建
    admin_obj = models.Admin.select_obj(admin_name)
    admin_obj.create_teacher(teacher_name, pwd)
    return True, f'【{teacher_name}】老师创建成功!'


# 创建课程
def create_course_interface(school_name, course_name, admin_name):
    # 1.获取学校对象 ，判断课程是否存在学校对象课程列表中
    school_obj = models.School.select_obj(school_name)
    if course_name in school_obj.course_list:
        return False, '课程已存在'

    # 2.获取管理员对象，调用管理员对象中的创建课程方法
    admin_obj = models.Admin.select_obj(admin_name)
    admin_obj.create_course(school_name, course_name)
    return True, f'【{course_name}】课程创建成功！'













































