import pytest
from pages.server_module.user_page import UserPage

class TestUser:
    @pytest.mark.server
    def test_user_operations(self, driver):
        """测试用户添加和删除操作"""
        try:
            # 1. 创建UserPage实例
            user_page = UserPage(driver)
            
            # 2. 导航到用户管理页面
            user_page.navigate_to()
            
            # 3. 添加新用户
            assert user_page.add_user(), "Failed to add new user"
            
            # 4. 删除用户
            assert user_page.delete_first_user(), "Failed to delete user"
            
        except Exception as e:
            pytest.fail(f"Test failed: {str(e)}") 