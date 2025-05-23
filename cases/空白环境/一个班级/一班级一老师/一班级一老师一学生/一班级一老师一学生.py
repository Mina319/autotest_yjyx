from hytest import CHECK_POINT, STEP
from lib.api.Teacher import teacher, getFirstTeacher
from lib.api.Student import student, getFirstStudent
from cfg.cfg import *
from lib.api.SClass import *


# 学生
class Case_tc002001:
    name = '添加学生2-API-tc002002'

    def teststeps(self):
        STEP(1, '创建学生')
        classid = getFirstClass()["id"]
        username, realname, grade, phonenumber = 'yaoanna', '姚安娜', '高二', '13823451090'
        r = student.add_student(username=username, realname=realname, gradeid=gradeToId[grade],
                                classid=classid, phonenumber=phonenumber)
        addRet = r.json()
        self.sid = addRet["id"]

        expected = {
            "retcode": 0,
            "id": self.sid
        }
        print('addRet----', addRet)
        print('expected----', expected)
        CHECK_POINT('返回的retcode值=0', addRet == expected)

        STEP(2, '列出学生')
        r = student.list_student()
        listRet = r.json()
        print('listRet----', listRet)
        flag = False
        for infos in listRet['retlist']:
            if infos['id'] == self.sid:
                flag = True
                break
        CHECK_POINT('返回的消息体，是否包含刚刚添加的学生的id', flag)

    def teardown(self):
        # 删除该学生
        student.del_student(self.sid)


class Case_tc002081:
    name = '删除学生1-API-tc002081'

    def teststeps(self):
        STEP(1, '删除学生')
        # 获取已经存在学生的信息
        # "classid": 19,"username": "lxz002","realname": "李钟硕33","phonenumber": "13433335569","id": 174
        self.classid, self.username, self.realname, self.phonenumber, self.sid = getFirstStudent().values()
        r = student.del_student(self.sid)
        delRet = r.json()
        print('delRet----', delRet)
        expected = {
            "retcode": 0,
        }
        CHECK_POINT('响应体消息是否符合预期', expected == delRet)

        STEP(2, '列出班级')
        r = student.list_student()
        listRet = r.json()
        print('listRet----', listRet)
        flag = True  # 查询为空，默认为True
        for sinfo in listRet['retlist']:
            classid1, username1, realname1, phonenumber1, sid1 = sinfo.values()
            if self.sid == sid1 and username1 == self.username:
                flag = False  # 找到的话就是为False
                break
        CHECK_POINT('该学生 是否 不在列出结果中', flag)

    def teardown(self):
        # 删掉，再加回来
        student.add_student(username=self.username, realname=self.realname, gradeid=gradeToId['高一'],
                            classid=self.classid, phonenumber=self.phonenumber)

