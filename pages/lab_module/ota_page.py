from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

class OtaPage(BasePage):
    # 页面元素定位
    ADD_VERSION_BTN = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div[1]/div[2]/button/span')
    VERSION_INPUT = (By.XPATH, '//*[@id="version_input"]')
    TYPE_DROPDOWN = (By.XPATH, '//*[@id="type_input"]/div/span/span[1]')
    TYPE_FIRST_OPTION = (By.XPATH, "//li[@role='option' and text()='TA']")
    TYPE_FIRST_OPTION_ALT = (By.CSS_SELECTOR, "li.arco-select-option:first-child")
    DATE_INPUT = (By.XPATH, '//*[@id="release_date"]/div/div/div[1]/input')
    TODAY_BTN = (By.XPATH, '/html/body/div[2]/div[2]/div/span/div/div[2]/div[2]/span/div/div[2]/div/span')
    SAVE_BTN = (By.XPATH, '/html/body/div[2]/div[2]/div/span/div/div[2]/div[1]/div/button[2]')

    # 更新验证相关的定位器
    RELEASE_LIST_URL = "http://172.16.20.170:18080/autogo2024/#/lab/otaManagement/releases"
    RELEASE_TABLE = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div[2]/div/div/div/div/div/table/tbody')
    RELEASE_NAME_TEMPLATE = '//*[@id="root"]/section/section/section/main/div/div[2]/div/div/div/div/div/table/tbody/tr[{}]/td[1]/div/span'

    # 添加上传相关的定位器
    RELEASE_NAME_LINK = (By.XPATH, "//span[text()='{}']")  # 使用版本号格式化
    OPTION_BTN = (By.CSS_SELECTOR, "svg.serverLite-DropDownSetGroup")
    UPLOAD_OPTION = (By.XPATH, "/html/body/div[3]/span/div/div/div[2]/div/div/div/div/span")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")

    def verify_version_exists(self, version):
        """验证指定版本是否存在于列表中"""
        try:
            # 等待表格加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.RELEASE_TABLE)
            )
            
            # 获取所有行
            rows = self.driver.find_elements(By.XPATH, f"{self.RELEASE_TABLE[1]}/tr")
            self.logger.info(f"Found {len(rows)} releases in the list")
            
            # 遍历每一行查找匹配的版本号
            for i in range(1, len(rows) + 1):
                name_xpath = self.RELEASE_NAME_TEMPLATE.format(i)
                name = self.driver.find_element(By.XPATH, name_xpath).text
                if name == version:
                    self.logger.info(f"Found matching version: {version} at row {i}")
                    return True
            
            self.logger.error(f"Version {version} not found in the list")
            return False
            
        except Exception as e:
            self.logger.error(f"Failed to verify version: {str(e)}")
            return False

    def add_new_version(self):
        """添加新的OTA版本"""
        try:
            # 1. 点击Add Version按钮
            self.click(*self.ADD_VERSION_BTN)
            self.logger.info("Clicked Add Version button")

            # 2. 输入Version (4位随机数)
            version = str(random.randint(1000, 9999))
            self.input_text(*self.VERSION_INPUT, version)
            self.logger.info(f"Input version: {version}")

            # 3. 选择Type
            self.click(*self.TYPE_DROPDOWN)
            time.sleep(1)  # 等待下拉框展开
            
            # 尝试多种方式选择第一个选项
            try:
                # 首先尝试使用主定位器
                type_option = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.TYPE_FIRST_OPTION)
                )
                type_option.click()
            except:
                # 如果失败，尝试使用备用定位器
                type_option = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.TYPE_FIRST_OPTION_ALT)
                )
                type_option.click()
                
            self.logger.info("Selected Type: TA")

            # 4. 选择日期
            self.click(*self.DATE_INPUT)
            time.sleep(1)  # 等待日期选择器展开
            self.click(*self.TODAY_BTN)
            self.logger.info("Selected today's date")

            # 5. 点击Save按钮
            self.click(*self.SAVE_BTN)
            self.logger.info("Clicked Save button")
            time.sleep(2)  # 等待保存完成
            
            # 6. 验证创建是否成功
            # 重新进入release list页面
            self.driver.get(self.RELEASE_LIST_URL)
            self.logger.info("Navigated to Release List page")
            time.sleep(2)  # 等待页面加载
            
            # 验证版本是否存在
            if self.verify_version_exists(version):
                self.logger.info("Successfully verified new version creation")
                return version
            else:
                self.logger.error("Failed to verify new version creation")
                return None
                
        except Exception as e:
            self.logger.error(f"Failed to add new version: {str(e)}")
            return None

    def upload_ta_file(self, version, file_path="C:\\Users\\vv\\Pictures\\3.jpg"):
        """上传TA文件"""
        try:
            # 1. 点击版本号进入详情页
            version_link = self.RELEASE_NAME_LINK[0], self.RELEASE_NAME_LINK[1].format(version)
            self.click(*version_link)
            self.logger.info(f"Clicked version: {version}")
            time.sleep(2)
            
            # 2. 鼠标悬停在 Option 按钮上
            option_btn = self.find_element(*self.OPTION_BTN)
            actions = ActionChains(self.driver)
            actions.move_to_element(option_btn).perform()
            self.logger.info("Hovered over Option button")
            time.sleep(1)
            
            # 3. 点击 Upload 选项
            self.click(*self.UPLOAD_OPTION)
            self.logger.info("Clicked Upload option")
            time.sleep(1)
            
            # 4. 上传文件
            file_input = self.find_element(*self.FILE_INPUT)
            file_input.send_keys(file_path)
            self.logger.info(f"Selected file: {file_path}")
            time.sleep(2)  # 等待上传完成
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to upload TA file: {str(e)}")
            self.driver.save_screenshot(f"upload_ta_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            return False