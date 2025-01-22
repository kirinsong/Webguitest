import pytest
from datetime import datetime
from pages.test_module.resource_page import ResourcePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.test
class TestResource:
    def test_create_repository(self, driver, config):
        """测试创建新的Repository"""
        resource_page = ResourcePage(driver)
        resource_page.navigate_to()
        
        # 创建Repository
        resource_page.create_repository()
        
        # 验证Repository创建成功
        assert resource_page.is_repository_created(), "Repository was not created successfully"
    
    def test_repository_list_display(self, driver, config):
        """测试Repository列表显示"""
        resource_page = ResourcePage(driver)
        resource_page.navigate_to()
        
        # 验证卡片列表是否正确加载
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(resource_page.REPO_CARD)
        )
        
        # 获取所有Repository卡片
        repo_cards = driver.find_elements(*resource_page.REPO_CARD)
        assert len(repo_cards) > 0, "Repository list should not be empty"
        
        # 验证页面标题
        title = driver.find_element(By.XPATH, "//h1[text()='Repository List']")
        assert title.is_displayed(), "Repository List title should be displayed" 
    
    def test_create_and_delete_repository(self, driver, config):
        """测试创建和删除Repository"""
        resource_page = ResourcePage(driver)
        resource_page.navigate_to()
        
        # 创建Repository
        resource_page.create_repository()
        
        # 验证创建成功
        assert resource_page.is_repository_created(), "Repository was not created successfully"
        
        # 删除Repository
        resource_page.delete_repository()
        
        # 验证删除成功
        assert not resource_page.is_repository_created(), "Repository was not deleted successfully" 
    
    def test_sync_repository(self, driver, config):
        """测试同步Repository"""
        resource_page = ResourcePage(driver)
        resource_page.navigate_to()
        
        # 同步Repository
        resource_page.sync_repository()
        
        # 验证同步成功
        # 这里我们通过成功消息来验证，该方法已经在sync_repository中实现 