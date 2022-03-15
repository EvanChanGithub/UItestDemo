from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
import win32gui
import win32api
import win32con

class WebDriver(object):
    def __init__(self,driver):
        self.driver = driver

    def findWindow(self,ClassName,WindowName):
        win32gui.FindWindow(ClassName,WindowName)

    def findWindowEx(self,hwndParent, hwndChild ,IpClassName,IpwindowName=None):
        win32gui.FindWindowEx(hwndParent, hwndChild, IpClassName, IpwindowName)

    def findElement(self,*loc):
        try:
            return  WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print('错误信息：{0}'.format(e.args[0]))

    def findElements(self, *loc):
        try:
            return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_elements(*loc))
        except NoSuchElementException as e:
            print('错误信息：{0}'.format(e.args[0]))
    
    
    def findElement_untilpresenceOfAllElements(self,*loc):
        '''显性等待页面中所有元素'''
        try:
            return  WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located(loc))
        except NoSuchElementException as e:
            print('错误信息：{0}'.format(e.args[0]))

    def findElement_untilelementClickable(self,*loc):
        '''等待元素直到可点击'''
        try:
            return  WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable(loc))
        except NoSuchElementException as e:
            print('错误信息：{0}'.format(e.args[0]))

    def findElement_untilelementvisiable(self,*loc):
        '''等待元素直到可见'''
        try:
            return  WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(loc))
        except NoSuchElementException as e:
            print('错误信息：{0}'.format(e.args[0]))


    def actionchains_moveToElement(self,element):  
        return ActionChains(self.driver).move_to_element(element).perform()
    
    def scrollToelement(self,*loc):
        # self.driver.execute_script("var q=document.documentElement.scrollTop=1000000")
        # ele = self.driver.find_element(*loc)
        ele = WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(loc))
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        # js = '''window.scrollTo(0, 1000)'''
        # self.driver.execute_script(js)

    def input_execute_script(self,js):
        # js = 'var ucode = document.getElementById("{}").innerHTML=("{}"); ucode.value=arguments[0]'.format(id,text)
        # print(js)
        self.driver.execute_script(js)
        

    def switchtoframe(self,*frames):
        time.sleep(1)
        self.driver.switch_to_default_content()
        for frame in frames:
            # print(frame)
            time.sleep(1.5)
            self.driver.switch_to.frame(frame)
        time.sleep(2)

    def switchto_iframe(self, iframe):
        time.sleep(1)
        self.driver.switch_to.frame(iframe)
        time.sleep(1)


    def switchto_default(self):
        time.sleep(1)
        self.driver.switch_to_default_content()
        time.sleep(1)
