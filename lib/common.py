import hashlib
from functools import wraps


def md5(pwd):
    md5 = hashlib.md5()
    val = '王氏家族终极密码'
    md5.update(val.encode('utf-8'))
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()


def login_auth(role):
    def outter(func):
        @wraps(func)
        def inner(*args, **kwargs):
            while True:
                if role == 'admin':
                    from core import admin_view
                    user = admin_view.admin_info['user']
                    if user:
                        return func(*args, **kwargs)
                    else:
                        print('请先登录')
                        break
                elif role == 'student':
                    from core import student_view
                    user = student_view.student_info['user']
                    if user:
                        return func(*args, **kwargs)
                    else:
                        print('请先登录')
                        break
                elif role == 'teacher':
                    from core import teacher_view
                    user = teacher_view.teacher_info['user']
                    if user:
                        return func(*args, **kwargs)
                    else:
                        print('请先登录')
                        break
        return inner
    return outter

























