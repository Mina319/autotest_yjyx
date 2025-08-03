import string
import random
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException


def open_browser():
    INFO('打开浏览器')
    options = webdriver.ChromeOptions()
    os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    #  使用 Hytest 的全局变量 GSTORE，把浏览器实例 wd 存进去，方便其他函数拿来用
    GSTORE['wd'] = wd


def mgr_login():
    wd = GSTORE['wd']
    wd.get('http://127.0.0.1/mgr/sign.html')
    wd.find_element(By.ID, 'username').send_keys('byhy')
    wd.find_element(By.ID, 'password').send_keys('88888888')
    # 点击登录
    (wd.find_element(By.CLASS_NAME, 'btn-flat')).click()


def generate_mixed_string(length=100):
    # 定义字符集
    chinese_chars = [chr(i) for i in range(0x4e00, 0x9fa5 + 1)]  # 常用汉字范围
    english_chars = string.ascii_letters  # 所有英文字母
    special_chars = "*()^&$#%@"  # 特殊字符

    # 组合所有可能的字符
    all_chars = chinese_chars + list(english_chars) + list(special_chars)

    # 随机选择字符直到达到指定长度
    result = []
    for _ in range(length):
        char = random.choice(all_chars)
        result.append(char)

    return ''.join(result)


def get_text_with_retry(driver, by, path, multi=False, max_retries=3, wait_time=1):
    """
    获取页面元素文本（单个或多个），支持重试机制。

    参数:
    driver       : WebDriver对象
    by           : By 类型（如 By.XPATH、By.ID 等）
    path         : 元素定位路径（如 xpath 表达式）
    multi        : 是否获取多个元素，默认 False（即 get_element）
    max_retries  : 最大重试次数
    wait_time    : 每次重试等待时间（秒）

    返回:
    - 如果 multi=False：返回文本字符串 或 None
    - 如果 multi=True：返回文本列表（可能为空列表）
    """
    print(f'\n获取{path}元素的文本：')
    for attempt in range(1, max_retries + 1):
        try:
            if multi:
                # 获取多个元素
                elements = driver.find_elements(by, path)
                if elements:
                    # 获取所有元素的文本，并过滤掉空文本
                    texts = [element.text.strip() for element in elements if element.text.strip()]
                    if texts:
                        print(f"\t第{attempt}次尝试：找到 {len(elements)} 个元素，文本已提取")
                        return texts
                    else:
                        print(f"\t第{attempt}次尝试：未找到任何有效文本，重试中...")
                else:
                    print(f"\t第{attempt}次尝试：未找到任何元素，重试中...")
            else:
                # 获取单个元素
                element = driver.find_element(by, path)
                text = element.text.strip()
                if text:
                    print(f"\t第{attempt}次尝试：成功找到元素，文本已提取")
                    return text
                else:
                    print(f"\t第{attempt}次尝试：找到元素，但文本为空，重试中...")
        except NoSuchElementException:
            print(f"\t第{attempt}次尝试：元素不存在，等待 {wait_time} 秒后重试...")
        except Exception as e:
            print(f"\t第{attempt}次尝试：发生异常：{e}")

        # 重试前等待一段时间
        sleep(wait_time)

    print("所有尝试失败。")
    return [] if multi else None


def get_element_with_retry(driver, by, path, multi=False, max_retries=3, wait_time=1):
    """
    获取页面元素（单个或多个），支持重试机制。

    参数:
    driver       : WebDriver对象
    by           : By 类型（如 By.XPATH、By.ID 等）
    path         : 元素定位路径（如 xpath 表达式）
    multi        : 是否获取多个元素，默认 False（即 find_element）
    max_retries  : 最大重试次数
    wait_time    : 每次重试等待时间（秒）

    返回:
    - 如果 multi=False：返回 WebElement 或 None
    - 如果 multi=True：返回元素列表（可能为空列表）
    """
    print(f'\n寻找{path}元素：')
    for attempt in range(1, max_retries + 1):
        try:
            if multi:
                elements = driver.find_elements(by, path)
                if elements:
                    print(f"\t第{attempt}次尝试：找到 {len(elements)} 个元素")
                    return elements
                else:
                    print(f"\t第{attempt}次尝试：未找到任何元素，重试中...")
            else:
                element = driver.find_element(by, path)
                print(f"\t第{attempt}次尝试：成功找到元素")
                return element
        except NoSuchElementException:
            print(f"\t第{attempt}次尝试：元素不存在，等待 {wait_time} 秒后重试...")
        except Exception as e:
            print(f"\t第{attempt}次尝试：发生异常：{e}")
        sleep(wait_time)

    print("所有尝试失败。")
    return [] if multi else None
