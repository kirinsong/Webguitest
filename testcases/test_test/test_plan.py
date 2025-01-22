import pytest
import allure
from datetime import datetime
from pages.test_module.plan_page import PlanPage

@allure.feature('Test Plan Management')
@pytest.mark.test
class TestPlan:
    @allure.story('Plan Operations')
    @allure.title('Create and Delete Test Plan')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_plan_operations(self, driver, config):
        """测试计划的创建和删除"""
        try:
            with allure.step("创建PlanPage实例"):
                plan_page = PlanPage(driver)
            
            with allure.step("导航到计划管理页面"):
                plan_page.navigate_to()
            
            with allure.step("创建新计划"):
                plan_name = f"Auto_Test_Plan_{datetime.now().strftime('%Y%m%d%H%M%S')}"
                plan_page.create_new_plan(plan_name)
                assert plan_page.is_plan_created(plan_name), f"Plan {plan_name} was not created successfully"
            
            with allure.step("删除计划"):
                assert plan_page.delete_plan(plan_name), "Failed to delete plan"
                assert plan_page.is_plan_deleted(plan_name), f"Plan {plan_name} was not deleted successfully"
            
        except Exception as e:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail(f"Test failed: {str(e)}")