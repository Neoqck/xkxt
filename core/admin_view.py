from interface import admin_interface
from interface import common_interface
from lib import common

admin_info = {'user': None}


def register():
    '''
    # 注册
    :return:
    '''
    while True:
        print('---管理员注册---')
        user_name = input('输入用户名：').strip()
        user_pwd = input('输入密码：').strip()
        pwd_d = input('确认密码：').strip()
        if not user_pwd == pwd_d:
            print('密码不一致')
            continue
        # 调用注册接口
        flag, msg = admin_interface.register_interface(user_name, user_pwd)
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
        user_pwd = input('输入密码').strip()
        # 调用登录接口
        flag, msg = common_interface.login_interface(user_name, user_pwd, 'admin')
        if flag:
            print(msg)
            admin_info['user'] = user_name
            break
        else:
            print(msg)
            continue


# 创建学校
@common.login_auth('admin')
def create_school():
    '''
    # 创建学校
    :return:
    '''
    while True:
        print('---创建学校页面---')
        school_name = input('输入学校名称：').strip()
        school_addr = input('输入学校地址：').strip()
        # 调用创建学校接口
        flag, msg = admin_interface.create_school_interface(school_name, school_addr, admin_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


# 创建老师
@common.login_auth('admin')
def create_teacher():
    '''
    # 创建老师
    :return:
    '''
    while True:
        print('---创建老师---')
        teacher_name = input('输入老师名称：').strip()
        flag, msg = admin_interface.create_teacher_interface(teacher_name, admin_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


# 创建课程
common.login_auth('admin')
def create_course():
    '''
    # 创建课程
    1.打印学校列表，按照路径来
    2.选择学校
    3.调用接口
    :return:
    '''
    while True:
        print('---创建课程---')
        # 获取所有学校
        school_list = common_interface.check_school_interface()
        if not school_list:
            print('还没有学校，请先返回创建学校再来！')
            break
        # 循环打印，用枚举
        for index, school_name in enumerate(school_list):
            print(index, school_name)

        choice = input('请选择学校：').strip()

        if not choice.isdigit():
            print('请输入编号！')
            continue
        choice = int(choice)

        if choice not in range(len(school_list)):
            print('请输入正确的范围!')
            continue
        school_name = school_list[choice]

        # 选择学校后，输入课程的名称
        course_name = input('输入课程名称：').strip()
        # 调用管理员中创建课程接口
        flag, msg = admin_interface.create_course_interface(school_name, course_name, admin_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


def run():
    while True:
        print('你已进入管理员！')
        print('''
        1.注册
        2.登录
        3.创建学校
        4.创建老师
        5.创建课程
        q.退出
        ''')
        dict = {
            '1': register,
            '2': login,
            '3': create_school,
            '4': create_teacher,
            '5': create_course
        }
        choice = input('选择功能：').strip()

        if choice == 'q':
            break
        elif not choice in dict:
            print('输入不正确!重新来过')
            continue
        dict[choice]()

































