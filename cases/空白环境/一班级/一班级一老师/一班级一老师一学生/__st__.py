from cfg.cfg import gradeToId
from lib.api.SClass import getFirstClass
from lib.api.Student import student

sidList = []


def suite_setup():
    # 创建一学生
    username, realname, grade, classid, phonenumber = 'qinsang', '秦桑', '高一', \
                                                      getFirstClass()["id"], '1894567233'
    gradeid = gradeToId[grade]
    r = student.add_student(username, realname, gradeid, classid, phonenumber)
    sidList.append(r.json()['id'])


# 套件清除，只执行一次
def suite_teardown():
    # 删除所创建的学生
    for sid in sidList:
        student.del_student(sid)
