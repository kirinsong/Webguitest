import logging
import os
from datetime import datetime

class Logger:
    def __init__(self):
        # 使用绝对路径创建logs目录
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # 设置日志文件路径
        log_file = os.path.join(log_dir, f'test_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        
        # 创建 logger
        self.logger = logging.getLogger('AutoGoTest')
        self.logger.setLevel(logging.INFO)
        
        # 创建文件处理器
        file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # 设置日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            '%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # 添加处理器
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
    
    def info(self, message):
        self.logger.info(message)
        self.logger.handlers[0].flush()  # 立即刷新文件处理器
    
    def error(self, message):
        self.logger.error(message)
        self.logger.handlers[0].flush()
    
    def warning(self, message):
        self.logger.warning(message)
        self.logger.handlers[0].flush()
    
    def debug(self, message):
        self.logger.debug(message)
        self.logger.handlers[0].flush() 