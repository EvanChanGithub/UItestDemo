import unittest
import os
import time
import HTMLTestRunner
from utils.helper import Helper

def allCases():
    suite = unittest.TestLoader().discover(start_dir=os.path.dirname(__file__),pattern="test*_*.py",top_level_dir=None)
    # suite = unittest.TestLoader().loadTestsFromModule(Helper().dir_base("test_sendDocument.py", filePath='testcase'))
    return suite

def getNowTime():
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
    fileName=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'Report.html')
    fp=open(fileName,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='UI自动化测试报告',
        description='UI自动化测试报告详细信息')
    runner.run(allCases())

if __name__ == '__main__':
    run()