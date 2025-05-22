from lib.api.Teacher import teacher
from cfg.cfg import *
from lib.api.SClass import *
# newgrade, newname, studentlimit = '九年级', '实验一班', 50
# newgrade, newname, studentlimit = '八年级', '实验二班', 50
# r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
# print(r.json())
# r = sclass.list_class()
# listRet = r.json()
# print(listRet)
# print(listRet['retlist'][0]['id'])
# r = sclass.del_class(20267)
# r = sclass.del_class(20263)
# print(r.json())

# username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
#     'zhangming', '张明', subjectToId['初中数学'], [{"id": getFirstClass()}], '13451813456', \
#     'zhangming@163.com', '3209251983090987799'
# username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
#     'sunny', '孙四', subjectToId['初中英语'], [{"id": getFirstClass()}], '13451812456', \
#     'sunny@163.com', '3208251983080987799'
# r = teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
#                         classlist=classlist, phonenumber=phonenumber, email=email,
#                         idcardnumber=idcardnumber)
# print(r)
# addRet = r.json()
# print(addRet)


# r = teacher.list_teacher()
# print(r.json())

# r = teacher.del_teacher(5214)
# r = teacher.del_teacher(5215)
# print(r.json())
# r = teacher.list_teacher()
# print(r.json())


r = sclass.list_class()
listRet = r.json()
print(listRet)
r = teacher.list_teacher()
print(r.json())

