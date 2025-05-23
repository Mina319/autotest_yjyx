from lib.api.Teacher import teacher
from lib.api.SClass import *
from hytest import INFO
from cfg.cfg import *


def suite_setup():
    # 创建一个老师
    subject = '初中数学'
    username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
        'zhangming', '张明', subjectToId[subject], [{"id": getFirstClass()['id']}], '13451813456', \
        'zhangming@163.com', '3209251983090987799'
    teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
                        classlist=classlist, phonenumber=phonenumber, email=email,
                        idcardnumber=idcardnumber)


# 套件清除，只执行一次
def suite_teardown():
    # 执行用例过程中，创建的班级可能多次创建和删除，班级id会变化
    # r = teacher.list_class()
    # cid = r.json()["retlist"][0]["id"]
    # sclass.del_class(cid)
    # INFO(f'班级{r.json()["retlist"]}')
    teacher.del_allteachers()
