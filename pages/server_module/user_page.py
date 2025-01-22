from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import string
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserPage(BasePage):
    # 页面 URL
    USER_URL = "http://172.16.20.170:18080/autogo2024/#/server/system/allUsers"
    
    # 页面元素定位器
    ADD_USER_BTN = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div/div[2]/div[1]/div[2]/button')
    
    # 用户表单元素
    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="firstname_input"]')
    LAST_NAME_INPUT = (By.XPATH, '//*[@id="lastname_input"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="user_id_input"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password_input"]')
    SAVE_BTN = (By.CSS_SELECTOR, "button.deviceSettingSaveBtn___KR8ul")
    
    # 更新验证相关的定位器
    SEARCH_INPUT = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div/div[2]/div[1]/div[1]/div/span/span/input')
    USER_TABLE = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody')
    USER_NAME_TEMPLATE = '//*[@id="root"]/section/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[{}]/td[1]'
    
    # 更新删除相关的定位器
    DELETE_BTN = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[8]/div/span')
    # 使用成功的定位器
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[.//span[text()='Yes']]")  # 保留成功的 Text XPath 方式
    
    def navigate_to(self):
        """导航到用户管理页面"""
        self.driver.get(self.USER_URL)
        self.logger.info("Navigated to User Management page")
        
    def generate_random_letters(self, length=2):
        """生成随机字母"""
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    def generate_random_email(self):
        """生成随机邮箱"""
        username = self.generate_random_letters(5)
        return f"{username}@test.com"
        
    def get_all_user_names(self):
        """获取当前页面所有用户名"""
        try:
            # 1. 等待用户列表加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.USER_TABLE)
            )
            
            # 2. 获取所有行
            rows = self.driver.find_elements(By.XPATH, f"{self.USER_TABLE[1]}/tr")
            
            # 3. 获取每行的用户名
            user_names = []
            for i in range(1, len(rows) + 1):
                name_xpath = self.USER_NAME_TEMPLATE.format(i)
                name = self.driver.find_element(By.XPATH, name_xpath).text
                user_names.append(name)
                
            self.logger.info(f"Found {len(user_names)} users in the list")
            return user_names
            
        except Exception as e:
            self.logger.error(f"Failed to get user names: {str(e)}")
            return []
    
    def verify_user_exists(self, full_name):
        """验证用户是否创建成功"""
        try:
            # 1. 等待搜索框可用并输入
            search_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SEARCH_INPUT)
            )
            search_input.clear()
            self.input_text(*self.SEARCH_INPUT, full_name)
            self.logger.info(f"Searching for user: {full_name}")
            time.sleep(2)  # 等待搜索结果
            
            # 2. 获取所有用户名并验证
            user_names = self.get_all_user_names()
            
            if full_name in user_names:
                self.logger.info(f"Found user with name: {full_name}")
                return True
            else:
                self.logger.error(f"User not found. Expected: {full_name}, Available names: {user_names}")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to verify user: {str(e)}")
            return False
    
    def add_user(self):
        """添加新用户"""
        try:
            # 1. 点击Add User按钮
            self.click(*self.ADD_USER_BTN)
            self.logger.info("Clicked Add User button")
            time.sleep(1)
            
            # 2. 输入First Name (添加等待)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
            )
            first_name = self.generate_random_letters()
            self.input_text(*self.FIRST_NAME_INPUT, first_name)
            self.logger.info(f"Input First Name: {first_name}")
            
            # 3. 输入Last Name
            last_name = self.generate_random_letters()
            self.input_text(*self.LAST_NAME_INPUT, last_name)
            self.logger.info(f"Input Last Name: {last_name}")
            
            # 保存完整用户名
            full_name = f"{first_name} {last_name}"
            
            # 4. 输入Email
            email = self.generate_random_email()
            self.input_text(*self.EMAIL_INPUT, email)
            self.logger.info(f"Input Email: {email}")
            
            # 5. 输入Password
            self.input_text(*self.PASSWORD_INPUT, "testserver")
            self.logger.info("Input Password: testserver")
            
            # 6. 点击Save按钮 (添加等待)
            save_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SAVE_BTN)
            )
            save_btn.click()
            self.logger.info("Clicked Save button")
            time.sleep(2)
            
            # 7. 验证用户是否创建成功
            if self.verify_user_exists(full_name):
                self.logger.info("Successfully verified user creation")
                return True
            else:
                self.logger.error("Failed to verify user creation")
                return False
            
        except Exception as e:
            self.logger.error(f"Failed to add user: {str(e)}")
            return False
    
    def click_confirm_button(self):
        """点击确认按钮"""
        try:
            self.logger.info("Attempting to click confirm button using Text XPath")
            
            # 等待元素出现
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.CONFIRM_DELETE_BTN)
            )
            self.logger.info("Element found")
            
            # 等待元素可点击
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN)
            )
            self.logger.info("Element clickable")
            
            # 使用 JavaScript 点击
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info("Successfully clicked confirm button")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to click confirm button: {str(e)}")
            return False
    
    def delete_first_user(self):
        """删除搜索结果中的第一个用户"""
        try:
            # 1. 点击删除按钮
            delete_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DELETE_BTN)
            )
            delete_btn.click()
            self.logger.info("Clicked Delete button")
            time.sleep(2)  # 增加等待时间
            
            # 2. 确认删除
            if not self.click_confirm_button():
                return False
                
            time.sleep(2)
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to delete user: {str(e)}")
            return False 