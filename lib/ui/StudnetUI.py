import datetime
import random
import re

from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from cfg.cfg import *
from time import sleep

from lib.webui import get_text_with_retry, get_element_with_retry


class StudentUI:

    def open_browser(self):
        INFO('打开浏览器')
        options = webdriver.ChromeOptions()
        os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # 添加无头模式配置
        # options.add_argument('--headless')  # 启用无头模式
        # options.add_argument('--disable-gpu')  # 禁用 GPU 加速 (在某些系统上有帮助)
        # options.add_argument('--no-sandbox')  # 某些系统可能需要此选项

        self.wd = webdriver.Chrome(options=options)  # 保存为 self.wd
        self.wd.implicitly_wait(10)

    def login(self, username, password='888888'):
        self.wd.get(g_ui_url_student)
        self.wd.find_element(By.ID, 'username').send_keys(username)
        self.wd.find_element(By.ID, 'password').send_keys(password)
        self.wd.find_element(By.ID, 'submit').click()

    def logout(self):
        # 登出
        # 点击 右上角 用户名
        sleep(2)
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div[2]/ul/li[2]/a').click()
        # 点击 退出
        self.wd.find_element(By.CSS_SELECTOR, '.fa-key').click()

    def get_home_infos(self,):
        # 返回页面 捕获的 学校、姓名、已发布微课、已发布作业 的信息
        # 主页页面
        # 等待 school 信息加载
        sleep(1.5)
        infos_ele = self.wd.find_elements(By.XPATH, '//table//td[2]/span')
        infos = [e.text for e in infos_ele]
        name1, school1, parent = infos
        infos_ele1 = self.wd.find_elements(By.XPATH, '//*[@id="icon-choose"]/div[1]//h2//strong')
        infos1 = [int(e.text) for e in infos_ele1]
        microlessons, homework = infos1
        return name1, school1, microlessons, homework

    def forget_pwd(self, username):
        # 点击忘记密码
        self.wd.get(g_ui_url_student)
        sleep(0.5)
        mainWindow = self.wd.current_window_handle
        self.wd.find_element(By.CSS_SELECTOR, '#reg-for li:nth-child(2) > a').click()
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
        self.wd.find_element(By.CSS_SELECTOR, 'li.dropdown:nth-child(2)').click()
        # 点击 个人信息
        self.wd.find_element(By.CSS_SELECTOR, '.fa-user').click()

    def set_pwd(self, orignpwd, newpwd):
        # 账号登录状态  设置新密码newpwd
        self.click_right()

        # 点击 修改密码
        self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div/div[2]/ul/li[3]/a').click()

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
        sleep(0.5)
        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer button').click()
        return mes

    def set_realname(self, new):
        # 账号登录状态  设置新用户名

        self.click_right()
        # 点击 基本信息修改
        self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div/div[2]/ul/li[2]/a').click()

        # 获取 输入框
        input = self.wd.find_element(By.XPATH, '//*[@id="tab_two"]/div/div[2]/form/div[1]/div/div/input')
        # 输入 新姓名
        input.clear()
        input.send_keys(new)

        # 点击确定
        self.wd.find_element(By.XPATH, '//*[@id="tab_two"]/div/div[2]/div/button').click()
        sleep(0.3)
        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer button').click()

        return mes

    def get_right_name(self):
        # 获取主页  右上角 用户名
        sleep(1)
        # tname = self.wd.find_element(By.CSS_SELECTOR, 'ul > li:nth-child(2) .ng-binding').text
        tname = get_text_with_retry(self.wd, By.CSS_SELECTOR, 'ul > li:nth-child(2) .ng-binding')
        return tname

    def click_wrong_answer_database(self):
        # 点击错题库
        # 没有错题时
        self.wd.find_element(By.CSS_SELECTOR, 'div.main-menu a:nth-child(4) > li').click()
        info = self.wd.find_element(By.CSS_SELECTOR, '#page-wrapper > div > div > div.row.ng-scope > div > span').text
        return info

    def set_icon(self):
        # 设置头像
        self.click_right()
        # 点击 修改信息
        self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div/div[2]/ul/li[2]/a').click()
        # 点击 选择图片
        self.wd.find_element(By.XPATH, '//*[@id="tab_two"]/div/div[1]/div/div[1]/figure/a[1]').click()
        # 点击选择的图片
        self.wd.find_elements(By.CSS_SELECTOR, '.pop-ico img')[0].click()
        # 点击确定
        self.wd.find_element(By.XPATH, '//*[@id="tab_two"]/div/div[2]/div/button').click()
        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text

        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()
        return mes

    def submit_view(self, viewtype=None, detai=None, phone=None):
        # 点击 右上角头像
        self.wd.find_element(By.CSS_SELECTOR, 'li.dropdown:nth-child(2)').click()
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
            ele = self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div/div[3]/div/input')
            ele.clear()
            ele.send_keys(phone)

        # 点击 提交
        self.wd.find_element(By.CSS_SELECTOR, '.col-md-2 button').click()
        res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        return res

    def change_class(self, newclass):
        # 更改班级
        # 点击 右上角头像
        self.wd.find_element(By.CSS_SELECTOR, 'li.dropdown:nth-child(2)').click()
        # 点击 更改班级
        self.wd.find_element(By.CSS_SELECTOR, 'ul.pull-right li:nth-child(2) i').click()
        sleep(0.5)
        # 邀请码 输入框
        ele = self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div[1]/div[2]/div[1]/input')
        ele.clear()
        ele.send_keys(newclass)
        # 点击 确定
        self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div[1]/div[2]/div[2]/button').click()
        # 点击 确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button:nth-child(2)').click()
        sleep(0.5)
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        return mes


    def get_menus(self):
        # 获取主页 菜单
        eles = self.wd.find_elements(By.CSS_SELECTOR, '.main-menu li')
        menus = [e.text for e in eles]
        return menus

    def click_message(self):
        # 点击消息

        # self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div[2]/ul/li[1]/a/i').click()
        btn1 = self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div[2]/ul/li[1]/a/i')
        self.wd.execute_script("arguments[0].click();", btn1)
        # 查看所有任务
        # self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div[2]/ul/li[1]/ul/li[3]/a').click()
        btn2 = self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div[2]/ul/li[1]/ul/li[3]/a')
        self.wd.execute_script("arguments[0].click();", btn2)

    def do_homework(self, taskid, num=10, sleeptime=None):
        # 做作业
        # num 完成题目数量
        window1 = self.wd.current_window_handle
        self.click_message()
        allwindows = self.wd.window_handles
        self.wd.switch_to.window(allwindows[-1])

        # task id
        taskids = self.wd.find_elements(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[2]/div/table/tbody/tr/td[1]')
        taskids = [i.text.strip() for i in taskids]
        time = None


        for i, td in enumerate(taskids):
            if td == taskid:
                times = self.wd.find_elements(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[2]/div/table/tbody/tr/td[5]/span')
                time = int(''.join([char for char in times[i].text if char.isdigit()]))
                # dos = self.wd.find_elements(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[2]/div/table/tbody/tr/td[7]/button')
                dos = get_element_with_retry(self.wd, By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[2]/div/table/tbody/tr/td[7]/button', True)
                dos[i].click()  # 点击做任务
                sleep(2)
                break

        # coms = self.wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]/div/div/div')
        coms = get_element_with_retry(self.wd, By.XPATH, '//*[@id="exam_question_list_choice"]/div/div/div', True)
        n = len(coms)
        sleep(1)
        for i in range(n):
            n = random.randint(1, 4)
            # com_btns = self.wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]/div/div/div/div[2]/div/div')
            # com_btns[i].find_element(By.XPATH, f'/button[{n}]').click()
            btn = get_element_with_retry(self.wd, By.XPATH, f'//*[@id="exam_question_list_choice"]/div/div/div[{i+1}]/div[2]/div/div/button[{n}]')
            INFO(f'btn: {btn}')
            SELENIUM_LOG_SCREEN(self.wd, width='100%')
            btn.click()
            sleep(1)
            if i == num - 1:
                break

        if sleeptime is not None:
            sleep(sleeptime*60)

        # 点击提交
        self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[3]/button').click()
        sleep(1)
        mes1 = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text.strip()
        # CHECK_POINT('检查', mes1 == mes)
        # 点击 确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button:nth-child(2)').click()
        sleep(1)
        # 获取当前时间
        current_time = datetime.datetime.now()
        # 格式化时间为 "YYYY-MM-DD HH:MM:SS"
        complete_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        sleep(1)
        # 执行 JavaScript 来点击页面的某个位置
        self.wd.execute_script("document.elementFromPoint(100, 100).click();")
        # 获取信息：正确率
        acc_element = self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[1]/div[2]/span[2]')
        acc_text = acc_element.text
        acc = float(acc_text[4:-1].strip()) / 100
        bingo = self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[1]/div[2]/sapn[2]').text.strip()
        error = self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[1]/div[2]/span[1]').text.strip()
        pattern = re.compile(r'\d+')
        # 提取数字
        result1 = pattern.search(bingo)
        result2 = pattern.search(error)
        b, e = None, None
        if result1:
            b = result1.group(0)
        if result2:
            e = result2.group(0)
        INFO(f'正确率:{acc*100}%\t规定完成时间:{time}分钟\t提交时间:{complete_time}\t正确题目个数:{b}\t错误题目个数:{e}')
        return acc, b, e, complete_time, time, mes1


student_ui = StudentUI()
