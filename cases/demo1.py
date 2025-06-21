from lib.api.Teacher import teacher
from cfg.cfg import *
from lib.api.SClass import *
from lib.api.Student import *
# newgrade, newname, studentlimit = '九年级', '实验一班', 50
# newgrade, newname, studentlimit = '八年级', '实验二班', 50
# r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
# print(r.json())
# r = sclass.list_class()
# listRet = r.json()
# print(listRet)
# print(listRet['retlist'][0]['id'])
# r = sclass.del_class(20278)
# r = sclass.del_class(20272)
# print(r.json())

# subject = '初中数学'
# username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
#     'zhangming', '张明', subjectToId[subject], [{"id": getFirstClass()['id']}], '13451813456', \
#     'zhangming@163.com', '3209251983090987799'
# teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
#                     classlist=classlist, phonenumber=phonenumber, email=email,
#                     idcardnumber=idcardnumber)
#
# username, realname, grade, classid, phonenumber = 'qinsang', '秦桑', '高一', \
#                                                   getFirstClass()["id"], '1894567233'
# gradeid = gradeToId[grade]
# student.add_student(username, realname, gradeid, classid, phonenumber)

# print(r)
# addRet = r.json()
# print(addRet)
#
#
# r = teacher.list_teacher()
# print(r.json())

# r = teacher.del_teacher(5225)
# print(r.json())
# r = teacher.list_teacher()
# print(r.json())

# student.del_allstudents()
# teacher.del_allteachers()
# sclass.del_allclasses()


r = sclass.list_class()
listRet = r.json()
print(listRet)
r = teacher.list_teacher()
print(r.json())
r = student.list_student()
print(r.json())
