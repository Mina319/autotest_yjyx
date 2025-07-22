from cfg.cfg import gradeToId
from lib.api.SClass import getFirstClass, sclass
from lib.api.Student import student

sidList = []

scidList = []

def suite_setup():
    # 创建一班级
    newgrade, newname, studentlimit = '高一', '实验一班', 80
    r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
    scidList.append(r.json()['id'])

    # 创建一学生
    username, realname, grade, classid, phonenumber = 'hongyu', '红玉', '高一', \
                                                      r.json()['id'], '1896666212'
    gradeid = gradeToId[grade]
    r = student.add_student(username, realname, gradeid, classid, phonenumber)
    sidList.append(r.json()['id'])


# 套件清除，只执行一次
def suite_teardown():
    # 删除所创建的学生
    for sid in sidList:
        student.del_student(sid)
    # 删除所创建的班级
    for scid in scidList:
        student.del_student(scid)
