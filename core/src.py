from core import admin_view, student_view, teacher_view


def run():
    while True:
        print('---欢迎进入王氏家族选课---')
        print('''
        1.管理员
        2.学生
        3.老师
        q.退出
        ''')
        dict = {
            '1': admin_view.run,
            '2': student_view.run,
            '3': teacher_view.run
        }
        choice = input('请选择你的功能：').strip()
        if choice == 'q':
            break
        elif choice in dict:
            dict[choice]()
        else:
            print('输入不正确！重新来过')
            continue





