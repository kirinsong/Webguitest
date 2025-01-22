# Web UI Automation Testing Framework

基于 Selenium 和 pytest 的 Web UI 自动化测试框架，用于实现 Web 界面的自动化测试。


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



## 📁 项目结构
```
Webguitest/
├── pages/                          # 页面对象目录
│   ├── base_page.py               # 基础页面类，包含共用方法
│   ├── login_page.py              # 登录页面
│   └── server_module/             # 服务器模块页面
│       └── user_page.py           # 用户管理页面
│
├── test_module/                    # 测试模块页面目录
│   ├── test_module/               # 测试管理模块
│   │   ├── plan_page.py          # 计划管理页面
│   │   ├── resource_page.py      # 资源管理页面
│   │   └── execution_page.py     # 执行管理页面
│   └── lab_module/               # 实验室模块
│       ├── bench_page.py         # 工作台页面
│       └── ota_page.py          # OTA管理页面
│
├── testcases/                     # 测试用例目录
│   ├── test_test/                # 测试模块用例
│   │   ├── test_resource.py     # 资源管理测试
│   │   ├── test_plan.py         # 计划管理测试
│   │   └── test_execution.py    # 执行管理测试
│   ├── lab_test/                # 实验室模块测试
│   │   ├── test_bench.py       # 工作台测试
│   │   └── test_ota.py         # OTA管理测试
│   └── server_test/             # 服务器模块测试
│       └── test_user.py         # 用户管理测试
│
├── common/                        # 公共组件目录
│   ├── utils.py                  # 工具函数
│   └── logger.py                 # 日志配置
│
├── config/                       # 配置文件目录
│   ├── config.ini               # 基础配置
│   └── locators.py              # 元素定位配置
│
├── reports/                      # 测试报告目录
│   ├── html_reports/            # HTML报告
│   └── allure_results/          # Allure报告数据
│
├── logs/                        # 日志文件目录
│   └── test.log                # 测试运行日志
│
├── data/                        # 测试数据目录
│   └── test_data.json          # 测试数据文件
│
├── drivers/                     # 浏览器驱动目录
│   └── chromedriver            # Chrome浏览器驱动
│
├── venv/                        # Python虚拟环境
├── conftest.py                 # pytest配置文件
├── pytest.ini                  # pytest配置文件
├── requirements.txt            # 项目依赖
└── run_tests.py               # 测试运行入口
```

## 📚 目录说明

### 1. pages/
- **基础页面类**：包含所有页面共用的基础方法
- **功能模块页面**：按照系统模块划分的页面对象
  - 服务器管理模块
  - 测试管理模块
  - 实验室模块

### 2. test_module/
- **测试管理模块**：包含测试计划、资源、执行等页面
- **实验室模块**：包含工作台、OTA等功能页面

### 3. testcases/
- **按模块组织的测试用例**
  - test_test: 测试管理相关用例
  - lab_test: 实验室功能相关用例
  - server_test: 服务器管理相关用例

### 4. common/
- **公共组件和工具类**
  - 日志配置
  - 工具函数
  - 通用方法

### 5. config/
- **配置文件**
  - 系统配置
  - 元素定位配置
  - 环境配置

### 6. reports/
- **测试报告**
  - HTML格式报告
  - Allure报告
  - 测试结果数据

### 7. 其他目录
- **logs/**: 运行日志
- **data/**: 测试数据
- **drivers/**: 浏览器驱动
- **venv/**: Python虚拟环境

### 8. 根目录文件
- **conftest.py**: pytest配置和固件
- **pytest.ini**: pytest运行配置
- **requirements.txt**: 项目依赖
- **run_tests.py**: 测试执行入口

## 🔄 项目工作流
1. 通过 `run_tests.py` 启动测试
2. 加载 `conftest.py` 中的配置和固件
3. 执行 `testcases` 中的测试用例
4. 测试用例调用 `pages` 中的页面对象
5. 使用 `common` 中的公共方法
6. 生成测试报告到 `reports` 目录
7. 记录日志到 `logs` 目录

## 📋 使用说明
1. 新增测试用例时，在对应模块的 testcases 目录下创建
2. 新增页面对象时，在对应模块的 pages 目录下创建
3. 公共方法添加到 common 目录
4. 配置信息添加到 config 目录
```
