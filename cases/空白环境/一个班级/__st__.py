from lib.api.SClass import sclass

cid = None


def suite_setup():
    # 创建一个班级
    newgrade, newname, studentlimit = '七年级', '实验一班', 80
    r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
    addRet = r.json()
    global cid
    cid = addRet["id"]


# 套件清除，只执行一次
def suite_teardown():
    sclass.del_class(classid=cid)
