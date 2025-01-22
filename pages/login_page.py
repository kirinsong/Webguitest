from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # 登录页面元素
    USERNAME_INPUT = (By.ID, "user_id_input")
    PASSWORD_INPUT = (By.ID, "password_input")
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Login']")
    
    # 登录成功后的仪表盘URL
    DASHBOARD_URL = "http://172.16.20.170:18080/autogo2024/#/dashboard/preview/automation"
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://172.16.20.170:18080/autogo2024/#/login_old"
    
    def login(self, username, password):
        """执行登录操作"""
        self.driver.get(self.url)
        self.input_text(*self.USERNAME_INPUT, username)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)
        self.logger.info(f"Logged in with username: {username}")
        
    def is_login_successful(self):
        """验证是否登录成功"""
        try:
            # 等待URL变为仪表盘URL
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url == self.DASHBOARD_URL
            )
            self.logger.info("Login successful, redirected to dashboard")
            return True
        except Exception as e:
            self.logger.error(f"Login verification failed: {str(e)}")
            return False 