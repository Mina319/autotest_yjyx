from hytest import CHECK_POINT, STEP
from lib.api.SClass import sclass
from cfg.cfg import *


class Case_tc000001:
    name = '添加班级1-API-tc000001'

    def teststeps(self):
        STEP(1, '创建班级')
        newgrade, newname, studentlimit = '七年级', '实验一班', 80
        r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
        addRet = r.json()
        invitecode = addRet["invitecode"]
        self.cid = addRet["id"]
        expected = {
            "invitecode": invitecode,
            "retcode": 0,
            "id": self.cid
        }
        print('addRet----', addRet)
        print('expected----', expected)
        CHECK_POINT('返回的retcode值=0', addRet == expected)

        STEP(2, '列出班级')
        r = sclass.list_class(grade=newgrade)
        listRet = r.json()

        expected = {
            "gradeid": gradeToId[newgrade],
            "retlist": [
                {
                    "name": newname,
                    "grade__name": newgrade,
                    "invitecode": invitecode,
                    "studentlimit": studentlimit,
                    "studentnumber": 0,
                    "id": self.cid,
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }
        print('expected----', expected)
        print('listRet----', listRet)
        CHECK_POINT('返回的消息体数据正确，添加班级是否成功', listRet == expected)

    def teardown(self):
        # 删除该班级
        sclass.del_class(self.cid)


