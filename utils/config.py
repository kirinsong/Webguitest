import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        
        # 基础URL配置
        self.BASE_URL = os.getenv('BASE_URL', 'http://localhost:8080')
        
        # 登录凭证
        self.ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
        self.ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')
        
        # 超时配置
        self.TIMEOUT = int(os.getenv('TIMEOUT', '10'))
        
        # 浏览器配置
        self.BROWSER = os.getenv('BROWSER', 'chrome') 