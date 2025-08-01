from cfg.cfg import gradeToId, subjectToId
from lib.api.SClass import getFirstClass, sclass
from lib.api.Student import student
from lib.api.Teacher import teacher


sidList = []


def suite_setup():
    # 创建三学生
    username, realname, grade, classid, phonenumber = 'wujing', '悟净', '高三', \
                                                      getFirstClass()["id"], '18777767233'
    gradeid = gradeToId[grade]
    r = student.add_student(username, realname, gradeid, classid, phonenumber)
    sidList.append(r.json()['id'])

    r = student.add_student('wuneng', '悟能', gradeToId['高二'], classid, '12723135643')
    sidList.append(r.json()['id'])

    r = student.add_student('wukong', '悟空', gradeToId['高一'], classid, '15623135613')
    sidList.append(r.json()['id'])


# 套件清除，只执行一次
def suite_teardown():

    # 删除所创建的学生
    for sid in sidList:
        student.del_student(sid)


