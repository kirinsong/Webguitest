import pytest
import allure
from datetime import datetime
from pages.test_module.plan_page import PlanPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature('Test Execution Management')
@pytest.mark.test
class TestExecution:
    @allure.story('Plan Execution Operations')
    @allure.title('Run and Cancel Test Plan Execution')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_execution_operations(self, driver, config):
        """测试计划执行和取消"""
        try:
            with allure.step("创建PlanPage实例"):
                plan_page = PlanPage(driver)
            
            with allure.step("导航到计划管理页面"):
                plan_page.navigate_to()
            
            with allure.step("下发测试计划"):
                assert plan_page.run_plan(), "Failed to run plan"
            
            with allure.step("取消计划执行"):
                assert plan_page.cancel_plan_execution(), "Failed to cancel plan execution"
            
        except Exception as e:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail(f"Test failed: {str(e)}")

    # def test_run_plan(self, driver, config):
    #     """测试下发测试计划"""
    #     plan_page = PlanPage(driver)
        
    #     # 导航到Plan页面
    #     plan_page.navigate_to()
        
    #     # 下发计划
    #     plan_page.run_plan("Touch py")
    
    # def test_cancel_plan(self, driver, config):
    #     """测试取消测试计划"""
    #     plan_page = PlanPage(driver)
        
    #     # 导航到执行队列页面并取消计划
    #     plan_page.cancel_plan_execution("Touch py")
        
    #     # TODO: 添加验证步骤
    #     # 比如验证计划状态是否变为已取消
