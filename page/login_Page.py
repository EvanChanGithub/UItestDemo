from selenium.webdriver.common.by import By
from base.basePage import *
from time import sleep
import json
import os
import time
from utils.helper import Helper
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Login(WebDriver,Helper):
    def __init__(self):
        self.loginUrl = self.getXmlData("url.xml",'loginurl')
    # 登录名输入框元素属性
    inputLoginName_loc = (By.NAME, "loginName")
    # 密码输入框元素属性
    inputPasswordName_loc = (By.NAME, "password")
    chrome_options = webdriver.ChromeOptions()

    # 设置开发者模式启动，该模式下webdriver属性为正常值
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chromedriver = "E:\\Program File\\Chrome\\Application\\chromedriver.exe"
    path = "E:\Program File\Chrome\Application\chromedriver"


    # IE浏览器设置
    capabilities = DesiredCapabilities.INTERNETEXPLORER
    # delete platform and version keys
    capabilities.pop("platform", None)
    capabilities.pop("version", None)
    # ieOption = webdriver.IeOptions()
    # ieOption.ignore_zoom_level = True
    capabilities['ignoreZoomSetting'] = True
    # capabilities.setCapability(InternetExplorerDriver.IGNORE_ZOOM_SETTING, true)
    iedriverPath = "C:\Program Files\Internet Explorer\IEDriverServer.exe"


    def loginSystem(self, username,usedriver):
        # self.driver.get(self.getXmlData('url'))
        # self.getCookie()

        # 首次登录遍历所有用户手动登录一次存储cookies
        if not os.path.exists(self.dir_base("cookies.xml", filePath='data')):
            nodes = self.getXmlList("user.xml", 'user')
            for node in nodes:
                if node.nodeName != '#text' and "{}".format(node.nodeName).index("user") != -1:
                    # for attr, attr_val in node.attributes.items():
                    #     print('\t\t\t\t\t打印属性名称和值', attr, '=', attr_val)
                    print(node.getAttribute('username'))
                    print(node.getAttribute('password'))
                    # 判断使用的浏览器类型
                    # if node.getAttribute('browser') == "chrome":
                        # 使用指定的谷歌浏览器用户
                    self.chrome_options.add_argument(node.getAttribute('user-data-dir'))
                    self.driver = webdriver.Chrome(self.chromedriver, options=self.chrome_options)
                    self.getCookie(node.getAttribute('username'),node.getAttribute('password'))
                    self.driver.quit()
                    # elif node.getAttribute('browser') == "ie":
                    #     self.driver = webdriver.Ie(executable_path=self.iedriverPath,capabilities=self.capabilities)
                    #     self.getCookie(node.getAttribute('username'), node.getAttribute('password'))
                    #     self.driver.quit()
        # 后续登录采用cookies
        if usedriver == "chrome":
            self.chrome_options.add_argument(self.getXmlAttribute("user.xml", username, "user-data-dir"))
            self.driver = webdriver.Chrome(self.chromedriver, options=self.chrome_options)
            self.driver.get(self.getXmlData("url.xml",'loginurl'))
            listCookies = json.loads(self.getXmlUser("cookies.xml", self.getXmlAttribute("user.xml", username, "username") , 'cookies'))
            # print(listCookies)
            # with open(self.dir_base("Cookies.txt", filePath = 'data'), 'r', encoding='utf8') as f:
            #     listCookies = json.loads(f.read())
            for cookie in listCookies:
                if 'expiry' in cookie:
                    del cookie['expiry']
                self.driver.add_cookie(cookie)
            # 登录主页面
            self.driver.get(self.getXmlData("url.xml",'mainurl'))
            time.sleep(1)
            self.driver.set_window_size(1920,1080)
            self.driver.maximize_window()
            # 读取完cookie刷新页面
            # obj.refresh()
        elif usedriver == "ie":
            self.driver = webdriver.Ie( capabilities=self.capabilities, executable_path=self.iedriverPath)
            self.driver.get(self.getXmlData("url.xml", 'loginurl'))
            listCookies = json.loads(self.getXmlUser("cookies.xml", self.getXmlAttribute("user.xml", username, "username"), 'cookies'))
            # print(listCookies)
            # with open(self.dir_base("Cookies.txt", filePath = 'data'), 'r', encoding='utf8') as f:
            #     listCookies = json.loads(f.read())
            for cookie in listCookies:
                if 'expiry' in cookie:
                    del cookie['expiry']
                self.driver.add_cookie(cookie)
            # 登录主页面
            self.driver.get(self.getXmlData("url.xml", 'mainurl'))
            time.sleep(1)
            self.driver.maximize_window()
        return self.driver


    def getCookie(self, userName, passWord):
        if not os.path.exists(self.dir_base("cookies.xml", filePath='data')):
            self.create_xml("cookies.xml")
        if self.getXmlUser("cookies.xml", userName, "cookies") is None:
            self.driver.get(self.getXmlData("url.xml",'loginurl'))
            self.driver.maximize_window()
            self.findElement(*self.inputLoginName_loc).clear()
            self.findElement(*self.inputLoginName_loc).send_keys(userName)
            self.findElement(*self.inputPasswordName_loc).clear()
            self.findElement(*self.inputPasswordName_loc).send_keys(passWord)
            # 预留验证码的时间
            sleep(13)
            dictCookies = self.driver.get_cookies()
            jsonCookies = json.dumps(dictCookies)
            # print(jsonCookies)
            self.write_xml('cookies.xml', userName, 'cookies',jsonCookies)
            # with open(self.dir_base("Cookies.txt", filePath = 'data'), 'w') as f:
            #     f.write(jsonCookies)






            
if __name__ == '__main__':
    test = Login()
    test.loginSystem('user1')