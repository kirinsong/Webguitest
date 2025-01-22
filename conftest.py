import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import Config
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

@pytest.fixture(scope="session")
def config():
    return Config()

@pytest.fixture(scope="session")
def login_driver(config):
    """创建一个session级别的已登录浏览器实例"""
    chrome_options = webdriver.ChromeOptions()
    
    # 只保留最基本的配置
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.page_load_strategy = 'eager'
    
    # 禁用日志和自动化提示
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # 使用 ChromeDriver
    # 方式1：自动下载匹配的版本
    service = Service("C:\\Users\\vv\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
    
    # 或者方式2：如果你想指定版本，使用 driver_version
    # service = Service(ChromeDriverManager(driver_version="132.0.6834.83").install())
    
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
    
    # 基本设置
    driver.maximize_window()
    driver.set_page_load_timeout(20)
    driver.implicitly_wait(5)
    
    # 执行登录
    try:
        login_page = LoginPage(driver)
        login_page.login(
            username="qi.song@zd-automotive.cn",
            password="testserver"
        )
        
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != login_page.url
        )
        
    except Exception as e:
        print(f"Login failed: {str(e)}")
        driver.quit()
        raise
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function")
def driver(login_driver):
    """为每个测试用例提供一个已登录的浏览器实例"""
    yield login_driver