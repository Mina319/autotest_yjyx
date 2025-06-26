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
        wd = t_ui.wd
        # 点击作业
        wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 创建作业
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()

        input = wd.find_element(By.XPATH, '//*[@id="exam_name_text"]')
        taskname = '作业1'
        input.send_keys(taskname)
        wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        sleep(2)
        # 切换窗口iframe，选择题目的小窗口
        wd.switch_to.frame("pick_questions_frame")
        ############
        # 检查是否能够找到某个 iframe 中的元素（例如一个按钮）
        options = wd.find_elements(By.CSS_SELECTOR, '.div-search-question-button-bar label:nth-child(2)')
        for i in range(3):
            options[i].click()
        # 点击确定
        wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(1)

        # 切换窗口：点击确认添加  按钮
        window1 = wd.current_window_handle
        wd.switch_to.window(window1)
        # 确认添加
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(2)

        # 切换窗口：弹框“新建作业成功”，点击发布给学生
        window2 = wd.current_window_handle
        wd.switch_to.window(window2)
        # 弹框点击  将作业发布给学生，不能直接定位id，id是自动生成的
        wd.find_element(By.XPATH, '//button[text()="发布给学生"]').click()

        # 设置主窗口
        mainWindow = wd.current_window_handle
        # 切换至新窗口
        # 所有窗口的句柄
        allHandles = wd.window_handles
        # 进入新窗口
        wd.switch_to.window(allHandles[-1])
        sleep(1)

        # 全选
        wd.find_element(By.CSS_SELECTOR, "a.ng-scope").click()
        # wd.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div[1]/a").click()
        # wd.find_element(By.XPATH, "//a[contains(text(), '全选')]").click()
        # 点击  确定下发
        wd.find_element(By.XPATH, '/html/body/div/div[2]/h3/button').click()
        sleep(0.5)
        # 点击 确定
        wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[3]/button[2]').click()
        sleep(0.5)
        # 提示窗口 点击 确定
        wd.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div/div/button").click()
        # 切换回主窗口
        wd.switch_to.window(mainWindow)

        # 点击 发布给学生
        wd.find_element(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[4]').click()

        # 主页查看是否发布作业成功
        # 点击主页
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/a[1]/li').click()
        # 已发布作业
        wd.find_element(By.XPATH, '//*[@id="home_div"]/div/div/div[2]/div[1]/div[2]/a/span').click()
        taskname1 = wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody/tr[1]/td[3]')
        CHECK_POINT('是否发布作业成功', taskname == taskname1.text)
        wd.close()

        STEP(3, '学生登录系统')
        sclassid, srealname, susername, sphonenumber, sid = getFirstStudent().values()
        s_ui.open_browser()
        s_ui.login(susername)
        wd = s_ui.wd
        wd.switch_to.window(wd.window_handles[-1])
        # 点击 消息
        wd.find_element(By.CSS_SELECTOR, 'li.dropdown > a > i.fa-tasks').click()
        # 点击 查看所有任务
        wd.find_element(By.CSS_SELECTOR, 'li.last').click()

        # 点击 去做
        wd.find_element(By.CSS_SELECTOR, 'table.table td:last-child > button').click()
        # 默认全都点击 C
        c_eles = wd.find_elements(By.XPATH, '//div//button[3]')
        for e in c_eles:
            e.click()
        # 点击 提交
        wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[3]/button').click()
        # 点击 确定
        wd.find_element(By.CSS_SELECTOR, 'div.bootstrap-dialog-footer-buttons > button:last-child').click()
        # 执行 JavaScript 来点击页面的某个位置
        wd.execute_script("document.elementFromPoint(100, 100).click();")
        # 获取信息：正确率
        acc_element = wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[1]/div[2]/span[2]')
        acc_text = acc_element.text
        acc = float(acc_text[4:-1].strip()) / 100
        wd.close()

        STEP(4, '老师登录系统')
        t_ui.open_browser()
        t_ui.login(username)
        wd = t_ui.wd
        # 点击 “已发布作业”
        wd.find_element(By.CSS_SELECTOR, 'span.badge-blue').click()
        # 点击 完成情况
        wd.find_element(By.CSS_SELECTOR, 'table.table td:nth-child(5)').click()
        sleep(0.5)
        # 获取信息
        mes_teacher = wd.find_element(By.CSS_SELECTOR, 'table td:nth-child(3) > p').text
        acc1 = float(mes_teacher.split('%')[0][3:]) / 100
        wd.close()
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
        # 点击作业
        wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 创建作业
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()

        input = wd.find_element(By.XPATH, '//*[@id="exam_name_text"]')
        taskname = ''
        input.send_keys(taskname)
        # 点击 确定添加
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(0.5)
        mes = wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        CHECK_POINT('弹窗消息是否正确', mes == '请输入作业名称')

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
        wd = t_ui.wd

        STEP(2, '发布作业，作业名称为1个符串')
        # 点击作业
        wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 创建作业
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()

        input = wd.find_element(By.XPATH, '//*[@id="exam_name_text"]')
        taskname = 'z'
        input.send_keys(taskname)
        wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        sleep(2)
        # 切换窗口iframe，选择题目的小窗口
        wd.switch_to.frame("pick_questions_frame")
        ############
        # 检查是否能够找到某个 iframe 中的元素（例如一个按钮）
        options = wd.find_elements(By.CSS_SELECTOR, '.div-search-question-button-bar label:nth-child(2)')
        for i in range(3):
            options[i].click()
        # 点击确定
        wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(1)

        # 切换窗口：点击确认添加  按钮
        window1 = wd.current_window_handle
        wd.switch_to.window(window1)
        # 确认添加
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(2)

        # 切换窗口：弹框“新建作业成功”，点击发布给学生
        window2 = wd.current_window_handle
        wd.switch_to.window(window2)
        mes11 = wd.find_element(By.CSS_SELECTOR, 'div.bootstrap-dialog-message h3').text
        CHECK_POINT('是否新建作业成功', '新建作业成功' == mes11)

        # 弹框点击  将作业发布给学生，不能直接定位id，id是自动生成的
        wd.find_element(By.XPATH, '//button[text()="发布给学生"]').click()


        # 切换窗口：
        window3 = wd.current_window_handle
        wd.switch_to.window(window3)

        # 点击 发布给学生
        wd.find_element(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[4]').click()
        sleep(1)

        # 设置主窗口
        mainWindow = wd.current_window_handle
        # 切换至新窗口
        # 所有窗口的句柄
        allHandles = wd.window_handles
        # 进入新窗口
        wd.switch_to.window(allHandles[-1])
        sleep(1)

        # 全选
        wd.find_element(By.CSS_SELECTOR, "a.ng-scope").click()
        # wd.find_element(By.XPATH, "//a[contains(text(), '全选')]").click()
        # 点击  确定下发
        wd.find_element(By.XPATH, '/html/body/div/div[2]/h3/button').click()
        # 点击 确定
        wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[3]/button[2]').click()
        # 提示窗口 点击 确定
        wd.find_element(By.XPATH, '(//button[text()="确定"])[2]').click()

        # 切换页面
        wd.switch_to.window(mainWindow)

        # 主页查看是否发布作业成功
        # 点击作业
        wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 点击 已发布作业
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[4]/li/span').click()
        # 获取 已发布作业名称
        taskname1 = wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody/tr/td[3]').text
        CHECK_POINT('作业名是否正确', taskname == taskname1)


class Case_tc005104:
    name = '老师发布作业4-API-tc005104'

    def teststeps(self):
        STEP(1, '老师登录系统')
        # {'username': 'sunny', 'teachclasslist': [20247], 'realname': '孙四', 'id': 5214, 'phonenumber': '13451812456', 'email': 'sunny@163.com', 'idcardnumber': '3208251983080987799'}
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = getFirstTeacher().values()
        t_ui.open_browser()
        t_ui.login(username)

        STEP(2, '发布作业，作业名称为100个符串')
        wd = t_ui.wd
        # 点击作业
        wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 创建作业
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()

        input = wd.find_element(By.XPATH, '//*[@id="exam_name_text"]')
        taskname = generate_mixed_string()
        input.send_keys(taskname)
        wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        sleep(2)
        # 切换窗口iframe，选择题目的小窗口
        wd.switch_to.frame("pick_questions_frame")
        ############
        # 检查是否能够找到某个 iframe 中的元素（例如一个按钮）
        options = wd.find_elements(By.CSS_SELECTOR, '.div-search-question-button-bar label:nth-child(2)')
        for i in range(3):
            options[i].click()
        # 点击确定
        wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(1)

        # 切换窗口：点击确认添加  按钮
        window1 = wd.current_window_handle
        wd.switch_to.window(window1)
        # 确认添加
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(2)

        # 切换窗口：弹框“新建作业成功”，点击发布给学生
        window2 = wd.current_window_handle
        wd.switch_to.window(window2)
        mes11 = wd.find_element(By.CSS_SELECTOR, 'div.bootstrap-dialog-message h3').text
        CHECK_POINT('是否新建作业成功', '新建作业成功' == mes11)

        # 弹框点击  将作业发布给学生，不能直接定位id，id是自动生成的
        wd.find_element(By.XPATH, '//button[text()="发布给学生"]').click()

        # 切换窗口：
        window3 = wd.current_window_handle
        wd.switch_to.window(window3)

        # 点击 发布给学生
        wd.find_element(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[4]').click()
        sleep(1)

        # 设置主窗口
        mainWindow = wd.current_window_handle
        # 切换至新窗口
        # 所有窗口的句柄
        allHandles = wd.window_handles
        # 进入新窗口
        wd.switch_to.window(allHandles[-1])
        sleep(1)

        # 全选
        wd.find_element(By.CSS_SELECTOR, "a.ng-scope").click()
        # wd.find_element(By.XPATH, "//a[contains(text(), '全选')]").click()
        # 点击  确定下发
        wd.find_element(By.XPATH, '/html/body/div/div[2]/h3/button').click()
        # 点击 确定
        wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[3]/button[2]').click()
        # 提示窗口 点击 确定
        wd.find_element(By.XPATH, '(//button[text()="确定"])[2]').click()

        # 切换页面
        wd.switch_to.window(mainWindow)
        STEP(3, '查看是否发布作业成功')
        # 主页查看是否发布作业成功
        # 点击作业
        wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 点击 已发布作业
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[4]/li/span').click()
        # 获取 已发布作业名称
        taskname1 = wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody/tr/td[3]').text
        CHECK_POINT('作业名是否正确', taskname == taskname1)
