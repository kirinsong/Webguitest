from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfigPage(BasePage):
    # 页面 URL
    CONFIG_URL = "http://172.16.20.170:18080/autogo2024/#/server/configManagement/configs"
    
    # 页面元素定位器
    ADD_CONFIG_BTN = (By.XPATH, "//button//span[text()='Add Config']")
    
    def navigate_to(self):
        """导航到配置管理页面"""
        self.driver.get(self.CONFIG_URL)
        self.logger.info("Navigated to Config Management page") 