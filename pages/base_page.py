from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import Logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger()
        self.wait = WebDriverWait(self.driver, 10)
    
    def find_element(self, by, value):
        """查找单个元素"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            self.logger.error(f"Element not found with {by}={value}")
            raise e
    
    def find_elements(self, by, value):
        """查找多个元素"""
        try:
            elements = self.wait.until(
                EC.presence_of_all_elements_located((by, value))
            )
            return elements
        except Exception as e:
            self.logger.error(f"Elements not found with {by}={value}")
            raise e
    
    def click(self, by, value):
        """点击���素"""
        element = self.find_element(by, value)
        element.click()
    
    def input_text(self, by, value, text):
        """输入文本"""
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, by, value):
        """获取元素文本"""
        element = self.find_element(by, value)
        return element.text 