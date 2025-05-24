from hytest import CHECK_POINT, STEP
from lib.api.Teacher import teacher, getFirstTeacher
from lib.api.Student import student, getFirstStudent
from cfg.cfg import *
from lib.api.SClass import *


# 老师
class Case_tc001002:
    name = '添加老师2-API-tc001002'

    def teststeps(self):
        STEP(1, '创建老师')
        subject = '初中体育'
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
            'lining', '李宁', subjectToId[subject], [{"id": getFirstClass()['id']}], '13410243456', \
            'lining@163.com', '3209251988090987199'
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


class Case_tc001003:
    name = '添加老师3-API-tc001003'

    def teststeps(self):
        STEP(1, '创建老师')

        # {'username': 'sunny', 'teachclasslist': [20247], 'realname': '孙四', 'id': 5214, 'phonenumber': '13451812456', 'email': 'sunny@163.com', 'idcardnumber': '3208251983080987799'}
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = getFirstTeacher().values()

        subject = '初中体育'
        username1, realname1, subjectid1, classlist1, phonenumber1, email1, idcardnumber1 = \
            username, '李宁', subjectToId[subject], [{"id": getFirstClass()['id']}], '13410243456', \
            'lining@163.com', '3209251988090987199'
        r = teacher.add_teacher(username=username1, realname=realname1, subjectid=subjectid1,
                                classlist=classlist1, phonenumber=phonenumber1, email=email1,
                                idcardnumber=idcardnumber1)
        addRet = r.json()
        print('addRet----', addRet)

        expected = {
            "retcode": 1,
            "reason": f"登录名 {username} 已经存在"
        }
        print('expected----', expected)
        CHECK_POINT('返回的响应体符合预期', addRet == expected)

        STEP(2, '列出老师')
        r = teacher.list_teacher(subject=subject)
        listRet = r.json()
        print('listRet----', listRet)
        self.tid = None
        if addRet != expected:
            self.tid = addRet["id"]

        flag = True
        if self.tid is not None:
            for infos in listRet['retlist']:
                if infos['username'] == username and infos["id"] == self.tid:
                    flag = False
                    break
        CHECK_POINT('返回的消息体，没有刚刚添加的老师的', flag)


class Case_tc001051:
    name = '修改老师1-API-tc001051'

    def teststeps(self):
        STEP(1, '修改老师：老师ID不存在')
        tid = 111
        r = teacher.modify_teacher(tid)
        modifyRet = r.json()
        expected = {
            "retcode": 1,
            "reason": f" id 为`{tid}`的老师不存在"
        }
        print('modifyRet----', modifyRet)
        print('expected----', expected)
        CHECK_POINT('返回消息体是否符合预期', modifyRet == expected)


class Case_tc001052:
    name = '修改老师2-API-tc001052'

    def setup(self):
        # 新建第二个班级
        newgrade, newname, studentlimit = '八年级', '实验二班', 50
        r = sclass.add_class(grade=newgrade, classname=newname, studentlimit=studentlimit)
        addRet = r.json()
        self.cid = addRet['id']

    def teststeps(self):
        STEP(1, '修改老师')
        # {'username': 'sunny', 'teachclasslist': [20247], 'realname': '孙四', 'id': 5214, 'phonenumber': '13451812456', 'email': 'sunny@163.com', 'idcardnumber': '3208251983080987799'}
        username, teachclasslist, realname, tid, phonenumber, email, idcardnumber = getFirstTeacher().values()
        teachclasslist1 = [{"id": teachclasslist[0]}]
        teachclasslist1.append({"id": self.cid})
        # teachclasslist.append(self.cid)
        realname1 = '张星星'
        try:
            r = teacher.modify_teacher(teacherid=tid, realname=realname1, classlist=teachclasslist1)
            # 检查返回状态码
            if r.status_code == 200:
                modifyRet = r.json()
                expected = {"retcode": 0}
                print('modifyRet----', modifyRet)
                print('expected----', expected)
                CHECK_POINT('返回消息体是否符合预期', modifyRet == expected)
            else:
                print(f"修改老师信息失败，响应状态码：{r.status_code}")
                print(f"响应内容：{r.text}")
        except Exception as e:
            print(f"修改老师信息时发生错误：{str(e)}")

        STEP(2, '列出老师')
        r = teacher.list_teacher()
        listRet = r.json()
        flag = False
        for ts in listRet["retlist"]:
            if ts["id"] == tid and ts["realname"] == realname1 and ts["teachclasslist"] == [i["id"] for i in teachclasslist1]:
                # 找到该老师，并且信息也都是修改后的
                flag = True
        CHECK_POINT('信息是否更正', flag)

    def teardown(self):
        # 删掉新增班级
        sclass.del_class(self.cid)


class Case_tc001081:
    name = '删除老师1-API-tc001081'

    def teststeps(self):
        STEP(1, '删除老师：使用不存在的老师ID')
        tid = 1111
        r = teacher.del_teacher(tid)
        delRet = r.json()
        print('delRet----', delRet)
        expected = {
            "retcode": 404,
            "reason": f"id 为`{tid}`的老师不存在"
        }
        CHECK_POINT('响应体消息是否符合预期', expected == delRet)


class Case_tc001082:
    name = '删除老师2-API-tc001082'

    def teststeps(self):
        STEP(1, '删除老师')
        username, teachclasslist, realname, tid, phonenumber, email, idcardnumber = getFirstTeacher().values()
        r = teacher.del_teacher(tid)
        delRet = r.json()
        print('delRet----', delRet)
        expected = {
            "retcode": 0
        }
        CHECK_POINT('响应体消息是否符合预期', expected == delRet)

        STEP(2, '列出老师')
        r = teacher.list_teacher()
        listRet = r.json()

        flag = True
        for ts in listRet["retlist"]:
            if ts["id"] == tid:
                flag = False
        CHECK_POINT('该老师不在列表中', flag)


# 学生
class Case_tc002001:
    name = '添加学生1-API-tc002001'

    def teststeps(self):
        STEP(1, '创建学生')
        classid = getFirstClass()["id"]
        username, realname, grade, phonenumber = 'benzhi', '张本智和', '高一', '13723451089'
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
