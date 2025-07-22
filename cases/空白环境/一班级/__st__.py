from lib.api.SClass import sclass
from lib.api.Student import student

scidList = []


def suite_setup():
    # 创建班级
    newgrade, newname, studentlimit = '八年级', '实验二班', 50
    r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
    scidList.append(r.json()['id'])


# 套件清除，只执行一次
def suite_teardown():
    # 删除所创建的班级
    for scid in scidList:
        sclass.del_class(scid)
