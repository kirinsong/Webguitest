from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from datetime import datetime
import time
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BenchPage(BasePage):
    # Bench页面URL
    BENCH_URL = "http://172.16.20.170:18080/autogo2024/#/lab/labManagement/bench"
    CREATE_URL = "http://172.16.20.170:18080/autogo2024/#/lab/labManagement/bench/create"
    
    # 页面元素定位器
    CREATE_BTN = (By.XPATH, "//span[text()='Create']")
    NAME_INPUT = (By.ID, "name_input")
    
    # Component Type相关元素
    COMPONENT_TYPE_INPUT = (By.XPATH, "//*[@id='componentType_input']/div/span/input")
    CLU43_OPTION = (By.XPATH, "//*[@id='arco-cascader-popup-0']/div/div/div/ul/li[2]/div")
    PPE_OPTION = (By.XPATH, "//*[@id='arco-cascader-popup-0']/div/div[2]/div/ul/li[1]/div")
    Q6_ETRON_OPTION = (By.XPATH, "//*[@id='arco-cascader-popup-0']/div/div[3]/div/ul/li[1]/div")
    CN_OPTION = (By.XPATH, "//*[@id='arco-cascader-popup-0']/div/div[4]/div/ul/li[1]/div")
    ADVANCE_OPTION = (By.XPATH, "//*[@id='arco-cascader-popup-0']/div/div[5]/div/ul/li[1]/div")
    
    # 其他输入字段
    VIN_INPUT = (By.XPATH, "//*[@id='vin_code_input']")
    ARRIVE_DATE_INPUT = (By.XPATH, "//*[@id='arrive_date']/div/div/div[1]/input")
    RETURN_DATE_INPUT = (By.XPATH, "//*[@id='return_date']/div/div/div[1]/input")
    SPECIFIC_DATE = (By.XPATH, "//div[contains(@class, 'arco-picker-cell')]//div[text()='11' and contains(@class, 'arco-picker-date')]")
    TODAY_BTN = (By.XPATH, "//span[text()='Today']")
    SAVE_BTN = (By.XPATH, "//span[text()='Save']")
    
    # 添加验证相关的定位器
    FIRST_BENCH_NAME = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/p/b")
    
    # 添加转换相关的定位器
    FIRST_BENCH_LINK = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/p/b")
    OPTIONS_BTN = (By.CSS_SELECTOR, "svg.serverLite-DropDownSetGroup")
    OPTIONS_BTN_ALT = (By.XPATH, "//svg[contains(@class, 'serverLite-DropDownSetGroup')]")
    CONVERT_OPTION = (By.XPATH, "//div[contains(@class, 'arco-dropdown-menu')]//span[text()='Convert To Auto bench']")
    BIND_BTN = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div[2]/form/div[2]/div/div[1]/button")
    FIRST_DEVICE_BIND_BTN = (By.XPATH, "//div[contains(@class, 'ScanDeviceListActive___mVOyc')]//button[contains(@class, 'arco-btn')]")
    FIRST_DEVICE_BIND_BTN_ALT = (By.XPATH, "//div[contains(@class, 'ScanDeviceList___vvEYi')]//button[.//span[text()='Bind']]")
    ENABLE_SWITCH = (By.XPATH, "//*[@id='able_input']")
    SAVE_BTN = (By.XPATH, "//span[text()='Save']")
    
    # 添加空白区域的定位器
    BLANK_AREA = (By.XPATH, "//main")
    
    # 添加 auto bench 相关的定位器
    AUTO_BENCH_URL = "http://172.16.20.170:18080/autogo2024/#/lab/labManagement/autoBench"
    SEARCH_INPUT = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div[1]/div/div[1]/div/div/span/span/input")
    AUTO_BENCH_NAME = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[1]/div[1]/div/div/div[1]/b")
    
    # 添加 issue 相关的定位器
    CREATE_ISSUE_BTN = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div/div[2]/div[4]/div/div/div[1]/div[2]/button/span")
    
    # Issue 表单元素
    EQUIPMENT_SELECT = (By.XPATH, "//*[@id='equipment_input']/div/span/span[1]")
    EQUIPMENT_FIRST_OPTION = (By.XPATH, "//li[contains(@class, 'arco-select-option')][1]")
    IP_INPUT = (By.XPATH, "//*[@id='ip_input']")
    ERROR_CODE_SELECT = (By.XPATH, "//*[@id='error_code_id_input']/div/span/span[1]")
    ERROR_CODE_FIRST_OPTION = (By.XPATH, "//li[contains(@class, 'arco-select-option')][1]")
    DESCRIPTION_INPUT = (By.XPATH, "//*[@id='description_input']")
    SAVE_ISSUE_BTN = (By.XPATH, "//button[contains(@class, 'serverLite-Button-Bg333752')]//span[text()='Save']")
    CONFIRM_YES_BTN = (By.XPATH, "//div[contains(@class, 'arco-modal-footer')]//span[text()='Yes']")
    
    # 添加 Auto Bench 详情页相关的定位器
    AUTO_BENCH_DETAIL_LINK = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[1]/b")
    
    # 备用定位器
    SAVE_ISSUE_BTN_ALT = (By.CSS_SELECTOR, "button.serverLite-Button-Bg333752 span")
    
    # 添加 issue 关闭相关的定位器
    ISSUE_LIST = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div/div[2]/div[4]/div/div/div[2]/div/div/div/div/div/table/tbody")
    FIRST_ISSUE_DESC = (By.XPATH, "//*[@id='root']/section/section/section/main/div/div/div[2]/div[4]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[7]/div/span")
    
    # Issue 编辑表单元素
    STATUS_SELECT = (By.XPATH, "//*[@id='status_input']/div/span/span")
    STATUS_CLOSE_OPTION = (By.XPATH, "//li[@role='option' and text()='Close']")
    STATUS_CLOSE_OPTION_ALT = (By.CSS_SELECTOR, "li.arco-select-option:first-child")
    CLOSE_REASON_INPUT = (By.XPATH, "//*[@id='comment_input']")
    SAVE_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'serverLite-Button-Bg333752')]//span[text()='Save']")
    
    def navigate_to(self):
        """导航到Bench页面"""
        self.driver.get(self.BENCH_URL)
        self.logger.info("Navigated to Bench page")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CREATE_BTN)
        )
    
    def create_manual_bench(self):
        """创建manual bench"""
        try:
            # 1. 点击Create按钮
            self.click(*self.CREATE_BTN)
            self.logger.info("Clicked Create button")
            
            # 等待页面加载
            time.sleep(2)
            
            # 2. 输入Name
            random_letters = ''.join(random.choices(string.ascii_lowercase, k=4))
            bench_name = f"manual bench {random_letters}"
            self.input_text(*self.NAME_INPUT, bench_name)
            self.logger.info(f"Input bench name: {bench_name}")
            
            # 3. 选择Component Type
            self.click(*self.COMPONENT_TYPE_INPUT)
            time.sleep(1)
            
            # 依次点击选项
            self.click(*self.CLU43_OPTION)
            time.sleep(0.5)
            self.click(*self.PPE_OPTION)
            time.sleep(0.5)
            self.click(*self.Q6_ETRON_OPTION)
            time.sleep(0.5)
            self.click(*self.CN_OPTION)
            time.sleep(0.5)
            self.click(*self.ADVANCE_OPTION)
            self.logger.info("Selected component type")
            
            # 4. 输入VIN
            vin_code = "TEST" + datetime.now().strftime('%Y%m%d%H%M%S')
            self.input_text(*self.VIN_INPUT, vin_code)
            self.logger.info(f"Input VIN: {vin_code}")
            
            # 5. 选择Arrive Date
            self.click(*self.ARRIVE_DATE_INPUT)
            time.sleep(1)
            
            # 等待日期选择器出现并选择日期
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.SPECIFIC_DATE)
            )
            self.click(*self.SPECIFIC_DATE)
            self.logger.info("Selected arrive date: 2025-01-11")
            
            # 6. 选择Return Date
            self.click(*self.RETURN_DATE_INPUT)
            time.sleep(1)
            self.click(*self.TODAY_BTN)
            self.logger.info("Selected return date")
            
            # 7. 点击Save
            self.click(*self.SAVE_BTN)
            self.logger.info("Clicked Save button")
            
            # 等待保存完成
            time.sleep(3)
            
            return bench_name
            
        except Exception as e:
            self.logger.error(f"Failed to create manual bench: {str(e)}")
            self.driver.save_screenshot(f"create_bench_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise 
    
    def verify_bench_created(self, bench_name):
        """验证manual bench是否创建成功"""
        try:
            # 等待页面加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.FIRST_BENCH_NAME)
            )
            
            # 获取第一个bench的名称
            first_bench = self.find_element(*self.FIRST_BENCH_NAME)
            actual_name = first_bench.text
            
            # 验证名称是否匹配
            if actual_name == bench_name:
                self.logger.info(f"Successfully verified bench creation: {bench_name}")
                return True
            else:
                self.logger.error(f"Bench name mismatch. Expected: {bench_name}, Actual: {actual_name}")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to verify bench creation: {str(e)}")
            self.driver.save_screenshot(f"verify_bench_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise 
    
    def convert_to_auto_bench(self):
        """将manual bench转换为auto bench"""
        try:
            # 1. 点击第一个bench名称进入详情页
            self.click(*self.FIRST_BENCH_LINK)
            self.logger.info("Entered bench details page")
            time.sleep(2)
            
            # 2. 触发 options 下拉菜单
            try:
                options_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.OPTIONS_BTN)
                )
                self.logger.info("Found options button using CSS selector")
            except:
                options_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.OPTIONS_BTN_ALT)
                )
                self.logger.info("Found options button using alternative XPath")
            
            # 确保元素在视图中
            self.driver.execute_script("arguments[0].scrollIntoView(true);", options_btn)
            time.sleep(1)
            
            # 使用 JavaScript 触发鼠标事件
            self.driver.execute_script("""
                var element = arguments[0];
                var mouseoverEvent = new MouseEvent('mouseover', {
                    'view': window,
                    'bubbles': true,
                    'cancelable': true
                });
                element.dispatchEvent(mouseoverEvent);
                
                var mouseenterEvent = new MouseEvent('mouseenter', {
                    'view': window,
                    'bubbles': true,
                    'cancelable': true
                });
                element.dispatchEvent(mouseenterEvent);
            """, options_btn)
            time.sleep(1)
            
            # 等待并点击Convert选项
            convert_option = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.CONVERT_OPTION)
            )
            convert_option.click()
            self.logger.info("Clicked Convert To Auto bench option")
            
            # 4. 点击Bind按钮
            self.click(*self.BIND_BTN)
            self.logger.info("Clicked Bind button")
            time.sleep(1)
            
            # 5. 选择第一个设备
            try:
                # 等待弹窗加载完成
                time.sleep(2)
                
                # 首先尝试使用精确的 XPath
                bind_device_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.FIRST_DEVICE_BIND_BTN)
                )
                self.logger.info("Found bind button using primary selector")
            except:
                # 如果失败，尝试使用备用定位器
                bind_device_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.FIRST_DEVICE_BIND_BTN_ALT)
                )
                self.logger.info("Found bind button using alternative selector")
            
            # 确保元素可见并可点击
            self.driver.execute_script("arguments[0].scrollIntoView(true);", bind_device_btn)
            time.sleep(1)
            
            # 尝试多种点击方式
            try:
                # 方式1：直接点击
                bind_device_btn.click()
            except:
                try:
                    # 方式2：JavaScript点击
                    self.driver.execute_script("arguments[0].click();", bind_device_btn)
                except:
                    # 方式3：Actions点击
                    ActionChains(self.driver).move_to_element(bind_device_btn).click().perform()
            
            self.logger.info("Selected first device")
            time.sleep(1)
            
            # 点击空白处关闭弹窗
            # blank_area = self.find_element(*self.BLANK_AREA)
            # self.driver.execute_script("arguments[0].click();", blank_area)
            # self.logger.info("Clicked blank area to close dialog")
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            
            # 6. 启用enable开关
            enable_switch = self.find_element(*self.ENABLE_SWITCH)
            if not enable_switch.is_selected():
                enable_switch.click()
                self.logger.info("Enabled auto bench")
            
            # 7. 点击Save按钮
            self.click(*self.SAVE_BTN)
            self.logger.info("Clicked Save button")
            
            # 等待保存完成
            time.sleep(3)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to convert to auto bench: {str(e)}")
            self.driver.save_screenshot(f"convert_bench_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise 
    
    def verify_auto_bench_converted(self, bench_name):
        """验证manual bench是否成功转换为auto bench"""
        try:
            # 1. 导航到auto bench列表页
            self.driver.get(self.AUTO_BENCH_URL)
            self.logger.info("Navigated to Auto Bench page")
            time.sleep(2)
            
            # 2. 等待并点击搜索框
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.SEARCH_INPUT)
            )
            search_input.click()
            
            # 3. 输入bench名称
            search_input.clear()
            search_input.send_keys(bench_name)
            self.logger.info(f"Searching for auto bench: {bench_name}")
            time.sleep(2)  # 等待搜索结果
            
            # 4. 验证搜索结果
            try:
                auto_bench_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.AUTO_BENCH_NAME)
                )
                actual_name = auto_bench_element.text
                
                if actual_name == bench_name:
                    self.logger.info(f"Successfully verified auto bench conversion: {bench_name}")
                    return True
                else:
                    self.logger.error(f"Auto bench name mismatch. Expected: {bench_name}, Actual: {actual_name}")
                    return False
                    
            except Exception as e:
                self.logger.error(f"Auto bench not found: {str(e)}")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to verify auto bench conversion: {str(e)}")
            self.driver.save_screenshot(f"verify_auto_bench_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise
    
    def is_element_visible(self, locator):
        """检查元素是否可见"""
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
    
    def create_issue(self, ip="192.168.1.2", description="this is a test"):
        """创建issue"""
        try:
            # 0. 点击 Auto Bench 名称进入详情页
            auto_bench_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.AUTO_BENCH_DETAIL_LINK)
            )
            auto_bench_link.click()
            self.logger.info("Clicked Auto Bench name to enter detail page")
            time.sleep(2)  # 等待详情页加载
            
            # 1. 点击Create Issue按钮
            self.click(*self.CREATE_ISSUE_BTN)
            self.logger.info("Clicked Create Issue button")
            time.sleep(1)
            
            # 2. 选择Equipment
            self.click(*self.EQUIPMENT_SELECT)
            time.sleep(1)
            self.click(*self.EQUIPMENT_FIRST_OPTION)
            self.logger.info("Selected Equipment: Bench")
            
            # 3. 输入IP
            self.input_text(*self.IP_INPUT, ip)
            self.logger.info(f"Input IP: {ip}")
            
            # 4. 选择Error Code
            self.click(*self.ERROR_CODE_SELECT)
            time.sleep(1)
            self.click(*self.ERROR_CODE_FIRST_OPTION)
            self.logger.info("Selected first Error Code")
            
            # 5. 输入Description
            self.input_text(*self.DESCRIPTION_INPUT, description)
            self.logger.info(f"Input Description: {description}")
            
            # 6. 点击Save按钮
            try:
                # 首先尝试使用主定位器
                save_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.SAVE_ISSUE_BTN)
                )
                save_btn.click()
            except:
                # 如果失败，尝试使用备用定位器
                save_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.SAVE_ISSUE_BTN_ALT)
                )
                save_btn.click()
            
            self.logger.info("Clicked Save button")
            time.sleep(1)
            
            # 7. 点击Yes确认
            self.click(*self.CONFIRM_YES_BTN)
            self.logger.info("Confirmed issue creation")
            
            # 等待操作完成
            time.sleep(2)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to create issue: {str(e)}")
            self.driver.save_screenshot(f"create_issue_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise
    
    def close_issue(self, expected_desc="this is a test", close_reason="Close For Test"):
        """关闭issue"""
        try:
            # 1. 等待 issue 列表加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ISSUE_LIST)
            )
            
            # 2. 获取第一条 issue 的描述
            first_issue_desc = self.get_text(*self.FIRST_ISSUE_DESC)
            self.logger.info(f"Found first issue description: {first_issue_desc}")
            
            # 验证描述是否匹配
            if first_issue_desc != expected_desc:
                raise Exception(f"Issue description mismatch. Expected: {expected_desc}, Actual: {first_issue_desc}")
            
            # 3. 点击第一条 issue
            self.click(*self.FIRST_ISSUE_DESC)
            self.logger.info("Clicked first issue")
            time.sleep(2)
            
            # 4. 点击 Status 下拉框并选择 Close
            self.click(*self.STATUS_SELECT)
            time.sleep(1)
            
            # 尝试多种方式选择 Close 选项
            try:
                # 首先尝试使用主定位器
                close_option = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.STATUS_CLOSE_OPTION)
                )
                close_option.click()
            except:
                # 如果失败，尝试使用备用定位器
                close_option = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.STATUS_CLOSE_OPTION_ALT)
                )
                close_option.click()
            
            self.logger.info("Selected Close status")
            
            # 5. 输入关闭原因
            self.input_text(*self.CLOSE_REASON_INPUT, close_reason)
            self.logger.info(f"Input close reason: {close_reason}")
            
            # 6. 点击 Save 按钮
            try:
                # 首先尝试使用主定位器
                save_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.SAVE_CLOSE_BTN)
                )
                save_btn.click()
            except:
                # 如果失败，尝试使用 JavaScript 点击
                save_btn = self.find_element(*self.SAVE_CLOSE_BTN)
                self.driver.execute_script("arguments[0].click();", save_btn)
            
            self.logger.info("Clicked Save button")
            
            # 等待操作完成
            time.sleep(2)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to close issue: {str(e)}")
            self.driver.save_screenshot(f"close_issue_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise