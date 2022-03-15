import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# # import time
# from base.basePage import WebDriver
from page.login_Page import Login
from utils.helper import Helper

# ,WebDriver
class Init(unittest.TestCase,Helper):

    def setUp(self):
        # self.globalcaseName = globals()
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    Init().getXmlData('url')

    

