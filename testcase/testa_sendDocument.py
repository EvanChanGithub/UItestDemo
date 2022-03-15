# -*- coding: utf-8 -*-
# @Time    : 2021-11-6 19:07
# @Author  : Evan
# @FileName:
# @Software: PyCharm
# @Function: 通用发文流程测试

import unittest
from selenium import webdriver
from page.initial import *
from page.SendCommonDocument_Page import *
from page.ReceiveCommonDocument_Page import *
from page.login_Page import *
from selenium.webdriver.common.by import By
import time
import os
from base.basePage import *
from page.login_Page import Login
from testcase.gol import gol


class SendSendCommon(Init, SendCommonDocument, Login, gol):


    def test_a_draft(self):
        '''科员拟稿，送流程局科长'''
        self.loginSystem("user1","ie")
        globals()["tileName"] = self.saveCommonDoc()
        self.set_golvalue("titlename", globals()["tileName"])
        self.driver.quit()
        # tileName = "【2021-12-15-13:35】 测试通用拟文"
        self.loginSystem("user1", "chrome")
        self.editDocument(globals()["tileName"])




    def test_b_ksfzr_approve(self):
        '''科室/股室负责人审批，送流程局局长'''
        # titleName =  "【2021-12-16-13:59】 测试通用拟文"
        self.loginSystem("user2", "chrome")
        self.ksfzrTofgld(globals()["tileName"])
        # self.ksfzrTofgld(titleName)


    def test_c_jz_approve(self):
        '''局长审核'''
        # titleName = "【2021-12-16-13:59】 测试通用拟文"
        self.loginSystem("user3", "chrome")
        self.fgldTongr(globals()["tileName"])
        # self.fgldTongr(titleName)


    def test_d_ky_send(self):
        '''科员成文处理'''
        # titleName = "【2021-12-16-13:59】 测试通用拟文"
        self.loginSystem("user1", "chrome")
        self.ky_cwcl(globals()["tileName"])
        # self.ky_cwcl(titleName)

    def test_e_ky_swdw(self):
        '''科员送外单位，办公室人员'''
        # titleName = "【2021-12-21-09:24】 测试通用拟文"
        self.loginSystem("user4", "chrome")
        self.ky_swdw(globals()["tileName"])
        # self.ky_swdw(titleName)







if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromModule(Helper().dir_base("test_sendDocument.py", filePath='testcase'))
    # unittest.TextTestRunner(verbosity=2).run()

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # 加载测试类
    suite.addTest(loader.loadTestsFromTestCase(SendSendCommon))
