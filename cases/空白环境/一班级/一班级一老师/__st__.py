from cfg.cfg import gradeToId, subjectToId
from lib.api.SClass import getFirstClass
from lib.api.Student import student
from lib.api.Teacher import teacher

tidList = []


def suite_setup():
    # 创建一老师
    subject = '初中数学'
    username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
        'zhangming', '张明', subjectToId[subject], [{"id": getFirstClass()['id']}], '13451813456', \
        'zhangming@163.com', '3209251983090987799'
    r = teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
                        classlist=classlist, phonenumber=phonenumber, email=email,
                        idcardnumber=idcardnumber)
    tidList.append(r.json()['id'])


# 套件清除，只执行一次
def suite_teardown():
    # 删除所创建的老师
    for tid in tidList:
        teacher.del_teacher(tid)
