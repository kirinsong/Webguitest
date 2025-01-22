from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from datetime import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import allure

class PlanPage(BasePage):
    # Plan页面URL
    PLAN_URL = "http://172.16.20.170:18080/autogo2024/#/test/testObject/Plan"
    
    # 列表页元素
    CREATE_BTN = (By.XPATH, "//span[text()='Create']")
    PLAN_TABLE = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div/div/div/div[2]/div/div/div/div/div/table/tbody')
    PLAN_NAME_CELLS = (By.XPATH, "//td[contains(@class, 'arco-table-td')][3]//span[contains(@class, 'arco-table-cell-wrap-value')]")
    
    # 创建页面元素
    PLAN_NAME_INPUT = (By.ID, "name_input")
    REPOSITORY_SELECT = (By.XPATH, "//span[contains(@class, 'arco-select-view-value-mirror') and text()='please select']")
    REPOSITORY_OPTION = (By.XPATH, "//li[@role='option' and text()='new_testproject']")
    SELECT_ALL_CHECKBOX = (By.XPATH, "//thead//div[contains(@class, 'arco-checkbox')]")
    SAVE_BTN = (By.XPATH, "//span[text()='Save']")
    
    # 更新删除相关的元素定位器
    DELETE_BTN = (By.XPATH, "//button//span[text()='Delete']")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[.//span[text()='Yes']]")
    CHECKBOX_BY_NAME = lambda self, name: (By.XPATH, f"//td[contains(@class, 'arco-table-td')]//span[text()='{name}']/ancestor::tr//label[contains(@class, 'arco-checkbox')]")
    
    # 添加下发相关的元素定位器
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search for ...']")
    RUN_BTN_BY_NAME = lambda self, name: (By.XPATH, f"//td[contains(@class, 'arco-table-td')]//span[text()='{name}']/ancestor::tr//button[contains(@class, 'gatherBtn___eePwx')]")
    RUN_ICON = (By.XPATH, "/html/body/div[1]/section/section/section/main/div/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[9]/div/span/div/button/svg[2]")
    PLAN_ROW_BY_NAME = lambda self, name: (By.XPATH, f"//td[contains(@class, 'arco-table-td')]//span[text()='{name}']/ancestor::tr")
    
    # 更新 run 按钮的定位器
    RUN_BTN = (By.XPATH, "//button[contains(@class, 'gatherBtn___eePwx')]")
    NEXT_BTN = (By.XPATH, "//span[text()='Next']")
    OK_BTN = (By.XPATH, "//span[text()='OK']")
    
    # 添加 Execution Queue 相关的定位器
    EXECUTION_QUEUE_URL = "http://172.16.20.170:18080/autogo2024/#/test/testExecution/queue"
    PLAN_IN_QUEUE = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/p")
    CANCEL_BTN = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/img")
    CONFIRM_YES_BTN = (By.XPATH, "//span[text()='Yes']")
    
    # 添加备用定位器
    PLAN_CARD = (By.CLASS_NAME, "ExectionList___ehGFY")
    PLAN_NAME_IN_QUEUE = lambda self, name: (By.XPATH, f"//div[contains(@class, 'ListInfoTitL___7wfGo')]//p[text()='{name}']")
    CANCEL_BTN_IN_CARD = (By.XPATH, "//img[@src='/autogo2024/images/cancelExecIcon.svg']")
    
    # 更新定位器
    FIRST_ROW_CHECKBOX = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[1]//label[contains(@class, "arco-checkbox")]')
    FIRST_ROW_NAME = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]//span')
    
    def navigate_to(self):
        """导航到Plan页面"""
        self.driver.get(self.PLAN_URL)
        self.logger.info("Navigated to Plan page")
        # 等待Create按钮出现，确认页面加载完成
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CREATE_BTN)
        )
    
    @allure.step("创建新的测试计划: {plan_name}")
    def create_new_plan(self, plan_name):
        """创建新的测试计划"""
        try:
            with allure.step("点击Create按钮"):
                self.logger.info("Attempting to click Create button")
                self.click(*self.CREATE_BTN)
                self.logger.info("Successfully clicked Create button")
            
            with allure.step(f"输入计划名称: {plan_name}"):
                self.logger.info(f"Attempting to input plan name: {plan_name}")
                self.input_text(*self.PLAN_NAME_INPUT, plan_name)
                self.logger.info("Successfully input plan name")
            
            # 选择仓库
            self.logger.info("Attempting to select repository")
            self.click(*self.REPOSITORY_SELECT)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.REPOSITORY_OPTION)
            )
            self.click(*self.REPOSITORY_OPTION)
            self.logger.info("Successfully selected repository")
            
            # 选择仓库后等待一下
            self.logger.info("Waiting after repository selection")
            time.sleep(2)  # 给页面一些时间加载case列表
            
            # 等待并点击全选
            self.logger.info("Waiting for checkbox to be present")
            try:
                checkbox = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.SELECT_ALL_CHECKBOX)
                )
                # 打印当前页面源码，帮助调试
                # self.logger.info("Current page source:")
                # self.logger.info(self.driver.page_source)
                
                # 确保元素可见和可点击
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.SELECT_ALL_CHECKBOX)
                )
                
                # 使用JavaScript点击复选框
                self.driver.execute_script("arguments[0].click();", checkbox)
                self.logger.info("Successfully selected all cases")
            except Exception as e:
                self.logger.error(f"Failed to find or click checkbox: {str(e)}")
                self.driver.save_screenshot("checkbox_error.png")
                raise
            
            # 保存
            self.logger.info("Attempting to save plan")
            self.click(*self.SAVE_BTN)
            self.logger.info("Clicked save button")
            
            # 等待URL变更到Plan列表页面
            self.logger.info("Waiting for navigation to Plan list page")
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be(self.PLAN_URL)
            )
            
            # 给后端更多时间处理保存请求
            time.sleep(5)  # 增加等待时间
            
            # 刷新页面以确保显示最新数据
            self.driver.refresh()
            self.logger.info("Page refreshed after save")
            
            # 等待表格重新加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PLAN_TABLE)
            )
            self.logger.info("Table reloaded successfully")
            
            # 再多等待一下确保数据完全加载
            time.sleep(3)  # 增加等待时间
            
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="create_plan_error",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    def get_plan_list(self):
        """获取计划列表"""
        try:
            # 等待表格加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PLAN_TABLE)
            )
            # 返回所有计划行
            return self.find_elements(*self.PLAN_ROWS)
        except Exception as e:
            self.logger.error(f"Failed to get plan list: {str(e)}")
            return []
    
    def is_plan_created(self, plan_name):
        """验证计划是否创建成功"""
        try:
            # 确保当前在Plan列表页面
            current_url = self.driver.current_url
            if not current_url == self.PLAN_URL:
                self.logger.error(f"Not on Plan list page. Current URL: {current_url}")
                return False
            
            # 等待表格加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PLAN_TABLE)
            )
            
            # 获取第一行的Plan Name（第三列）
            first_plan_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[1]/td[3]//span[contains(@class, 'arco-table-cell-wrap-value')]"))
            )
            
            # 检查第一行的计划名称是否匹配
            if first_plan_name.text == plan_name:
                self.logger.info(f"Found created plan at first row: {plan_name}")
                return True
                
            # 如果不匹配，打印找到的名称用于调试
            self.logger.error(f"Expected plan name: {plan_name}")
            self.logger.error(f"Actual first plan name: {first_plan_name.text}")
            return False
            
        except Exception as e:
            self.logger.error(f"Failed to verify plan creation: {str(e)}")
            self.driver.save_screenshot(f"plan_verification_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            return False 
    
    @allure.step("删除测试计划: {plan_name}")
    def delete_plan(self, plan_name):
        """删除第一行的测试计划"""
        try:
            with allure.step("验证第一行计划名称"):
                first_plan = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.FIRST_ROW_NAME)
                )
                if first_plan.text != plan_name:
                    self.logger.error(f"First plan name mismatch. Expected: {plan_name}, Found: {first_plan.text}")
                    return False
            
            with allure.step("选择第一行复选框"):
                checkbox = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.FIRST_ROW_CHECKBOX)
                )
                self.driver.execute_script("arguments[0].click();", checkbox)
                self.logger.info("Selected first plan checkbox")
                time.sleep(1)
            
            # 3. 点击删除按钮
            delete_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.DELETE_BTN)
            )
            delete_btn.click()
            self.logger.info("Clicked Delete button")
            time.sleep(1)
            
            # 4. 确认删除
            confirm_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN)
            )
            confirm_btn.click()
            self.logger.info("Confirmed deletion")
            time.sleep(2)
            
            return True
            
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="delete_plan_error",
                attachment_type=allure.attachment_type.PNG
            )
            return False
            
    def is_plan_deleted(self, plan_name):
        """验证计划是否已被删除"""
        try:
            # 等待表格加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PLAN_TABLE)
            )
            
            # 获取所有计划名称
            plan_cells = self.find_elements(*self.PLAN_NAME_CELLS)
            
            # 检查计划是否不存在
            for cell in plan_cells:
                if cell.text == plan_name:
                    self.logger.error(f"Plan {plan_name} still exists")
                    return False
                    
            self.logger.info(f"Plan {plan_name} was successfully deleted")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to verify plan deletion: {str(e)}")
            self.driver.save_screenshot(f"verify_deletion_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            return False 
    
    def search_plan(self, plan_name):
        """搜索指定的测试计划"""
        try:
            # 等待搜索框出现
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.SEARCH_INPUT)
            )
            
            # 清空搜索框并输入计划名称
            search_input.clear()
            search_input.send_keys(plan_name)
            self.logger.info(f"Searching for plan: {plan_name}")
            
            # 等待搜索结果加载
            time.sleep(2)
            
            # 验证搜索结果
            try:
                plan_row = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.PLAN_ROW_BY_NAME(plan_name))
                )
                self.logger.info(f"Found plan: {plan_name}")
                return True
            except:
                self.logger.error(f"Plan not found: {plan_name}")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to search plan: {str(e)}")
            self.driver.save_screenshot(f"search_plan_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise
    
    @allure.step("下发测试计划: {plan_name}")
    def run_plan(self, plan_name="Touch py"):
        """下发指定的测试计划"""
        try:
            with allure.step("等待页面加载"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.PLAN_TABLE)
                )
            
            with allure.step(f"搜索计划: {plan_name}"):
                if not self.search_plan(plan_name):
                    raise Exception(f"Plan {plan_name} not found")
            
            with allure.step("点击Run按钮"):
                try:
                    run_btn = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(self.RUN_BTN_BY_NAME(plan_name))
                    )
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", run_btn)
                    time.sleep(1)
                    run_btn.click()
                    self.logger.info("Clicked Run button")
                    time.sleep(2)
                except Exception as e:
                    allure.attach(
                        self.driver.get_screenshot_as_png(),
                        name="run_button_error",
                        attachment_type=allure.attachment_type.PNG
                    )
                    raise
            
            with allure.step("完成执行配置"):
                # 点击 Next
                next_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.NEXT_BTN)
                )
                next_btn.click()
                self.logger.info("Clicked Next button")
                
                # 点击 OK
                ok_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.OK_BTN)
                )
                ok_btn.click()
                self.logger.info("Clicked OK button")
            
            return True
            
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="run_plan_error",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    @allure.step("取消计划执行: {plan_name}")
    def cancel_plan_execution(self, plan_name="Touch py"):
        """取消计划执行"""
        try:
            with allure.step("导航到执行队列页面"):
                self.driver.get(self.EXECUTION_QUEUE_URL)
                self.logger.info("Navigated to Execution Queue page")
            
            with allure.step("等待计划加载"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.PLAN_CARD)
                )
            
            with allure.step(f"查找计划: {plan_name}"):
                try:
                    plan = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located(self.PLAN_IN_QUEUE)
                    )
                except:
                    plan = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located(self.PLAN_NAME_IN_QUEUE(plan_name))
                    )
                self.logger.info(f"Found plan in queue: {plan_name}")
            
            with allure.step("取消执行"):
                # 点击取消按钮
                cancel_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(self.CANCEL_BTN)
                )
                self.driver.execute_script("arguments[0].click();", cancel_btn)
                self.logger.info("Clicked cancel button")
                
                # 确认取消
                yes_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.CONFIRM_YES_BTN)
                )
                yes_btn.click()
                self.logger.info("Confirmed cancellation")
            
            return True
            
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="cancel_execution_error",
                attachment_type=allure.attachment_type.PNG
            )
            raise 