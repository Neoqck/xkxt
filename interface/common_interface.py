from db import models
from lib import common
import os
from conf import setting


# 公共登录
def login_interface(user_name, user_pwd, role):
    obj = None
    # 校验身份
    if role == 'admin':
        # 判断对象是否存在
        obj = models.Admin.select_obj(user_name)
        user_pwd = common.md5(user_pwd)
        # 如果不存在，失败，存在就校验密码
    # 校验身份
    elif role == 'student':
        # 判断对象是否存在
        obj = models.Student.select_obj(user_name)
        user_pwd = common.md5(user_pwd)
        # 如果不存在，失败，存在就校验密码
    # 校验身份
    elif role == 'teacher':
        # 判断对象是否存在
        obj = models.Teacher.select_obj(user_name)
        user_pwd = common.md5(user_pwd)
        # 如果不存在，失败，存在就校验密码

    if not obj:
        return False, '用户不存在，重新输入！'

    if obj.pwd == user_pwd:
        return True, '登录成功！'

    else:
        return False, '密码错误！'


# 获取所有学校
def check_school_interface():
    # 拼接存放学校文件的路径
    school_dir = os.path.join(setting.DB_PATH, 'School')

    if os.path.exists(school_dir):
        # 获取文件(夹)下的所有文件的名字
        school_list = os.listdir(school_dir)
        return school_list


# 获取学校下的所有课程
def check_course_interface(school_name):
    school_obj = models.School.select_obj(school_name)

    # 通过拿到的学校对象，拿到学校对象中的所有课程的列表
    course_list = school_obj.course_list

    # 判断列表是否为空
    if course_list:
        return True, course_list
    return False, '学校还没有课程，请联系管理员！'


























