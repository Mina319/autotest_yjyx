from lib.api.SClass import sclass, getFirstClass
from hytest import INFO

cid = None

def suite_setup():
    # 创建一个班级
    newgrade, newname, studentlimit = '七年级', '实验一班', 80
    r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
    global cid
    cid = r.json()["retlist"][0]["id"]


# 套件清除，只执行一次
def suite_teardown():
    # 删除该班级
    sclass.del_class(cid)

