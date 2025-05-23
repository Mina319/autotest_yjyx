from lib.api.SClass import sclass, getFirstClass
from hytest import INFO


def suite_setup():
    # 创建一个班级
    newgrade, newname, studentlimit = '七年级', '实验一班', 80
    sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)


# 套件清除，只执行一次
def suite_teardown():
    # 执行用例过程中，创建的班级可能多次创建和删除，班级id会变化
    r = sclass.list_class()
    cid = r.json()["retlist"][0]["id"]
    sclass.del_class(cid)
    # INFO(f'班级{r.json()["retlist"]}')
    # sclass.del_allclasses()
