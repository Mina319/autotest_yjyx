from hytest import CHECK_POINT, STEP
from lib.api.Teacher import teacher
from lib.api.Student import *
from cfg.cfg import *
from lib.api.SClass import *
from lib.ui.TeacherUI import *
from lib.ui.StudnetUI import *

# 老师
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


# 班级
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
        self.classname, gradename, _, self.studentlimit, _, self.cid, _ = getFirstClass().values()
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
        sclass.modify_class(self.cid, self.classname)


class Case_tc000052:
    name = '修改班级2-API-tc000052'

    def teststeps(self):
        STEP(1, '修改班级')
        # 获取已经存在班级的信息
        # {'name': '实验一班', 'grade__name': '七年级', 'invitecode': '202563130374', 'studentlimit': 80, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
        self.classname, gradename, _, self.studentlimit, _, self.cid, _ = getFirstClass().values()
        r = sclass.modify_class(self.cid, self.classname)
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
                flag = name1 == self.classname
                break
        CHECK_POINT('班级名是否修改成功', flag)


class Case_tc000053:
    name = '修改班级3-API-tc000053'

    def teststeps(self):
        STEP(1, '修改班级：使用不存在的班级ID')
        # 获取已经存在班级的信息
        # {'name': '实验一班', 'grade__name': '七年级', 'invitecode': '202563130374', 'studentlimit': 80, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
        self.classname, gradename, _, self.studentlimit, _, self.cid, _ = getFirstClass().values()
        newname, newlimit = '实验二班', 20
        r = sclass.modify_class(111, newname, newlimit)
        modifyRet = r.json()
        print('modifyRet----', modifyRet)
        expected = {
            "retcode": 404,
            "reason": "id 为`111`的班级不存在"
        }
        CHECK_POINT('响应体消息是否符合预期', expected == modifyRet)


class Case_tc000082:
    name = '删除班级2-API-tc000082'

    def teststeps(self):
        STEP(1, '删除班级')
        # 获取已经存在班级的信息
        # {'name': '实验一班', 'grade__name': '七年级', 'invitecode': '202563130374', 'studentlimit': 80, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
        self.classname, self.gradename, _, self.studentlimit, _, self.cid, _ = getFirstClass().values()
        r = sclass.del_class(self.cid)
        delRet = r.json()
        print('delRet----', delRet)
        expected = {
            "retcode": 0,
        }
        CHECK_POINT('响应体消息是否符合预期', expected == delRet)

        STEP(2, '列出班级')
        r = sclass.list_class(grade=self.gradename)
        listRet = r.json()
        print('listRet----', listRet)
        flag = True  # 查询为空，默认为True
        for cinfo in listRet['retlist']:
            name1, grade__name1, invitecode1, studentlimit1, studentnumber1, id1, _ = cinfo.values()
            if self.cid == id1 and name1 == self.classname:
                flag = False  # 找到的话就是为False
                break
        CHECK_POINT('该老师 是否 不在列出结果中', flag)

    def teardown(self):
        # 删掉，再加回来
        sclass.add_class(self.gradename, self.classname, self.studentlimit)


# web功能

class Case_tc005001:
    name = '老师登录1-API-tc005001'

    def teststeps(self):
        STEP(1, '创建老师')
        subject = '初中数学'
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
            'zhangming', '张明', subjectToId[subject], [{"id": getFirstClass()['id']}], '13451813456', \
            'zhangming@163.com', '3209251983090987799'
        r = teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
                            classlist=classlist, phonenumber=phonenumber, email=email,
                            idcardnumber=idcardnumber)
        self.tid = r.json()["id"]
        CHECK_POINT('是否创建老师成功', r.json()["retcode"] == 0)

        STEP(2, '登录web系统')
        t_ui.open_browser()
        t_ui.login(username=username)
        INFO('检查 学校、姓名、学科、金币、已发布微课、已发布作业 的信息是否正确')
        wd = GSTORE['wd']
        sleep(2)
        infos_ele = wd.find_elements(By.XPATH, '//table//td[2]/a')
        infos = [e.text for e in infos_ele]
        school1, name1, subject1, goldcoin = infos
        goldcoin = 0 if goldcoin == '' else int(goldcoin)
        infos_ele1 = wd.find_elements(By.XPATH, '//*[@class="col-md-12"]//a/h2/strong')
        infos1 = [int(e.text) for e in infos_ele1]
        microlessons, homework = infos1
        sleep(1)
        SELENIUM_LOG_SCREEN(wd, width='70%')

        CHECK_POINT('检查信息是否正确', name1 == realname and subject1 == subject and goldcoin == 0
                    and microlessons == 0 and homework == 0 and school1 == g_school)

        STEP(3, '点击班级学生')
        # 点击班级情况
        wd.find_element(By.XPATH, '//*[@class="main-menu"]//li[4]').click()
        # 点击班级学生
        wd.find_element(By.XPATH, '//*[@class="main-menu"]//li[4]//li/span').click()
        sleep(1)
        # 点击 年级
        wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div/div[1]/a').click()
        sleep(2)
        mes = wd.find_element(By.CSS_SELECTOR, '.panel-body > div:nth-child(2)')
        SELENIUM_LOG_SCREEN(wd, width='70%')
        CHECK_POINT('学生列表是否为空', mes.text == '该班级还没有学生注册')
        wd.close()

    def teardown(self):
        # 删掉老师
        teacher.del_teacher(self.tid)


class Case_tc005081:
    name = '学生登录1-API-tc005081'

    def teststeps(self):
        STEP(1, '创建学生')
        username, realname, grade, classid, phonenumber = 'qinsang', '秦桑', '高一', \
                                                          getFirstClass()["id"], '1894567233'
        gradeid = gradeToId[grade]
        r = student.add_student(username, realname, gradeid, classid, phonenumber)
        self.sid = r.json()["id"]
        CHECK_POINT('是否创建学生成功', r.json()["retcode"] == 0)

        STEP(2, '登录web系统')
        s_ui.open_browser()
        s_ui.login(username=username)
        INFO('检查 学校、姓名、已发布微课、已发布作业 的信息是否正确')
        wd = GSTORE['wd']
        sleep(2)
        infos_ele = wd.find_elements(By.XPATH, '//table//td[2]/span')
        infos = [e.text for e in infos_ele]
        name1, school1, parent = infos
        infos_ele1 = wd.find_elements(By.XPATH, '//*[@id="icon-choose"]/div[1]//h2//strong')
        infos1 = [int(e.text) for e in infos_ele1]
        microlessons, homework = infos1
        sleep(1)
        SELENIUM_LOG_SCREEN(wd, width='70%')
        CHECK_POINT('检查信息是否正确', name1 == realname and microlessons == 0
                    and homework == 0 and school1 == g_school)

        STEP(3, '点击班级学生')
        # 点击错题库
        wd.find_element(By.CSS_SELECTOR, 'div.main-menu a:nth-child(4) > li').click()
        info = wd.find_element(By.CSS_SELECTOR, '#page-wrapper > div > div > div.row.ng-scope > div > span')
        SELENIUM_LOG_SCREEN(wd, width='70%')
        CHECK_POINT('检查错题库', info.text == '您尚未有错题入库哦')
        wd.close()

    def teardown(self):
        # 删掉同学
        student.del_student(self.sid)
