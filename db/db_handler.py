import os
from conf import setting
import pickle


# 保存
def save(obj):
    # 获取对象(的类)的名字，就是要保存的目录的名字
    cls_name = obj.__class__.__name__
    # 拼接当前对象保存目录的路径
    dir_path = os.path.join(setting.DB_PATH, cls_name)
    # 判断目录是否存在，不存在则创建
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # 拼接目录下的文件绝对路径
    user_path = os.path.join(dir_path, obj.name)
    # 写入
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()


# 查看
def select(cls, name):
    # admin_obj.__class__ --> Admin.__name__ ----> 'Admin'
    # 获取对象的(类的)名字,比如teacher,admin,student
    cls_name = cls.__name__
    # 拼接路径
    dir_path = os.path.join(setting.DB_PATH, cls_name)
    # 若不存在，则创建目录
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # 拼接当前用户文件的绝对路径
    user_path = os.path.join(dir_path, name)
    # 若存在，则查找，不存在返回NONE
    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj

    # 个人总结，此处应该加一个返回 None，否则路径不存在会报错
    # return None









































