from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AttributePage(BasePage):
    # 页面 URL
    ATTRIBUTE_URL = "http://172.16.20.170:18080/autogo2024/#/server/attributeManagement/attributes"
    
    # 页面元素定位器
    ADD_ATTRIBUTE_BTN = (By.XPATH, "//button//span[text()='Add Attribute']")
    
    def navigate_to(self):
        """导航到属性管理页面"""
        self.driver.get(self.ATTRIBUTE_URL)
        self.logger.info("Navigated to Attribute Management page") 