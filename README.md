# Web UI Automation Testing Framework

基于 Selenium 和 pytest 的 Web UI 自动化测试框架。

## 项目结构
# Web UI Automation Testing Framework

基于 Selenium 和 pytest 的 Web UI 自动化测试框架。

## 项目结构
## 项目结构
```
Webguitest/
├── pages/
│   ├── base_page.py          # 基础页面类
│   └── login_page.py         # 登录页面
├── test_module/
│   └── plan_page.py          # 计划管理页面
├── testcases/
│   └── test_test/
│       ├── test_plan.py      # 计划管理测试
│       └── test_execution.py  # 计划执行测试
├── conftest.py               # pytest配置文件
├── reports/                  # 测试报告目录
├── venv/                     # Python虚拟环境
├── requirements.txt          # 项目依赖
└── pytest.ini               # pytest配置文件
```


## 环境要求
- Python 3.10+
- Chrome 浏览器
- ChromeDriver

## 安装
创建虚拟环境
python -m venv venv
激活虚拟环境
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
安装依赖
pip install -r requirements.txt

## 运行测试
运行所有测试
pytest
运行特定测试
pytest testcases/test_test/test_plan.py
生成 Allure 报告
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results

补充：
1.设计模式
使用 Page Object Model (POM) 设计模式
将页面操作和测试用例分离，提高代码复用性和维护性

2.主要组件 
# base_page.py - 基础页面类
class BasePage:
    def __init__(self, driver):
        self.driver = driver  # WebDriver实例
        self.logger = logging.getLogger()  # 日志记录器
    
    def click(self, by, value):
        """点击元素的通用方法"""
        self.driver.find_element(by, value).click()

# plan_page.py - 计划管理页面类
class PlanPage(BasePage):
    # 页面元素定位器
    CREATE_BTN = (By.XPATH, "//span[text()='Create']")
    
    def create_new_plan(self, plan_name):
        """创建新计划的方法"""
        self.click(*self.CREATE_BTN)
        # ... 其他操作

# test_plan.py - 测试用例
class TestPlan:
    def test_plan_operations(self, driver):
        plan_page = PlanPage(driver)
        plan_page.create_new_plan("测试计划")

3.关键技术
Selenium WebDriver: 自动化浏览器操作
pytest: 测试框架
allure: 生成精美的测试报告
Page Object Model: 设计模式
显式等待: 处理页面加载和元素交互

4.测试流程
# 一个典型的测试用例
@allure.feature('Test Plan Management')
class TestPlan:
    def test_plan_operations(self, driver):
        """测试计划的创建和删除"""
        with allure.step("创建PlanPage实例"):
            plan_page = PlanPage(driver)
        
        with allure.step("创建新计划"):
            plan_page.create_new_plan("测试计划")
5.运行测试
# 运行特定测试
pytest testcases/test_test/test_plan.py

# 生成allure报告
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results


6.项目特点
模块化设计
良好的代码组织
详细的日志记录
精美的测试报告
可靠的错误处理
易于维护和扩展


7.最佳实践
使用显式等待处理页面加载
详细的日志记录
截图保存失败场景
使用 allure 装饰器组织测试步骤
统一的异常处理机制


