from hytest import CHECK_POINT, STEP
from lib.api.Teacher import teacher
from cfg.cfg import *
from lib.api.SClass import *


class Case_tc001001:
    name = '添加老师1-API-tc001001'

    def teststeps(self):
        STEP(1, '创建老师')
        subject = '初中数学'
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
            'zhangming', '张明', subjectToId[subject], [{"id": getFirstClass()}], '13451813456', \
            'zhangming@163.com', '3209251983090987799'

        r = teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
                                classlist=classlist, phonenumber=phonenumber, email=email,
                                idcardnumber=idcardnumber)
        addRet = r.json()
        self.tid = addRet["id"]

        expected = {
            "retcode": 0,
            "id": self.tid
        }
        print('addRet----', addRet)
        print('expected----', expected)
        CHECK_POINT('返回的retcode值=0', addRet == expected)

        STEP(2, '列出老师')
        r = teacher.list_teacher(subject=subject)
        listRet = r.json()
        print('listRet----', listRet)

        flag = False
        for infos in listRet['retlist']:
            if infos['id'] == self.tid:
                flag = True
                break

        CHECK_POINT('返回的消息体，是否包含刚刚添加的老师的id', flag)

    def teardown(self):
        # 删除该老师
        teacher.del_teacher(self.tid)

