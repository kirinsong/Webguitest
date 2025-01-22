from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from datetime import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains

class ResourcePage(BasePage):
    # Resource页面URL
    RESOURCE_URL = "http://172.16.20.170:18080/autogo2024/#/test/testObject/resource"
    
    # Repository List页面元素
    CREATE_REPO_BTN = (By.XPATH, '//*[@id="root"]/section/section/section/main/div/div[1]/div[1]/div[2]/button/span')
    REPO_CARD = (By.XPATH, "//div[contains(@class, 'arco-card-body')]")
    REPO_LIST_TITLE = (By.XPATH, "//h1[text()='Repository List']")
    
    # Add Repository页面元素
    REPO_LINK_INPUT = (By.XPATH, "//input[@placeholder='please enter link...']")
    REPO_NAME_SELECT = (By.XPATH, "//span[contains(@class, 'arco-select-view-value-mirror') and contains(text(), 'Select the repository Name')]")
    REPO_NAME_OPTION = (By.XPATH, "//li[@role='option' and text()='testproject']")
    SAVE_BTN = (By.XPATH, "//span[text()='Save']")
    
    # Repository验证元素
    REPO_NAME_IN_LIST = lambda self, name: (By.XPATH, f"//div[contains(@class, 'titBlock___U395P')]//span[text()='{name}']")
    REPO_CARD = (By.XPATH, "//div[contains(@class, 'arco-card-body')]")
    REPO_CREATED_TIME = lambda self, name: (By.XPATH, f"//div[contains(@class, 'titBlock___U395P')]//span[text()='{name}']/ancestor::div[contains(@class, 'arco-card-body')]//li[contains(.,'Created Time:')]//label")
    
    # 更新删除相关的元素定位器
    REPO_OPTIONS_BY_NAME = lambda self, name: (By.XPATH, f"//div[contains(@class, 'titBlock___U395P')]//span[text()='{name}']/ancestor::div[contains(@class, 'titBlock___U395P')]//svg[contains(@class, 'serverLite-DropDownSetGroup')]")
    DELETE_OPTION = (By.XPATH, "//span[text()='Delete']")
    CONFIRM_YES_BTN = (By.XPATH, "//div[contains(@class, 'arco-modal')]//span[text()='Yes']")
    
    # 更新定位器
    REPO_CARD_BY_NAME = lambda self, name: (By.XPATH, f"//div[contains(@class, 'arco-card-body')]//span[text()='{name}']/ancestor::div[contains(@class, 'arco-card-body')]")
    OPTIONS_BTN_IN_CARD = (By.XPATH, ".//p[contains(@class, 'serverLite-cursorPointer') and contains(.,'Sync')]/following-sibling::svg[contains(@class, 'serverLite-DropDownSetGroup')]")
    
    # 更新 Sync 相关的定位器
    SYNC_BTN_BY_NAME = lambda self, name: (By.XPATH, f"//div[contains(@class, 'titBlock___U395P')]//span[text()='{name}']/ancestor::div[contains(@class, 'arco-card-body')]//p[contains(@class, 'serverLite-cursorPointer')]//img[@src='/autogo2024/images/refresh.svg']/..")
    START_SYNC_BTN = (By.XPATH, "//button[contains(@class, 'serverLite-Button-Bg333752')]//span[text()='Start Sync Resource']")
    
    def navigate_to(self):
        """导航到Resource页面"""
        self.driver.get(self.RESOURCE_URL)
        self.logger.info("Navigated to Resource page")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CREATE_REPO_BTN)
        )
    
    def create_repository(self, link="git@172.16.20.230:/git/testproject", name="testproject"):
        """创建新的Repository"""
        try:
            # 先检查是否已存在
            if self.is_repository_created(name):
                self.logger.info(f"Repository {name} already exists, skipping creation")
                return True
            
            # 点击Create Repository按钮
            self.click(*self.CREATE_REPO_BTN)
            self.logger.info("Clicked Create Repository button")
            
            # 等待Add Repository对话框加载
            time.sleep(2)
            
            # 尝试多种方式输入链接
            try:
                # 方法1：直接输入
                link_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.REPO_LINK_INPUT)
                )
                link_input.click()
                link_input.clear()
                link_input.send_keys(link)
                
                # 验证输入
                actual_value = link_input.get_attribute('value')
                if actual_value != link:
                    raise ValueError(f"Input verification failed. Expected: {link}, Actual: {actual_value}")
                
                self.logger.info(f"Successfully input repository link: {link}")
                
            except Exception as e:
                self.logger.error(f"Failed to input repository link: {str(e)}")
                self.driver.save_screenshot(f"input_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
                raise
            
            # 等待一下确保输入完成
            time.sleep(1)
            
            # 选择Repository Name
            self.click(*self.REPO_NAME_SELECT)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.REPO_NAME_OPTION)
            )
            self.click(*self.REPO_NAME_OPTION)
            self.logger.info(f"Selected repository name: {name}")
            
            # 保存
            self.click(*self.SAVE_BTN)
            self.logger.info("Clicked Save button")
            
            # 增加等待时间确保保存完成
            time.sleep(5)
            
            # 刷新页面确保数据更新
            self.driver.refresh()
            self.logger.info("Page refreshed")
            
            # 等待页面重新加载完成
            time.sleep(3)
            
            # 等待卡片列表加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.REPO_CARD)
            )
            self.logger.info("Repository list reloaded")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to create repository: {str(e)}")
            self.driver.save_screenshot(f"create_repo_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise
    
    def is_repository_created(self, name="testproject"):
        """验证Repository是否创建成功"""
        try:
            # 多次尝试查找Repository（最多尝试3次
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    # 等待卡片列表加载
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(self.REPO_CARD)
                    )
                    
                    # 查找指定名称的Repository
                    repo = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(self.REPO_NAME_IN_LIST(name))
                    )
                    
                    self.logger.info(f"Found repository: {name}")
                    return True
                    
                except Exception as e:
                    if attempt < max_attempts - 1:  # 如果不是最后一次尝试
                        self.logger.warning(f"Attempt {attempt + 1} failed, retrying...")
                        time.sleep(2)  # 等待2秒后重试
                        self.driver.refresh()  # 刷新页面
                        continue
                    else:
                        raise  # 最后一次尝试失败，抛出异常
            
        except Exception as e:
            self.logger.error(f"Repository {name} not found after {max_attempts} attempts: {str(e)}")
            self.driver.save_screenshot(f"verify_repo_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            return False 
    
    def delete_repository(self, name="testproject"):
        """删除指定的Repository"""
        try:
            # 等待卡片列表加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.REPO_CARD)
            )
            
            # 找到指定名称的仓库卡片
            repo_card = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.REPO_CARD_BY_NAME(name))
            )
            self.logger.info(f"Found repository card: {name}")
            
            # 找到 options 按钮
            options_btn = repo_card.find_element(By.CSS_SELECTOR, "svg.serverLite-DropDownSetGroup")
            self.logger.info("Found options button")
            
            # 使用 JavaScript 触发鼠标悬停事件
            self.driver.execute_script("""
                var element = arguments[0];
                var mouseoverEvent = new MouseEvent('mouseover', {
                    'view': window,
                    'bubbles': true,
                    'cancelable': true
                });
                element.dispatchEvent(mouseoverEvent);
            """, options_btn)
            
            # 等待下拉菜单出现
            time.sleep(1)
            
            # 使用 JavaScript 查找并点击 Delete 选项
            delete_clicked = self.driver.execute_script("""
                // 等待下拉菜单出现
                var dropdownMenu = document.querySelector('.arco-dropdown-menu');
                if (!dropdownMenu) return false;
                
                // 查找 Delete 选项
                var items = dropdownMenu.querySelectorAll('.arco-dropdown-menu-item');
                var deleteItem = Array.from(items).find(item => item.textContent.trim() === 'Delete');
                
                if (deleteItem) {
                    deleteItem.click();
                    return true;
                }
                return false;
            """)
            
            if not delete_clicked:
                # 如果上面的方法失败，尝试直接点击
                try:
                    # 先移动到 options 按钮
                    actions = ActionChains(self.driver)
                    actions.move_to_element(options_btn).perform()
                    time.sleep(1)
                    
                    # 等待并点击 Delete 选项
                    delete_btn = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".arco-dropdown-menu-item span"))
                    )
                    delete_btn.click()
                    delete_clicked = True
                except Exception as e:
                    self.logger.error(f"Failed to click Delete option: {str(e)}")
                    
                    # 打印调试信息
                    menu_items = self.driver.execute_script("""
                        var items = document.querySelectorAll('.arco-dropdown-menu-item');
                        return Array.from(items).map(item => ({
                            text: item.textContent,
                            visible: item.offsetParent !== null,
                            rect: item.getBoundingClientRect()
                        }));
                    """)
                    self.logger.info(f"Menu items: {menu_items}")
            
            if not delete_clicked:
                raise Exception("Could not find or click Delete option")
            
            self.logger.info("Clicked Delete option")
            
            # 等待确认对话框出现并点击Yes
            try:
                # 增加等待时间，确保对话框完全显示
                time.sleep(1)
                
                # 使用多种方式尝试点击 Yes 按钮
                try:
                    # 方法1：使用 WebDriverWait
                    yes_btn = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'arco-modal')]//span[text()='Yes']"))
                    )
                    yes_btn.click()
                except:
                    # 方法2：使用 JavaScript
                    self.driver.execute_script("""
                        var yesBtn = document.evaluate(
                            "//div[contains(@class, 'arco-modal')]//span[text()='Yes']",
                            document,
                            null,
                            XPathResult.FIRST_ORDERED_NODE_TYPE,
                            null
                        ).singleNodeValue;
                        if (yesBtn) {
                            yesBtn.click();
                        } else {
                            throw new Error("Yes button not found");
                        }
                    """)
                
                self.logger.info("Clicked Yes button in confirmation dialog")
                
                # 等待删除操作完成
                time.sleep(3)
                
                # 刷新页面
                self.driver.refresh()
                self.logger.info("Page refreshed after deletion")
                
                # 验证删除成功
                try:
                    WebDriverWait(self.driver, 5).until_not(
                        EC.presence_of_element_located(self.REPO_CARD_BY_NAME(name))
                    )
                    self.logger.info(f"Repository {name} was successfully deleted")
                    return True
                except:
                    self.logger.error(f"Repository {name} still exists after deletion")
                    return False
                
            except Exception as e:
                self.logger.error(f"Failed to confirm deletion: {str(e)}")
                # 添加调试信息
                modal_info = self.driver.execute_script("""
                    var modal = document.querySelector('.arco-modal');
                    if (modal) {
                        return {
                            visible: modal.offsetParent !== null,
                            content: modal.textContent,
                            buttons: Array.from(modal.querySelectorAll('button, span')).map(el => ({
                                text: el.textContent,
                                visible: el.offsetParent !== null
                            }))
                        };
                    }
                    return null;
                """)
                self.logger.info(f"Modal dialog info: {modal_info}")
                raise
                
        except Exception as e:
            self.logger.error(f"Failed to delete repository: {str(e)}")
            self.driver.save_screenshot(f"delete_repo_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise 
    
    def sync_repository(self, name="new_testproject"):
        """同步指定的Repository"""
        try:
            # 等待卡片列表加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.REPO_CARD)
            )
            
            # 找到指定仓库的 Sync 按钮
            sync_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.SYNC_BTN_BY_NAME(name))
            )
            self.logger.info(f"Found sync button for repository: {name}")
            
            # 点击 Sync 按钮
            sync_btn.click()
            self.logger.info("Clicked sync button")
            
            # 等待 Start Sync Resource 按钮出现并点击
            start_sync_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.START_SYNC_BTN)
            )
            start_sync_btn.click()
            self.logger.info("Clicked Start Sync Resource button")
            
            # 等待按钮变为不可点击状态（同步开始）
            WebDriverWait(self.driver, 10).until_not(
                EC.element_to_be_clickable(self.START_SYNC_BTN)
            )
            self.logger.info("Sync process started")
            
            # 等待按钮重新变为可点击状态（同步完成）
            WebDriverWait(self.driver, 300).until(  # 设置较长的超时时间，因为同步可能需要较长时间
                EC.element_to_be_clickable(self.START_SYNC_BTN)
            )
            self.logger.info("Sync process completed")
            
            # 刷新页面
            self.driver.refresh()
            self.logger.info("Page refreshed after sync")
            
            # 等待页面重新加载
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.REPO_CARD)
            )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to sync repository: {str(e)}")
            self.driver.save_screenshot(f"sync_repo_error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
            raise 



