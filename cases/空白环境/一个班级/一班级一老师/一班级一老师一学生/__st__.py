from lib.api.Student import student
from lib.api.SClass import *
from hytest import INFO
from cfg.cfg import *


def suite_setup():
    # 创建一个学生
    classid = getFirstClass()["id"]
    username, realname, grade, phonenumber = 'benzhi', '张本智和', '高一', '13723451089'
    student.add_student(username=username, realname=realname, gradeid=gradeToId[grade],
                            classid=classid, phonenumber=phonenumber)


# 套件清除，只执行一次
def suite_teardown():
    student.del_allstudents()
