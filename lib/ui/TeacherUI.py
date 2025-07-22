import selenium
from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from cfg.cfg import *
from time import sleep


class TeacherUI:

    def open_browser(self):
        INFO('打开浏览器')
        options = webdriver.ChromeOptions()
        os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.wd = webdriver.Chrome(options=options)
        self.wd.implicitly_wait(10)

    def login(self, username, password='888888'):
        # 登录
        self.wd.get(g_ui_url_teacher)
        self.wd.find_element(By.ID, 'username').send_keys(username)
        self.wd.find_element(By.ID, 'password').send_keys(password)
        # 点击登录
        self.wd.find_element(By.ID, 'submit').click()

    def logout(self):
        # 登出
        # 点击 右上角 用户名
        sleep(1)
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/a').click()
        # 点击 退出
        self.wd.find_element(By.CSS_SELECTOR, '.fa-key').click()

    def get_right_name(self):
        # 获取主页  右上角 用户名
        tname = self.wd.find_element(By.CSS_SELECTOR, 'li.dropdown .ng-binding').text
        return tname

    def get_home_infos(self, ):
        # 返回页面 捕获的 学校、姓名、学科、金币、已发布微课、已发布作业数量信息
        # 主页页面
        # 等待 school 信息加载
        sleep(2)
        infos_ele = self.wd.find_elements(By.XPATH, '//table//td[2]/a')
        infos = [e.text for e in infos_ele]
        school1, name1, subject1, goldcoin = infos
        goldcoin = 0 if goldcoin == '' else int(goldcoin)
        sleep(1)
        infos_ele1 = self.wd.find_elements(By.XPATH, '//*[@class="col-md-12"]//a/h2/strong')
        infos1 = [int(e.text) for e in infos_ele1]
        microlessons, homework = infos1
        return school1, name1, subject1, goldcoin, microlessons, homework

    def get_menus(self):
        # 获取主页 菜单
        menus = []
        home = self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/a[1]/li').text
        eles = self.wd.find_elements(By.CSS_SELECTOR, '.main-menu li > a')
        menus.append(home)
        menus += [e.text for e in eles]
        return menus

    def has_students(self):
        # 查看该老师的学生数量，返回{班级名称：学生人数}， 学生总人数
        # 主页页面
        # 点击班级情况
        sleep(0.4)
        res = {}
        self.wd.find_element(By.XPATH, '//*[@class="main-menu"]//li[4]').click()
        # 点击班级学生
        self.wd.find_element(By.XPATH, '//*[@class="main-menu"]//li[4]//li/span').click()
        sleep(0.2)

        # 点击 所有班级
        eles = self.wd.find_elements(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div/div[1]/a')
        for e in eles:
            e.click()

        stuClass = self.wd.find_elements(By.XPATH, "//*[contains(@class, 'fa-home')]/..")
        sClassname = [i.text.strip() for i in stuClass]
        nums = self.wd.find_elements(By.CSS_SELECTOR, '.panel-heading .ng-scope')
        sum1 = 0
        for i, sname in enumerate(sClassname):
            num = int(nums[i].text)
            sum1 += num
            res[sname] = num
        return res, sum1

    def forget_pwd(self, username):
        # 点击忘记密码
        self.wd.get(g_ui_url_teacher)
        sleep(1)
        mainWindow = self.wd.current_window_handle
        self.wd.find_element(By.XPATH, '//*[@id="reg-for"]/ul/li/a').click()
        sleep(0.5)
        # 切换页面
        # 所有窗口的句柄
        allHandles = self.wd.window_handles
        # 进入新窗口
        self.wd.switch_to.window(allHandles[-1])
        self.wd.find_element(By.XPATH, '//dd/input').send_keys(username)
        # 点击 获取手机验证码
        self.wd.find_element(By.CSS_SELECTOR, '.subtijiao input').click()
        # 获取信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.ng-binding').text
        # 关闭当前（忘记密码）窗口
        self.wd.close()
        # 切换回主窗口
        self.wd.switch_to.window(mainWindow)
        return mes

    def click_right(self):
        # 点击个人信息
        # 点击 右上角头像
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/a').click()
        # 点击 个人信息
        self.wd.find_element(By.CSS_SELECTOR, '.fa-user').click()

    def set_pwd(self, orignpwd, newpwd):
        # 账号登录状态  设置新密码newpwd

        self.click_right()

        # 点击 登录密码修改
        self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div[2]/ul/li[3]').click()

        # 获取三个输入框
        inputs = self.wd.find_elements(By.CSS_SELECTOR, 'table.table_password tr input')
        # 输入当前密码
        inputs[0].send_keys(orignpwd)
        # 输入修改密码
        inputs[1].send_keys(newpwd)
        # 确认当前密码
        inputs[2].send_keys(newpwd)
        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, 'table.table_password button').click()

        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text

        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()
        return mes

    def set_realname(self, new):
        # 账号登录状态  设置新用户名

        self.click_right()
        # 点击 基本信息修改
        self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div[2]/ul/li[2]').click()

        # 获取 输入框
        inputs = self.wd.find_elements(By.XPATH, '//tbody/tr/td[2]/div/input')
        # 输入 新姓名
        inputs[0].clear()
        inputs[0].send_keys(new)

        # 点击确定
        self.wd.find_element(By.XPATH, '//tbody/tr[3]/td/div/button').click()
        sleep(0.3)
        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()

        return mes

    def set_icon(self):
        # 设置头像
        self.click_right()
        # 点击 基本信息修改
        self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div[2]/ul/li[2]').click()
        # 点击 选择图片
        self.wd.find_element(By.XPATH, '//figure/a[1]').click()
        # 点击选择的图片
        self.wd.find_elements(By.CSS_SELECTOR, '.pop-ico img')[0].click()
        # 点击确定
        self.wd.find_element(By.XPATH, '//table/tbody/tr[3]/td/div/button').click()
        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text

        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()
        return mes

    def submit_view(self, viewtype=None, detai=None, phone=None):
        # 点击 右上角头像
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/a').click()
        # 点击 意见反馈
        self.wd.find_element(By.CSS_SELECTOR, '.fa-envelope-o').click()
        if viewtype is not None:
            # 选择意见: 操作不方便 系统错误 不能登录 授课信息变更 变更学校 其他
            eles = self.wd.find_elements(By.CSS_SELECTOR, '.col-md-12 label')
            eles[viewtype].click()
        if detai is not None:
            ele = self.wd.find_element(By.CSS_SELECTOR, '.col-md-12 textarea')
            ele.clear()
            ele.send_keys(detai)
        if phone is not None:
            ele = self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div[3]/div/input')
            ele.clear()
            ele.send_keys(phone)

        # 点击 提交
        self.wd.find_element(By.CSS_SELECTOR, '.col-md-2 button').click()
        res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        return res

    def publish_homework(self, taskname='作业1'):
        # 发布作业
        # 点击作业
        self.wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 创建作业
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()
        if taskname is None or taskname.strip() == '':
            # 点击 确定添加
            self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
            sleep(0.5)
            mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
            CHECK_POINT('弹窗消息是否正确', mes == '请输入作业名称')
            return
        input = self.wd.find_element(By.XPATH, '//*[@id="exam_name_text"]')
        input.send_keys(taskname)
        self.wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        sleep(0.5)
        # 切换窗口iframe，选择题目的小窗口
        self.wd.switch_to.frame("pick_questions_frame")
        sleep(1)
        ############
        options = self.wd.find_elements(By.CSS_SELECTOR, '.div-search-question-button-bar label:nth-child(2)')
        # 检查是否能够找到某个 iframe 中的元素（例如一个按钮）
        for i in range(3):
            options[i].click()
        # 点击确定
        self.wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(0.5)

        # 切换窗口：点击确认添加  按钮
        window1 = self.wd.current_window_handle
        self.wd.switch_to.window(window1)
        sleep(0.5)
        # 确认添加
        self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(0.5)

        # 切换窗口：弹框“新建作业成功”，点击发布给学生
        window2 = self.wd.current_window_handle
        self.wd.switch_to.window(window2)
        sleep(1)
        mes11 = self.wd.find_element(By.CSS_SELECTOR, 'div.bootstrap-dialog-message h3').text
        CHECK_POINT('是否新建作业成功', '新建作业成功' == mes11)
        # 弹框点击  将作业发布给学生，不能直接定位id，id是自动生成的
        self.wd.find_element(By.XPATH, '//button[text()="发布给学生"]').click()

        # 设置主窗口
        mainWindow = self.wd.current_window_handle
        # 切换至新窗口
        # 所有窗口的句柄
        allHandles = self.wd.window_handles
        # 进入新窗口
        self.wd.switch_to.window(allHandles[-1])
        sleep(0.5)

        # 全选
        self.wd.find_element(By.CSS_SELECTOR, "a.ng-scope").click()
        # self.wd.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div[1]/a").click()
        # self.wd.find_element(By.XPATH, "//a[contains(text(), '全选')]").click()
        # 点击  确定下发
        self.wd.find_element(By.XPATH, '/html/body/div/div[2]/h3/button').click()
        sleep(0.5)
        # 点击 确定
        self.wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[3]/button[2]').click()
        sleep(0.5)
        # 提示窗口 点击 确定
        self.wd.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div/div/button").click()
        # 切换回主窗口
        self.wd.switch_to.window(mainWindow)
        sleep(0.5)
        # 点击 发布给学生
        self.wd.find_element(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[4]').click()

        # 主页查看是否发布作业成功
        # 点击主页
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/a[1]/li').click()
        # 已发布作业
        self.wd.find_element(By.XPATH, '//*[@id="home_div"]/div/div/div[2]/div[1]/div[2]/a/span').click()
        taskname1 = self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody/tr[1]/td[3]')
        CHECK_POINT('是否发布作业成功', taskname == taskname1.text)
        self.wd.close()

    def create_questions(self, type=None, difflevel=None, knowleadege=None, textbook=None, content=None, video=None,
                         answer=None, desc=None):
        # 创建题目
        # type： 0 选择题， 1 填空题
        # difflevel：0 简单， 1 中等， 2 难
        # knowleadege：选择knowleadege个知识点
        # textbook：[[0, 0, 0]]
        # 0浙教版 1人教版
        # 0七年级 1八年级 2九年级 3高一 4高二 5高三
        # 0上册 1下册
        # content: 题目内容
        # video： 视频
        # answer：[答案个数, [具体答案]]
        # desc: 解释说明

        # 点击 题目
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]').click()
        # 点击 创建题目
        self.wd.find_element(By.CSS_SELECTOR, '.fa-plus-square-o').click()

        if type is not None:
            eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_questiontypes"]/label')
            eles[type].click()

        if difflevel is not None:
            eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_level"]/label')
            eles[difflevel].click()

        if knowleadege is not None:
            # 点击 选择
            self.wd.find_element(By.XPATH, '//*[@id="btn_choose_knowledgetree"]').click()
            # 点击 初中数学左边的三角
            self.wd.find_element(By.XPATH, '//*[@id="ZSD_1_0"]/i').click()

            # 点击 所有章
            self.wd.find_elements(By.CSS_SELECTOR, 'i.jstree-ocl')[1].click()
            self.wd.find_elements(By.CSS_SELECTOR, 'i.jstree-ocl')[2].click()

            div_elements = self.wd.find_elements(By.CSS_SELECTOR, 'a i.jstree-checkbox:nth-child(1)')[4:]
            for i in range(knowleadege):
                div_elements[i].click()

            # 点击 确定
            self.wd.find_element(By.XPATH, '//*[@id="btn_selectTree_ok"]').click()

        if textbook is not None:
            for e in textbook:
                i, j, k = e
                # 点击 增加
                self.wd.find_element(By.XPATH, '//*[@id="nav_item_add"]/a').click()
                eles = self.wd.find_elements(By.XPATH, '//*[@id="dropdown_textbookversions"]/li')
                eles[i].click()  # 选择 浙教版 或 人教版
                nianji = self.wd.find_elements(By.CSS_SELECTOR, '#btn_group_grades_1 label')
                # 强制点击
                self.wd.execute_script("arguments[0].click();", nianji[j])
                cehao = self.wd.find_elements(By.CSS_SELECTOR, '#btn_group_textbookvols_1 label')
                self.wd.execute_script("arguments[0].click();", cehao[k])  # 选择 册号

        if content is not None:
            # 获取输入框
            # 切换到iframe
            mainWindow = self.wd.current_window_handle
            iframe = self.wd.find_element(By.CLASS_NAME, 'ke-edit-iframe')
            self.wd.switch_to.frame(iframe)
            input = self.wd.find_elements(By.CSS_SELECTOR, 'body.ke-content')
            input[0].send_keys(content)
            sleep(0.3)
            self.wd.switch_to.window(mainWindow)

        if video is not None:
            # 点击 选择视频文件
            self.wd.find_element(By.XPATH, '//*[@id="pick_video_files"]').send_keys(r'C:\Users\Administrator\evVedios\333.mp4')

        if answer is not None:
            input = self.wd.find_element(By.XPATH, '//*[@id="Question_AnswerNum_text"]')
            input.clear()
            input.send_keys(answer[0])
            if answer[1][0] is not None and 1 <= answer[0] <= 10:
                if type == 0:
                    # 选择题  点击正确答案
                    eles = self.wd.find_elements(By.XPATH, '//*[@id="question_answers"]/label')
                    if answer[1][0] is not None and len(eles) != 0:
                        # eles[answer[1][0]].click()
                        self.wd.execute_script("arguments[0].click();", eles[answer[1][0]])
                elif type == 1:
                    # 填空题 输入正确答案
                    ele = self.wd.find_elements(By.XPATH, '//*[@id="question_answers"]/input')
                    for i, e in enumerate(ele):
                        e.send_keys(answer[1][i])

        if desc is not None:
            # 获取输入框
            mainWindow = self.wd.current_window_handle
            iframe = self.wd.find_elements(By.CLASS_NAME, 'ke-edit-iframe')[1]
            self.wd.switch_to.frame(iframe)
            input = self.wd.find_elements(By.CSS_SELECTOR, 'body.ke-content')
            input[1].send_keys(desc)
            sleep(0.3)
            self.wd.switch_to.window(mainWindow)

        try:
            # 点击 确定添加
            self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        except Exception as e:
            print(e)

        try:
            res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message h3').text
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
            res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        # 点击 确定
        try:
            self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button:nth-child(3)').click()
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
            self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()

        return res

    def del_questions(self, type, content):
        # 删除 type为提醒，0选择1填空，题目内容为content的 题目

        # 点击题目-搜索题目，
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]').click()
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]/ul/a[2]/li/i').click()
        # 点击 按知识点
        sleep(1)
        self.wd.find_element(By.XPATH, '//*[@id="btn_choose_knowledgetree"]').click()
        # 点击 题目类型
        self.wd.find_elements(By.CSS_SELECTOR, '#btn_group_questiontypes label')[type].click()
        # 点击 我创建的
        self.wd.find_element(By.XPATH, '//*[@id="onlysearchmine"]').click()
        # 查找
        ele = self.wd.find_elements(By.CSS_SELECTOR, '#serach_result_table label:nth-child(3)')
        num = len(ele)
        sleep(0.4)
        cons = self.wd.find_elements(By.CSS_SELECTOR, 'div.div-search-result-one-text')
        for i, c in enumerate(cons):
            if c.text.strip() == content:
                sleep(0.3)
                ele = self.wd.find_elements(By.CSS_SELECTOR, '#serach_result_table label:nth-child(3)')
                ele[i].click()  # 点击删除
                # 确定
                self.wd.find_element(By.CSS_SELECTOR, 'div.bootstrap-dialog-footer-buttons button.btn-primary').click()

        ele = self.wd.find_elements(By.CSS_SELECTOR, '#serach_result_table label:nth-child(3)')
        return len(ele) == num-1

    def get_result_acc(self):
        # 查看学生完成作业情况
        # 点击 “已发布作业”
        self.wd.find_element(By.CSS_SELECTOR, 'span.badge-blue').click()
        # 点击 完成情况
        self.wd.find_element(By.CSS_SELECTOR, 'table.table td:nth-child(5)').click()
        sleep(0.5)
        # 获取信息
        mes_teacher = self.wd.find_element(By.CSS_SELECTOR, 'table td:nth-child(3) > p').text
        acc1 = float(mes_teacher.split('%')[0][3:]) / 100
        self.wd.close()
        return acc1


teacher_ui = TeacherUI()
