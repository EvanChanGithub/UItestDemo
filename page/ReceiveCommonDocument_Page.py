from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.basePage import *
import time
import random
from utils.helper import Helper
from datetime import datetime
import win32gui
import win32api
import win32con

class ReceiveCommonDocument(WebDriver):

    # 单位公文菜单
    menu2_loc = (By.XPATH, '''//div[@title="{}"]'''.format(Helper().getXmlAttribute("testdataTYSW_bgsry.xml", "menuName2", "value")))
    # 单位公文子菜单
    sub_menu2_loc = (By.XPATH,'''//*[@id="cyan_tree_node0"]/div[contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYSW_bgsry.xml", "submenuName1", "value")))
    # 收文箱的子菜单
    # 收文处理菜单
    submenu1Node1_loc = (By.XPATH, '''//div[1]/div[@class="cyan-tree-node-text" and contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYSW_bgsry.xml", "submenu1Node1", "value")))
    # 纸质收文菜单
    submenu1Node2_loc  = (By.XPATH,'''//div[2]/div[@class="cyan-tree-node-text" and contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYSW_bgsry.xml", "submenu1Node2", "value")))
    # 全部收文菜单
    submenu1Node3_loc = (By.XPATH, '''//div[5]/div[@class="cyan-tree-node-text" and contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYSW_bgsry.xml", "submenu1Node4", "value")))

    '''纸质收文子菜单'''
    # 收文稿笺-通用收文按钮
    swgj_tysw_loc = (By.XPATH, '''//div/ul/li/a[contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYSW_bgsry.xml", "documentName", "value")))
    # 表单元素
    swgj_tysw_receiveNumber_input_loc  = (By.XPATH, '''//div[@id="通用收文表单"]/input[contains(@name,"通用收文表单.原文号")] ''')
    swgj_tysw_receiveFrom_input_loc = (By.XPATH, '''//div[@id="通用收文表单"]/input[contains(@name,"通用收文表单.来文单位")] ''')
    dateSelect_iframe_loc = (By.XPATH, '''/html/body/div[1]/iframe''')
    swgj_tysw_receiveDate_select_loc = (By.XPATH, '''//div[@id="通用收文表单"]/input[contains(@name,"通用收文表单.来文日期")]''')
    swgj_tysw_receiveDate_iframe =  (By.XPATH, '''/html/body/div[1]/iframe''')
    swgj_tysw_receiveDate_loc = (By.XPATH, '''//tr[4]/td[@onmouseout="this.className='Wday'"]''')
    swgj_tysw_receiveTimeLimit_select_loc = (By.XPATH, '''//div[@id="通用收文表单"]/input[contains(@name,"通用收文表单.办理时限")]''')
    swgj_tysw_title_loc = (By.XPATH, '''//div[@id="通用收文表单"]/input[contains(@name,"通用收文表单.文件名称")] ''')
    # swgj_tysw_title_loc = (By.XPATH,'''/html/body/form/div[2]/div[1]/div/div/input[16]''')

    '''通用收文的按钮栏'''
    save_btn_loc = (By.XPATH, '''//button[contains(text(),"保存")]''')
    gsfzr_approve_btn_loc = (By.XPATH, '''//button[contains(text(),"股室负责人审核")]''')
    fgld_approve_btn_loc = (By.XPATH, '''//button[contains(text(),"呈领导")]''')
    fhngr_btn_loc = (By.XPATH, '''//button[contains(text(),"返回拟稿人")]''')
    cwcl_btn_loc = (By.XPATH, '''//button[contains(text(),"成文处理")]''')
    # receive_btn_loc = (By.XPATH, '''//div[1]/span[2]/button[contains(text(),"接收")]''')
    receive_btn_loc = (By.XPATH, '''//button[contains(text(),"接收")]''')
    fwdw_btn_loc = (By.XPATH, '''//button[contains(text(),"发外单位")]''')

    '''待办公文子菜单'''
    # 按钮栏
    dbgw_query_btn_loc = (By.XPATH,'''//div[@class="buttons"]/button[@id="btn_query" and contains(text(),"查询")]''')
    # 待办公文第一行查询结果
    dbgw_result1_loc = (By.XPATH, '''//*[@id="mainBody"]/div/div[2]/table/tbody/tr/td[4]/div/span/a''')
    # 查询子页面
    dbgw_queruwindow_title_input_loc = (By.XPATH, '''//div/span[1]/input[@name="title"]''')
    dbgw_queruwindow_query_loc = (By.XPATH, '''//div[@id="query_window"]/div[@class="query_window_buttons"]/button[contains(text(),"查询")]''')



    '''收文处理子菜单'''
    # 按钮栏
    swcl_query_btn_loc = (By.XPATH, '''//button[@id="btn_query" and contains(text(),"查询")]''')

    # 页面第一行查询结果
    swgw_result1_loc = (By.XPATH, '''//tr/td[4]/div/spana[contains(text(),{})]'''.format("测试通用拟文"))
    swcl_queruwindow_title_input_loc = (By.XPATH, '''//div/span[1]/input[@name="title"]''')
    swcl_queruwindow_query_loc = (By.XPATH, '''//div[@id="query_window"]/div[@class="query_window_buttons"]/button[contains(text(),"查询")]''')
    sqcl_receive_btn_loc = (By.XPATH, '''//button[contains(text(),"接收")]''')




    '''公共'''
    # 确定按钮
    confirmBox_ok_button =  (By.XPATH, '''//button[contains(text(),"确定")]''')
    common_ifame_loc = (By.XPATH, '''//iframe[contains(@name,'WindowFrame')]''')

    '''选择接收对象框'''
    # '''/html/body/div[5]/div[2]/iframe'''
    # receiver_input_loc = (By.XPATH, '''//div[@id="group_receiver_select"]/div[1]/input''')
    receiver_input_loc = (By.XPATH, '''/html/body/form/div/div[1]/input''')
    # receiver_confirm_loc = (By.XPATH,'''//button[contains(text(),"确定")]''')


    def swcl_tysw(self, titleName):
        '''单位公文-收文箱-收文处理-通用收文流程'''
        # 进入纸质发文菜单
        self.click_menuitem(self.menu2_loc, self.sub_menu2_loc, self.submenu1Node1_loc)
        self.switchtoframe("mainFrame", "main_frame1")
        self.dbgw_query(titleName)
        self.click_receive_btn
        self.input_tyswInfo
        time.sleep(2)

    def zzsw_tysw_process(self):
        '''单位公文-收文箱-纸质收文-通用收文流程'''
        # 进入纸质发文菜单
        self.click_menuitem(self.menu2_loc, self.sub_menu2_loc, self.submenu1Node2_loc)
        self.save_tysw
        time.sleep(1)
        self.driver.get(self.getXmlData("url.xml", 'mainurl'))
        time.sleep(5)

    @property
    def click_receive_btn(self):
        self.findElement(*self.sqcl_receive_btn_loc).click()
        self.switchto_default()
        iframe = self.findElement(*self.common_ifame_loc)
        self.switchto_iframe(iframe)
        self.findElement(*self.confirmBox_ok_button).click()
        time.sleep(2)


    @property
    def input_tyswInfo(self):
        '''填写通用收文信息保存'''
        self.switchtoframe("mainFrame", "main_frame2")

        self.findElement(*self.swgj_tysw_receiveNumber_input_loc).send_keys(self.getXmlAttribute("testdataTYSW_bgsry.xml", "receiveNumber", "value"))
        # titleName = "{}{}{}{}".format("【", datetime.now().strftime("%Y-%m-%d-%H:%M"), "】 ",self.getXmlAttribute("testdataTYSW_bgsry.xml", "documentTitle", "value"))
        # self.findElement(*self.swgj_tysw_title_loc).clear()
        # self.findElement(*self.swgj_tysw_title_loc).send_keys(titleName)
        time.sleep(2)
        self.findElement(*self.save_btn_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(1)
        self.findElement(*self.confirmBox_ok_button).click()



    @property
    def save_tysw(self):
        '''填写通用收文信息后保存'''
        self.switchtoframe("mainFrame", "main_frame1")
        self.findElement(*self.swgj_tysw_loc).click()
        self.findElement(*self.swgj_tysw_receiveNumber_input_loc).send_keys(self.getXmlAttribute("testdataTYSW_bgsry.xml", "receiveNumber", "value"))
        self.findElement(*self.swgj_tysw_receiveFrom_input_loc).send_keys(self.getXmlAttribute("testdataTYSW_bgsry.xml", "receiveFrom", "value"))
        self.findElement(*self.swgj_tysw_receiveDate_select_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(1)
        self.driver.switch_to.frame(self.findElement(*self.dateSelect_iframe_loc ))
        time.sleep(1)
        self.findElement(*self.swgj_tysw_receiveDate_loc).click()
        self.switchtoframe("mainFrame", "main_frame1")
        titleName = "{}{}{}{}".format("【", datetime.now().strftime("%Y-%m-%d-%H:%M"), "】 ",self.getXmlAttribute("testdataTYSW_bgsry.xml", "documentTitle", "value"))
        self.findElement(*self.swgj_tysw_title_loc).send_keys(titleName)
        time.sleep(2)
        self.findElement(*self.save_btn_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(1)
        self.findElement(*self.confirmBox_ok_button).click()

    def click_menuitem(self,menu_loc,sub_menu,sub_menu_third ):
        '''点击一级二级菜单'''
        self.switchtoframe("mainFrame")
        self.findElement(*menu_loc).click()
        time.sleep(2)
        self.findElement(*sub_menu).click()
        time.sleep(2)
        self.findElement(*sub_menu_third).click()

    def dbgw_query(self,titleName):
        '''查询公文名称'''
        self.findElement(*self.swcl_query_btn_loc).click()
        self.findElement(*self.swcl_queruwindow_title_input_loc).send_keys(titleName)
        time.sleep(2)
        self.findElement(*self.swcl_queruwindow_query_loc).click()
        time.sleep(2)