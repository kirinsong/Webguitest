import os
import sys
import pytest
from pages.lab_module.ota_page import OtaPage
from common.read_yaml import ReadYaml




class TestOta:
    @pytest.mark.ota
    def test_add_new_version(self, driver):
        """测试添加新的OTA版本"""
        try:
            # 1. 进入OTA release list页面
            driver.get("http://172.16.20.170:18080/autogo2024/#/lab/otaManagement/releases")
            
            # 2. 创建OtaPage实例并执行添加版本操作
            ota_page = OtaPage(driver)
            version = ota_page.add_new_version()  # 获取返回的版本号
            
            # 3. 断言操作是否成功
            assert version is not None, "Failed to add new OTA version"
            
            # 4. 上传TA文件
            assert ota_page.upload_ta_file(version), "Failed to upload TA file"
            
        except Exception as e:
            pytest.fail(f"Test failed: {str(e)}")