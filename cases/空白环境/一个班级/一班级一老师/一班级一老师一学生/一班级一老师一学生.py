from hytest import CHECK_POINT, STEP
from selenium.common import NoSuchElementException
from lib.webui import generate_mixed_string

from lib.api.Teacher import teacher, getFirstTeacher
from lib.api.Student import student, getFirstStudent
from cfg.cfg import *
from lib.api.SClass import *
from lib.ui.TeacherUI import *
from lib.ui.StudnetUI import *


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


# web功能
class Case_tc005101:
    name = '老师发布作业1-API-tc005101'

    def teststeps(self):
        STEP(1, '老师登录系统')
        # {'username': 'sunny', 'teachclasslist': [20247], 'realname': '孙四', 'id': 5214, 'phonenumber': '13451812456', 'email': 'sunny@163.com', 'idcardnumber': '3208251983080987799'}
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = getFirstTeacher().values()
        t_ui.open_browser()
        t_ui.login(username)

        STEP(2, '发布作业，包含3道选择题，把这个作业布置给一个学生')
        t_ui.publish_homework(taskname='作业1')

        STEP(3, '学生登录系统')
        sclassid, srealname, susername, sphonenumber, sid = getFirstStudent().values()
        s_ui.open_browser()
        s_ui.login(susername)
        # 学生做作业
        acc = s_ui.do_homework()

        STEP(4, '老师登录系统')
        t_ui.open_browser()
        t_ui.login(username)
        acc1 = t_ui.get_result_acc()
        CHECK_POINT('作业完成正确率是否一致：', acc1 == acc)


class Case_tc005102:
    name = '老师发布作业2-API-tc005102'

    def teststeps(self):
        STEP(1, '老师登录系统')
        # {'username': 'sunny', 'teachclasslist': [20247], 'realname': '孙四', 'id': 5214, 'phonenumber': '13451812456', 'email': 'sunny@163.com', 'idcardnumber': '3208251983080987799'}
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = getFirstTeacher().values()
        t_ui.open_browser()
        t_ui.login(username)
        wd = t_ui.wd
        STEP(2, '发布作业，作业名称为空字符串')
        t_ui.publish_homework(taskname='')

        STEP(3, '查看已发布作业')
        # 点击确定
        wd.find_element(By.XPATH, '(//button[text()="确定"])[2]').click()
        # 点击作业
        wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 已创建作业
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[3]/li/span').click()
        sleep(0.5)
        # 获取信息：
        mes1 = wd.find_element(By.XPATH, '//*[@id="serach_result_table"]/div').text
        CHECK_POINT('查看作业列表中是否出现新的作业', mes1 == '没有找到符合搜索条件的试卷')
        wd.close()


class Case_tc005103:
    name = '老师发布作业3-API-tc005103'

    def teststeps(self):
        STEP(1, '老师登录系统')
        # {'username': 'sunny', 'teachclasslist': [20247], 'realname': '孙四', 'id': 5214, 'phonenumber': '13451812456', 'email': 'sunny@163.com', 'idcardnumber': '3208251983080987799'}
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = getFirstTeacher().values()
        t_ui.open_browser()
        t_ui.login(username)

        STEP(2, '发布作业，作业名称为1个符串')
        t_ui.publish_homework(taskname='z')


class Case_tc005104:
    name = '老师发布作业4-API-tc005104'

    def teststeps(self):
        STEP(1, '老师登录系统')
        # {'username': 'sunny', 'teachclasslist': [20247], 'realname': '孙四', 'id': 5214, 'phonenumber': '13451812456', 'email': 'sunny@163.com', 'idcardnumber': '3208251983080987799'}
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = getFirstTeacher().values()
        t_ui.open_browser()
        t_ui.login(username)

        STEP(2, '发布作业，作业名称为100个符串')
        taskname = generate_mixed_string()
        t_ui.publish_homework(taskname=taskname)

