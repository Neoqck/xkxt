from interface import student_interface
from interface import common_interface
from lib import common


student_info = {'user': None}


def register():
    while True:
        print('---学生注册---')
        user_name = input('输入用户名：').strip()
        user_pwd = input('输入密码：').strip()
        pwd_d = input('确认密码：').strip()
        if not user_pwd == pwd_d:
            print('密码不一致')
            continue
        # 调用注册接口
        flag, msg = student_interface.register_interface(user_name, user_pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue

def login():
    '''
    # 登录
    :return:
    '''
    while True:
        print('---登录页面---')
        user_name = input('输入用户名：').strip()
        user_pwd = input('输入密码：').strip()
        # 调用登录接口
        flag, msg = common_interface.login_interface(user_name, user_pwd, 'student')
        if flag:
            print(msg)
            student_info['user'] = user_name
            break
        else:
            print(msg)
            continue


# 选择学校
@common.login_auth('student')
def choose_school():
    while True:
        print('---选择学校---')
        # 先打印学校列表
        school_list = common_interface.check_school_interface()
        if not school_list:
            print('学校还没开，请等待')
            break
        # 循环打印
        for index, school_name in enumerate(school_list):
            print(index, school_name)

        choice = input('请输入选择的学校编号(q.退出)：').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('输入不规范，重新输入！')
            continue

        choice = int(choice)
        # 判断范围
        if choice not in range(len(school_list)):
            print('输入的不在范围，重新输入！')
            continue
        school_name = school_list[choice]
        # 调用学生中的选择学校接口
        flag, msg = student_interface.choose_school_interface(school_name, student_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


# 选择课程
@common.login_auth('student')
def choose_course():
    while True:
        print('---选择课程---')
        # 先查看当前对象的学校中所有的课程
        flag, course_list = student_interface.select_course_list(student_info['user'])
        # 判断返回值是否为空-->看看学校课程列表有没有课程
        if not flag:
            print(course_list)
            break
        # 打印课程列表让用户选择
        for index, course_name in enumerate(course_list):
            print(index, course_name)

        choice = input('请输入选择的课程编号(q.退出)：').strip()

        if choice == 'q':
            break
        if not choice.isdigit():
            print('输入不规范，不是数字！')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('输入不规范，不在范围！')
            continue

        course_name = course_list[choice]

        # 调用学生选择课程接口
        flag, msg = student_interface.choose_course(course_name, student_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


# 查看分数
@common.login_auth('student')
def check_score():
    while True:
        print('---查看分数---')
        score_dict = student_interface.check_score(student_info['user'])
        print(score_dict)
        break


def run():
    while True:
        print('你已进入学生端！')
        print('''
        1.注册
        2.登录
        3.选择校区
        4.选择课程
        5.查看分数
        q.返回
        ''')
        dict = {
            '1': register,
            '2': login,
            '3': choose_school,
            '4': choose_course,
            '5': check_score
        }
        choice = input('选择功能：').strip()
        if choice == 'q':
            break
        elif not choice in dict:
            print('输入不正确！重新来过')
            continue
        dict[choice]()
































































































