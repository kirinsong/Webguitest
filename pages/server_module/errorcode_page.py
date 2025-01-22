from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ErrorCodePage(BasePage):
    # 页面 URL
    ERRORCODE_URL = "http://172.16.20.170:18080/autogo2024/#/server/errorCodeManagement/errorCodes"
    
    # 页面元素定位器
    ADD_ERRORCODE_BTN = (By.XPATH, "//button//span[text()='Add Error Code']")
    
    def navigate_to(self):
        """导航到错误码管理页面"""
        self.driver.get(self.ERRORCODE_URL)
        self.logger.info("Navigated to Error Code Management page") 