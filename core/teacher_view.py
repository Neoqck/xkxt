from lib import common
from interface import common_interface
from interface import teacher_interface


teacher_info = {'user': None}


# 登录
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
        flag, msg = common_interface.login_interface(user_name, user_pwd, 'teacher')
        if flag:
            print(msg)
            teacher_info['user'] = user_name
            break
        else:
            print(msg)
            continue


# 选择教授课程
@common.login_auth('teacher')
def choose_course():
    while True:
        print('---选择课程---')
        # 获取学校-->循环打印学校-->选择学校-->打印学校中的课程列表-->让老师选择-->添加到老师对象的课程列表中
        school_list = common_interface.check_school_interface()
        # 判断学校是否存在
        if not school_list:
            print('还没有学校可以选择，请联系管理员！')
            break
        # 循环打印
        for index, school_name in enumerate(school_list):
            print(index, school_name)

        # 选择
        choice = input('请输入学校编号：').strip()
        if not choice.isdigit():
            print('请规范选择，输入数字！')
            continue
        choice = int(choice)

        if choice not in range(len(school_list)):
            print('请规范选择，不在范围!')
            continue
        # 1.拿到学校名称
        school_name = school_list[choice]

        # 通过学校名称，获取学校下的所有课程列表
        flag, course_list = common_interface.check_course_interface(school_name)

        if not flag:
            print(course_list)
            break
        # 循环打印
        for index, course_name in enumerate(course_list):
            print(index, course_name)

        choice = input('请输入课程编号：').strip()
        if not choice.isdigit():
            print('输入不规范，请输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('输入不规范，不在范围！')
            continue

        # 拿到课程名称
        course_name = course_list[choice]

        # 调用选择教授课程接口
        flag, msg = teacher_interface.choose_course_interface(course_name,teacher_info['user'])

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 查看教授课程
@common.login_auth('teacher')
def check_course():
    while True:
        print('---教授课程---')
        flag, course_list = teacher_interface.check_course(teacher_info['user'])
        if flag:
            print(course_list)
            break
        else:
            print(course_list)
            break


# 查看课程下学生
@common.login_auth('teacher')
def check_course_student():
    while True:
        print('---查看课程下学生---')
        # 打印老实的课程列表-->选择课程-->查看课程下的学生
        flag, course_list = teacher_interface.check_course(teacher_info['user'])
        if not flag:
            print(course_list)
            break
        # 打印课程列表
        for index, course_name in enumerate(course_list):
            print(index, course_name)

        choice = input('请输入课程编号：').strip()
        if not choice.isdigit():
            continue
        choice = int(choice)

        if choice not in range(len(course_list)):
            continue
        # 获取了课程名称
        course_name = course_list[choice]

        # 调用接口，获取课程下的学生列表
        flag, student_list = teacher_interface.check_student(course_name, teacher_info['user'])
        if flag:
            print(student_list)
            break
        else:
            print(student_list)
            break


# 修改学生成绩
@common.login_auth('teacher')
def change_score():
    while True:
        # 获取老师中所有的课程，并选择
        flag, course_list_or_msg = teacher_interface.check_course(teacher_info['user'])

        if not flag:
            print(course_list_or_msg)
            break

        # 通过课程查看课程中所有的学生
        for index, course_name in enumerate(course_list_or_msg):
            print(index, course_name)

        choice = input('请输入课程编号:').strip()
        if not choice.isdigit():
            print('输入不规范，请输入数字！')
            continue

        choice = int(choice)

        if choice not in range(len(course_list_or_msg)):
            print('输入不规范，不在范围！')
            continue

        course_name = course_list_or_msg[choice]

        # 调用查看课程中所有学生接口
        flag, student_list = teacher_interface.check_student(course_name, teacher_info['user'])

        if not flag:
            print(student_list)
            break

        # 先循环打印所有的学生，并选择学生编号，获取学生姓名
        for index, student_name in enumerate(student_list):
            print(index, student_name)

        choice2 = input('请输入学生编号：').strip()
        if not choice2.isdigit():
            print('输入不规范，请输入数字！')
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(student_list)):
            print('输入不规范，不在范围！')
            continue

        # 获取学生姓名
        student_name = student_list[choice2]

        # 让老师输入修改课程的分数
        score = input('请输入修改的分数：').strip()

        # 课后作业1，校验修改的分数是否是数字
        # if not score.isdigit():
        #     print('输入不规范，输入数字！')
        #     continue

        score = int(score)

        # 课后作业2，校验输入的成绩是否 >100
        # if score < 0 or score > 100:
        #     print('输入不规范，输入正确范围！')
        #     continue

        # 调用修改学生分数接口
        flag, msg = teacher_interface.change_score(
            student_name, course_name, score, teacher_info['user']
        )

        if flag:
            print(msg)
            break


def run():
    while True:
        print('你已进入老师端！')
        print('''
        1.登录
        2.选择教授课程
        3.查看教授课程
        4.查看课程下学生
        5.修改学生成绩
        q.返回
        ''')
        dict = {
            '1': login,
            '2': choose_course,
            '3': check_course,
            '4': check_course_student,
            '5': change_score
        }
        choice = input('选择功能：').strip()
        if choice == 'q':
            break
        elif not choice in dict:
            print('输入不正确!重新来过')
            continue
        dict[choice]()











































