from lib.api.SClass import sclass
from lib.api.Teacher import teacher
from lib.api.Student import student

cid = None


def suite_setup():
    # 创建一个班级
    newgrade, newname, studentlimit = '七年级', '实验一班', 80
    r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
    addRet = r.json()
    # {'name': '实验二班', 'grade__name': '八年级', 'invitecode': '202563130374', 'studentlimit': 50, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
    global cid
    cid = addRet['id']
    print(f'班级id：', cid)


# 套件清除，只执行一次
def suite_teardown():
    # 删除创建的班级
    sclass.del_class(cid)

