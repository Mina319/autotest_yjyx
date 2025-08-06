
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '12',  # 手机安卓版本，如果是鸿蒙系统，依次尝试 12、11、10 这些版本号
    'deviceName': 'HA19CUMG',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.yjyxapp',  # 启动APP Package名称
    'appActivity': '.MainActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 自动化需要输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    # 'noReset': True,  # 不要重置App
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2',
    # 'chromeOptions': {'w3c': False},
    # 'chromedriverExecutable': r'D:\tools\chromedriver_win32_99.0.4844.51\chromedriver.exe',
}
app_server_url = 'http://localhost:4723/wd/hub'


g_vcode = "00000004074389951477"

g_api_server = "http://127.0.0.1"
g_api_url_class = g_api_server + "/api/3school/school_classes"
g_api_url_teacher = g_api_server + "/api/3school/teachers"
g_api_url_student = g_api_server + "/api/3school/students"

# ui
g_ui_url_teacher = g_api_server + "/teacher/login/login.html"
g_ui_url_student = g_api_server + "/student/login/login.html"

g_school = '白月学院00002'

# 年级对应的ID
gradeToId = {
    "七年级": 1,
    "八年级": 2,
    "九年级": 3,
    "高一": 4,
    "高二": 5,
    "高三": 6,
}

# 系统中的学科对应ID
subjectToId = {
    "初中数学": 1,
    "初中科学": 5,
    "初中英语": 11,
    "初中体育": 12,
    "高中语文": 13,
    "高中数学": 14,
}
