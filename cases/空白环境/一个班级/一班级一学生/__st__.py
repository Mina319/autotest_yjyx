from lib.api.Student import *
from lib.api.SClass import *
from hytest import INFO
from cfg.cfg import *


def suite_setup():
    # 创建一个学生
    username, realname, grade, classid, phonenumber  = 'qinsang', '秦桑', '高一', \
                                                       getFirstClass()["id"], '1894567233'
    gradeid = gradeToId[grade]
    student.add_student(username, realname, gradeid, classid, phonenumber)


# 套件清除，只执行一次
def suite_teardown():
    # 删除学生
    student.del_allstudents()