from cfg.cfg import gradeToId, subjectToId
from lib.api.SClass import getFirstClass
from lib.api.Student import student
from lib.api.Teacher import teacher

tidList = []


def suite_setup():
    # 创建一老师
    subject = '初中科学'
    username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
        'tangsen', '唐僧', subjectToId[subject], [{"id": getFirstClass()['id']}], '12451813456', \
        'tangsen@163.com', '3209250020090988811'
    r = teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
                        classlist=classlist, phonenumber=phonenumber, email=email,
                        idcardnumber=idcardnumber)
    tidList.append(r.json()['id'])


# 套件清除，只执行一次
def suite_teardown():
    # 删除所创建的老师
    for tid in tidList:
        teacher.del_teacher(tid)
