# Web UI Automation Testing Framework

基于 Selenium 和 pytest 的 Web UI 自动化测试框架。

## 📁 项目结构
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

## 🔧 环境要求
- Python 3.10+
- Chrome 浏览器
- ChromeDriver

## 📦 安装
1. 创建虚拟环境
```bash
python -m venv venv
```

2. 激活虚拟环境
```bash
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

## 🚀 运行测试
```bash
# 运行所有测试
pytest

# 运行特定测试
pytest testcases/test_test/test_plan.py

# 生成 Allure 报告
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results
```

## 💡 设计模式
- 使用 Page Object Model (POM) 设计模式
- 将页面操作和测试用例分离，提高代码复用性和维护性

## 🔨 主要组件
### base_page.py - 基础页面类
```python
class BasePage:
    def __init__(self, driver):
        self.driver = driver  # WebDriver实例
        self.logger = logging.getLogger()  # 日志记录器
    
    def click(self, by, value):
        """点击元素的通用方法"""
        self.driver.find_element(by, value).click()
```

### plan_page.py - 计划管理页面类
```python
class PlanPage(BasePage):
    # 页面元素定位器
    CREATE_BTN = (By.XPATH, "//span[text()='Create']")
    
    def create_new_plan(self, plan_name):
        """创建新计划的方法"""
        self.click(*self.CREATE_BTN)
        # ... 其他操作
```

### test_plan.py - 测试用例
```python
class TestPlan:
    def test_plan_operations(self, driver):
        plan_page = PlanPage(driver)
        plan_page.create_new_plan("测试计划")
```

## 🛠 关键技术
- **Selenium WebDriver**: 自动化浏览器操作
- **pytest**: 测试框架
- **allure**: 生成精美的测试报告
- **Page Object Model**: 设计模式
- **显式等待**: 处理页面加载和元素交互

## 📝 测试流程
```python
@allure.feature('Test Plan Management')
class TestPlan:
    def test_plan_operations(self, driver):
        """测试计划的创建和删除"""
        with allure.step("创建PlanPage实例"):
            plan_page = PlanPage(driver)
        
        with allure.step("创建新计划"):
            plan_page.create_new_plan("测试计划")
```

## ✨ 项目特点
- 模块化设计
- 良好的代码组织
- 详细的日志记录
- 精美的测试报告
- 可靠的错误处理
- 易于维护和扩展

## 📌 最佳实践
- 使用显式等待处理页面加载
- 详细的日志记录
- 截图保存失败场景
