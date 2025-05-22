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
            'zhangming', '张明', subjectToId[subject], [{"id": getFirstClass()['id']}], '13451813456', \
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


class Case_tc000002:
    name = '添加班级2-API-tc000002'

    def teststeps(self):
        STEP(1, '创建不同年级的不同名班级')
        # 获取已经存在班级的信息
        # {'name': '实验一班', 'grade__name': '七年级', 'invitecode': '202563130374', 'studentlimit': 80, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
        newgrade, newname, studentlimit = '八年级', '实验二班', 70
        r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
        addRet = r.json()
        self.cid = addRet["id"]
        invitecode = addRet["invitecode"]
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
        print('listRet----', listRet)
        flag = False
        for cinfo in listRet['retlist']:
            name1, grade__name1, invitecode1, studentlimit1, studentnumber1, id1, _ = cinfo.values()
            if self.cid == id1 and invitecode == invitecode1:
                flag = True
                break
        CHECK_POINT('返回的消息体数是否包含刚刚添加的班级信息', flag)

    def teardown(self):
        # 删除该班级
        sclass.del_class(self.cid)


class Case_tc000003:
    name = '添加班级3-API-tc000003'

    def teststeps(self):
        STEP(1, '创建同年级的同名班级')
        # 获取已经存在班级的信息
        # {'name': '实验一班', 'grade__name': '七年级', 'invitecode': '202563130374', 'studentlimit': 80, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
        name, gradename, _, _, _, _, _ = getFirstClass().values()
        studentlimit = 55
        try:
            r = sclass.add_class(grade=gradename, classname=name, studentlimit=studentlimit)
            addRet = r.json()
            invitecode = addRet["invitecode"]
            expected = {
                "retcode": 1,
                "reason": "duplicated class name"
            }
            print('addRet----', addRet)
            print('expected----', expected)
            CHECK_POINT('返回值和期望一致', addRet == expected)
        except Exception as e:
            print("添加班级失败，异常信息：", str(e))
            # 失败断言
            assert False, f"添加班级异常或返回结构错误，异常信息: {e}"

        STEP(2, '列出班级')
        r = sclass.list_class(grade=gradename)
        listRet = r.json()
        print('listRet----', listRet)
        flag = True
        for cinfo in listRet['retlist']:
            name1, grade__name1, invitecode1, studentlimit1, studentnumber1, id1, _ = cinfo.values()
            if self.cid == id1 and invitecode == invitecode1:
                flag = False
                break
        CHECK_POINT('返回的消息体数是否包含刚刚添加的班级信息', flag)

    def teardown(self):
        # 删除该班级
        sclass.del_class(self.cid)


class Case_tc000051:
    name = '修改班级1-API-tc000051'

    def teststeps(self):
        STEP(1, '修改班级')
        # 获取已经存在班级的信息
        # {'name': '实验一班', 'grade__name': '七年级', 'invitecode': '202563130374', 'studentlimit': 80, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
        self.name, gradename, _, self.studentlimit, _, self.cid, _ = getFirstClass().values()
        newname = '实验三班'
        r = sclass.modify_class(self.cid, newname)
        modifyRet = r.json()
        print('modifyRet----', modifyRet)
        CHECK_POINT('修改班级返回retcode为0', modifyRet['retcode'] == 0)

        STEP(2, '列出班级')
        r = sclass.list_class(grade=gradename)
        listRet = r.json()
        print('listRet----', listRet)
        flag = True
        for cinfo in listRet['retlist']:
            name1, grade__name1, invitecode1, studentlimit1, studentnumber1, id1, _ = cinfo.values()
            if self.cid == id1:
                flag = name1 == newname
                break
        CHECK_POINT('班级名是否修改成功', flag)

    def teardown(self):
        # 该班级名修改回来
        sclass.modify_class(self.cid, self.name)


class Case_tc000052:
    name = '修改班级2-API-tc000052'

    def teststeps(self):
        STEP(1, '修改班级')
        # 获取已经存在班级的信息
        # {'name': '实验一班', 'grade__name': '七年级', 'invitecode': '202563130374', 'studentlimit': 80, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
        self.name, gradename, _, self.studentlimit, _, self.cid, _ = getFirstClass().values()
        newname = '实验三班'
        r = sclass.modify_class(self.cid, self.name)
        modifyRet = r.json()
        print('modifyRet----', modifyRet)
        expected = {
            "retcode": 1,
            "reason": "duplicated class name"
        }
        CHECK_POINT('响应体消息是否符合预期', expected == modifyRet)

        STEP(2, '列出班级')
        r = sclass.list_class(grade=gradename)
        listRet = r.json()
        print('listRet----', listRet)
        flag = None
        for cinfo in listRet['retlist']:
            name1, grade__name1, invitecode1, studentlimit1, studentnumber1, id1, _ = cinfo.values()
            if self.cid == id1:
                flag = name1 == self.name
                break
        CHECK_POINT('班级名是否修改成功', flag)



