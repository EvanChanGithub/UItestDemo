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

class SendCommonDocument(WebDriver, Helper):
    def __init__(self):
        self.caseName = " "

    # 内部公文菜单
    menu_loc = (By.XPATH, '''//div[@title="{}"]'''.format(Helper().getXmlAttribute("testdataTYNW_ky.xml", "menuName", "value")))
    # sub_menu_loc = (By.XPATH, '''//div[contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYNW_ky.xml", "submenuName", "value")))
    # 内部公文子菜单
    sub_menu1_loc = (By.XPATH, '''//div/div[@class="sub_menu_item_title" and contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYNW_ky.xml", "submenuName1", "value")))
    sub_menu2_loc = (By.XPATH, '''//div/div[@class="sub_menu_item_title" and contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYNW_kz.xml", "submenuName2", "value")))
    sub_menu3_loc = (By.XPATH, '''//div/div[@class="sub_menu_item_title" and contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYNW_ky.xml", "submenuName3", "value")))

    # '''/html/body/div[3]/div[3]/div/div[2]/div/div[1]'''
    '''新建公文子菜单'''
    # 发文稿笺-通用拟文
    send_document_loc = (By.XPATH, '''//a[contains(text(),"{}")]'''.format(Helper().getXmlAttribute("testdataTYNW_ky.xml", "document", "value")))
    # 通用拟文
    # commondoc_input_loc = (By.XPATH, '''/html/body/form/div[2]/div[1]/div/div/input[7] ''')
    commondoc_draftPerson_input_loc = (By.XPATH, '''//div[contains(@id,"通用发文")]/input[contains(@name,"拟稿者")] ''')
    commondoc_title_input_loc = (By.XPATH, '''//div[contains(@id,"通用发文")]/input[contains(@name,"文件标题")] ''')
    # commondoc_remark_input_loc = (By.XPATH,  '''//div[contains(@id,"通用发文")]/div[contains(@id,"附注")]/textarea[contains(@name,"附注")] ''')
    commondoc_remark_input_loc = (By.XPATH, '''//div[2]/div[1]/div/div/div[contains(@id,"附注")]''')

    commondoc_remark_input_id = '通用发文稿笺1.附注$div'
    commondoc_opinion_input_loc = (By.XPATH, '''//div[contains(@id,"通用发文")]/div[contains(@id,"处理意见")] ''')

    commondoc_text_input_loc = (By.XPATH, '''//div[contains(@id,"通用发文")]/div[contains(@id,"短信通知内容")] ''')
    commondoc_text_input_id = '通用发文稿笺1.短信通知内容$textdiv'
    # 正文的两个按钮
    import_wordandpdf_button_loc = (By.XPATH,'''//div/button[contains(text(),"导入word、pdf")]''')
    import_otherformatfile_button_loc = (By.XPATH, '''//div/button[contains(text(),"导入其他格式")]''')
    # 导入其他格式文件框

    # 拟稿人意见填写框
    opinion_iframe = (By.XPATH, '''//div[@class="cyan-window"]/div[@class="cyan-window-body"]/iframe''')
    opinion_input_loc = (By.XPATH, '''//div[1]/div[1]/div[2]/textarea''')  # /html/body/form/div[1]/div[1]/div[2]/textarea
    opinion_confirm_loc = (By.XPATH, '''/html/body/form/div[3]/span[1]/button''')
    # 主送、抄送输入框
    mainDelivery_select_loc =  (By.XPATH,'''//div[contains(@title,"单击选择主送部门")]''')
    secondDelivery_select_loc = (By.XPATH, '''//div[contains(@id,"抄送")]''')

    # 通用拟文的按钮栏
    save_btn_loc = (By.XPATH, '''//div[1]/span[1]/button[contains(text(),"保存")]''')
    gsfzr_approve_btn_loc = (By.XPATH, '''//div[1]/span[5]/button[contains(text(),"股室负责人审核")]''')
    fgld_approve_btn_loc = (By.XPATH, '''//div[1]/span[5]/button[contains(text(),"呈领导")]''')
    fhngr_btn_loc = (By.XPATH, '''//div[1]/span[7]/button[contains(text(),"返回拟稿人")]''')
    cwcl_btn_loc = (By.XPATH, '''//div[1]/span[7]/button[contains(text(),"成文处理")]''')
    # receive_btn_loc = (By.XPATH, '''//div[1]/span[2]/button[contains(text(),"接收")]''')
    receive_btn_loc = (By.XPATH, '''//tbody/tr[1]/td[3]/div/button[contains(text(),"接收")]''')
    fwdw_btn_loc = (By.XPATH, '''//div[1]/span[8]/button[contains(text(),"发外单位")]''')

    ''' 草稿箱子菜单 '''
    # 按钮栏
    cgx_query_btn_loc = (By.XPATH, '''//div[1]/div[1]/div/div[2]/div[1]/span[1]/button[contains(text(),"查询")]''')
    # 草稿箱第一行查询结果
    cgx_result1_loc = (By.XPATH, '''//*[@id="mainBody"]/div/div[2]/table/tbody/tr/td[3]/div/span/a''')
    # 查询子页面
    cgx_queruwindow_query_btn_loc = (By.XPATH, '''//*[@id="query_window"]/div[@class="query_window_buttons"]/button[contains(text(),"查询")] ''')
    cgx_queruwindow_title_input_loc = (By.XPATH, '''//div/span/input[@name="title"]''')

    '''待办公文子菜单'''
    # 按钮栏
    dbgw_query_btn_loc = (By.XPATH,'''//div[@class="buttons"]/button[@id="btn_query" and contains(text(),"查询")]''')
    # 待办公文第一行查询结果
    dbgw_result1_loc = (By.XPATH, '''//*[@id="mainBody"]/div/div[2]/table/tbody/tr/td[4]/div/span/a''')
    # 查询子页面
    dbgw_queruwindow_title_input_loc = (By.XPATH, '''//div/span[1]/input[@name="title"]''')
    dbgw_queruwindow_query_loc = (By.XPATH, '''//div[@id="query_window"]/div[@class="query_window_buttons"]/button[contains(text(),"查询")]''')

    '''公共'''
    # 信息确认框确定按钮
    confirmBox_ok_button =  (By.XPATH, '''//div[@class="cyan-messagebox-buttons cyan-box-buttons"]/button[contains(text(),"确定")]''')

    '''选择接收对象框'''
    # '''/html/body/div[5]/div[2]/iframe'''
    # receiver_input_loc = (By.XPATH, '''//div[@id="group_receiver_select"]/div[1]/input''')
    receiver_input_loc = (By.XPATH, '''/html/body/form/div/div[1]/input''')
    receiver_confirm_loc = (By.XPATH,'''//button[contains(text(),"确定")]''')

    '''送股室负责人审核接收框'''
    '''/html/body/div[5]/div[2]/iframe'''
    receiver_iframe = (By.XPATH, '''//div[@class="cyan-window"]/div[@class="cyan-window-body"]/iframe''')
    gsfzr_receiver_loc = (By.XPATH, '''//div[contains(text(),"{}")]/../../td[5]/div/label/span'''.format(Helper().getXmlAttribute("testdataTYNW_ky.xml", "gsfzr", "value")))
    receiver_confirm_loc = (By.XPATH, '''//button[contains(text(),"确定")]''')
    # “呈领导”选择输入框
    fgld_receiver_loc = (By.XPATH, '''//div[contains(text(),"{}")]/../../td[5]/div/label/span'''.format(Helper().getXmlAttribute("testdataTYNW_kz.xml", "fgld", "value")))
    # 发外单位接收框

    # 科员送成文处理接收框
    cwcl_receiver_loc = (By.XPATH, '''//div[contains(text(),"{}")]/../../td[5]/div/label/span'''.format(Helper().getXmlAttribute("testdataTYNW_ky.xml", "cwcl", "value")))


    def saveCommonDoc(self):
        '''科员拟稿，保存通用拟文'''
        self.switchtoframe("mainFrame")
        self.click_menuitem(self.sub_menu1_loc)
        self.switchtoframe("mainFrame", "main_frame1")
        self.click_document
        titleName = self.save_commonInfo1
        return titleName


    def editDocument(self,titleName):
        '''科员拟稿并并送科室负责人审核'''
        self.switchtoframe("mainFrame")
        self.click_menuitem(self.sub_menu3_loc)
        self.switchtoframe("mainFrame", "main_frame1")
        self.save_commonInfo2(titleName)
        self.sendTo_gsfzr


    def ksfzrTofgld(self,titleName):
        '''科室负责人填写意见，送领导审核'''
        self.switchtoframe("mainFrame")
        self.click_menuitem(self.sub_menu2_loc)
        self.switchtoframe("mainFrame", "main_frame1")
        self.sendTo_fgld(titleName)

    def fgldTongr(self,titleName):
        '''分管领导填写意见，返回拟稿人'''
        self.switchtoframe("mainFrame")
        self.click_menuitem(self.sub_menu2_loc)
        self.switchtoframe("mainFrame", "main_frame1")
        self.sendTo_ngr(titleName)
        
    def ky_cwcl(self,titleName):
        '''科员成文处理'''
        self.switchtoframe("mainFrame")
        self.click_menuitem(self.sub_menu2_loc)
        self.switchtoframe("mainFrame", "main_frame1")
        self.ngr_cwcl(titleName)
        # 在接收人框选择接收人
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.switch_to.frame(self.findElement(*self.receiver_iframe))
        time.sleep(1)
        self.findElement(*self.cwcl_receiver_loc).click()
        time.sleep(1)
        self.findElement(*self.receiver_confirm_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(1)
        self.findElement(*self.confirmBox_ok_button).click()
        time.sleep(1)


        # receiverlist = []
        # for value in range(1, 3):
        #     receiverlist.append(self.getXmlAttribute("testdataTYNW_ky.xml", "docReceiver", "value{}".format(value)))
        # self.selectReceiver(receiverlist)

    def ky_swdw(self,titleName):
        '''科员发外单位'''
        self.switchtoframe("mainFrame")
        self.click_menuitem(self.sub_menu2_loc)
        self.switchtoframe("mainFrame", "main_frame1")
        self.cwcl_fwdw(titleName)
        time.sleep(1)


    def click_menuitem(self,sub_menu):
        self.findElement(*self.menu_loc).click()
        time.sleep(2)
        self.findElement(*sub_menu).click()

    @property
    def click_document(self):
        '''点击通用拟文'''
        time.sleep(2)
        self.findElement(*self.send_document_loc).click()

    @property
    def save_commonInfo1(self):
        # 填写拟稿人
        self.findElement(*self.commondoc_draftPerson_input_loc).clear()
        self.findElement(*self.commondoc_draftPerson_input_loc).send_keys(self.getXmlAttribute("testdataTYNW_ky.xml", "draftPerson", "value"))
        # 填写正文标题
        titleName = "{}{}{}{}".format("【", datetime.now().strftime("%Y-%m-%d-%H:%M"), "】 ",self.getXmlAttribute("testdataTYNW_ky.xml", "title", "value"))
        self.findElement(*self.commondoc_title_input_loc).send_keys(titleName)
        # 导入正文附件
        self.findElement(*self.import_otherformatfile_button_loc).click()
        fileinputdialog = win32gui.FindWindow(None, "选择要加载的文件")
        ComboBoxEx = win32gui.FindWindowEx(fileinputdialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx, 0, 'ComboBox', None)
        fileNameEdit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        confirmbutton = win32gui.FindWindowEx(fileinputdialog, 0, 'Button', "打开(&O)")
        time.sleep(2)
        win32gui.SendMessage(fileNameEdit, win32con.WM_SETTEXT, 0, "{}".format(self.getXmlAttribute("testdataTYNW_ky.xml", "attachmentPath", "value")))
        time.sleep(2)
        win32gui.SendMessage(fileinputdialog, win32con.WM_COMMAND, 1, confirmbutton)
        time.sleep(3)
        # 点击保存
        self.findElement(*self.save_btn_loc).click()
        time.sleep(3)
        return titleName


    def save_commonInfo2(self,titleName):
        # 查询公文名称
        self.findElement(*self.cgx_query_btn_loc).click()
        self.findElement(*self.cgx_queruwindow_title_input_loc).send_keys(titleName)
        time.sleep(3)
        self.findElement(*self.cgx_queruwindow_query_btn_loc).click()
        time.sleep(3)
        # 打开公文编辑页面
        self.findElement(*self.cgx_result1_loc).click()
        self.switchtoframe("mainFrame","main_frame2")
        # 填写附注
        self.input_execute_script('var ucode = document.getElementById("{}").innerHTML=("{}"); ucode.value=arguments[0]'.format(self.commondoc_remark_input_id, self.getXmlAttribute("testdataTYNW_ky.xml", "remark", "value")))
        # 向下滚动
        self.scrollToelement(*self.commondoc_remark_input_loc)
        # 输入处理意见方法1：
        self.findElement(*self.commondoc_opinion_input_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.switch_to.frame(self.findElement(*self.opinion_iframe))
        self.findElement(*self.opinion_input_loc).send_keys(self.getXmlAttribute("testdataTYNW_ky.xml", "kyopinion", "value"))
        self.findElement(*self.opinion_confirm_loc).click()
        # 输入短信内容
        self.switchtoframe("mainFrame", "main_frame2")
        self.input_execute_script('var ucode = document.getElementById("{}").innerHTML=("{}"); ucode.value=arguments[0]'.format(self.commondoc_text_input_id, self.getXmlAttribute("testdataTYNW_ky.xml", "text", "value")))
        time.sleep(1)
        self.findElement(*self.save_btn_loc).click()
        self.driver.switch_to_default_content()
        self.findElement(*self.confirmBox_ok_button).click()

    @property
    def sendTo_gsfzr(self):
        '''送股室负责人审核操作'''
        # 切回草稿箱页面
        self.switchtoframe("mainFrame", "main_frame1")
        # 打开公文编辑页面
        self.findElement(*self.cgx_result1_loc).click()
        self.switchtoframe("mainFrame", "main_frame2")
        # 点击股室负责人审核
        self.findElement(*self.gsfzr_approve_btn_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.switch_to.frame(self.findElement(*self.receiver_iframe))
        time.sleep(1)
        self.findElement(*self.gsfzr_receiver_loc).click()
        time.sleep(1)
        self.findElement(*self.receiver_confirm_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(2)
        # self.findElement(*self.confirmBox_ok_button).click()
        # time.sleep(1)


    def sendTo_fgld(self,titleName):
        '''送分管领导审核操作'''
        # 查询公文名称
        self.findElement(*self.dbgw_query_btn_loc).click()
        self.findElement(*self.dbgw_queruwindow_title_input_loc).send_keys(titleName)
        time.sleep(2)
        self.findElement(*self.dbgw_queruwindow_query_loc).click()
        time.sleep(2)
        # 打开公文编辑页面
        self.findElement(*self.dbgw_result1_loc).click()
        self.switchtoframe("mainFrame", "main_frame2")
        # 向下滚动
        self.scrollToelement(*self.commondoc_remark_input_loc)
        # 输入处理意见方法1：
        self.findElement(*self.commondoc_opinion_input_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.switch_to.frame(self.findElement(*self.opinion_iframe))
        self.findElement(*self.opinion_input_loc).send_keys(self.getXmlAttribute("testdataTYNW_kz.xml", "kzopinion", "value"))
        self.findElement(*self.opinion_confirm_loc).click()
        self.switchtoframe("mainFrame", "main_frame2")
        # 填写意见后，点击“呈领导”按钮
        self.findElement(*self.fgld_approve_btn_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.switch_to.frame(self.findElement(*self.receiver_iframe))
        time.sleep(1)
        self.findElement(*self.fgld_receiver_loc).click()
        time.sleep(1)
        self.findElement(*self.receiver_confirm_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(1)
        self.findElement(*self.confirmBox_ok_button).click()
        time.sleep(1)

    def sendTo_ngr(self,titleName):
        '''返回拟稿人操作'''
        # 查询公文名称
        self.findElement(*self.dbgw_query_btn_loc).click()
        self.findElement(*self.dbgw_queruwindow_title_input_loc).send_keys(titleName)
        time.sleep(2)
        self.findElement(*self.dbgw_queruwindow_query_loc).click()
        time.sleep(2)
        # 打开公文编辑页面
        self.findElement(*self.dbgw_result1_loc).click()
        self.switchtoframe("mainFrame", "main_frame2")
        # 向下滚动
        self.scrollToelement(*self.commondoc_remark_input_loc)
        # 输入处理意见方法1：
        self.findElement(*self.commondoc_opinion_input_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.driver.switch_to.frame(self.findElement(*self.opinion_iframe))
        self.findElement(*self.opinion_input_loc).send_keys(self.getXmlAttribute("testdataTYNW_fgld.xml", "fgldopinion", "value"))
        self.findElement(*self.opinion_confirm_loc).click()
        self.switchtoframe("mainFrame", "main_frame2")
        # 填写意见后，点击“返回拟稿人”按钮
        self.findElement(*self.fhngr_btn_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(2)
        self.findElement(*self.confirmBox_ok_button).click()
        time.sleep(1)

    def ngr_cwcl(self,titleName):
        '''拟稿人成文处理操作'''
        # 查询公文名称
        self.findElement(*self.dbgw_query_btn_loc).click()
        self.findElement(*self.dbgw_queruwindow_title_input_loc).send_keys(titleName)
        time.sleep(2)
        self.findElement(*self.dbgw_queruwindow_query_loc).click()
        time.sleep(2)
        # 打开公文编辑页面
        self.findElement(*self.dbgw_result1_loc).click()
        self.switchtoframe("mainFrame", "main_frame2")
        # 填写意见后，点击“成文处理”按钮
        self.findElement(*self.cwcl_btn_loc).click()

    def cwcl_fwdw(self,titleName):
        '''成文处理人发外单位操作'''
        self.dbgw_query(titleName)
        # # 点击接收按钮 '''成文处理接收人为1人，不点接收按钮'''
        # self.findElement_untilelementClickable(*self.receive_btn_loc).click()
        # time.sleep(0.5)
        # 打开公文编辑页面
        self.findElement(*self.dbgw_result1_loc).click()
        self.switchtoframe("mainFrame", "main_frame2")

        # 向下滚动，填写主送单位
        self.findElement_untilelementvisiable(*self.commondoc_remark_input_loc)
        self.scrollToelement(*self.commondoc_remark_input_loc)
        self.findElement_untilelementvisiable(*self.mainDelivery_select_loc).click()
        receiverlist = []
        receiverlist.append(self.getXmlAttribute("testdataTYNW_lcjbgsry.xml", "mainDelivery", "value"))
        self.selectReceiver(receiverlist)
        self.switchtoframe("mainFrame", "main_frame2")
        # 点击“发外单位”按钮
        self.findElement(*self.fwdw_btn_loc).click()
        self.driver.switch_to_default_content()
        time.sleep(1)
        self.findElement(*self.confirmBox_ok_button).click()


    def dbgw_query(self,titleName):
        '''查询公文名称'''
        self.findElement(*self.dbgw_query_btn_loc).click()
        self.findElement(*self.dbgw_queruwindow_title_input_loc).send_keys(titleName)
        time.sleep(2)
        self.findElement(*self.dbgw_queruwindow_query_loc).click()
        time.sleep(2)



    def selectReceiver(self,receiverlist):
        '''选择接收对象操作'''
        self.driver.switch_to_default_content()
        time.sleep(1)
        self.driver.switch_to.frame(self.findElement(*self.receiver_iframe))
        time.sleep(1)
        for receiver in receiverlist:
            self.findElement(*self.receiver_input_loc).clear()
            time.sleep(1)
            self.findElement(*self.receiver_input_loc).send_keys(receiver)
            time.sleep(1)
            self.findElement(*self.receiver_input_loc).send_keys(Keys.ENTER)
            time.sleep(2)
        self.findElement(*self.receiver_confirm_loc).click()
        time.sleep(3)