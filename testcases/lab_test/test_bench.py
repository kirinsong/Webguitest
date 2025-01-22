import os
import sys
import logging

# 获取项目根目录路径
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

import pytest
from pages.lab_module.bench_page import BenchPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.lab
class TestBench:
    def test_create_and_convert_bench(self, driver, config, caplog):
        """测试创建manual bench并转换为auto bench"""
        # 设置日志级别
        caplog.set_level(logging.INFO)
        
        bench_page = BenchPage(driver)
        
        # 导航到Bench页面
        bench_page.navigate_to()
        
        # 创建manual bench
        bench_name = bench_page.create_manual_bench()
        
        # 验证bench创建成功
        assert bench_page.verify_bench_created(bench_name), "Manual bench creation verification failed"
        
        # 转换为auto bench
        assert bench_page.convert_to_auto_bench(), "Failed to convert to auto bench"
        
        # 验证auto bench转换成功
        assert bench_page.verify_auto_bench_converted(bench_name), "Failed to verify auto bench conversion"
        
        # 创建issue
        assert bench_page.create_issue(), "Failed to create issue"
        
        # 关闭issue
        assert bench_page.close_issue(), "Failed to close issue" 