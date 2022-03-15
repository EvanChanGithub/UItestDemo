# -*- coding: utf-8 -*-
# @Time    : 2021-11-6 19:07
# @Author  : Evan
# @FileName:
# @Software: PyCharm
# @Function: 通用收文流程测试

import unittest
from selenium import webdriver
from page.initial import *
from page.ReceiveCommonDocument_Page import *
from page.login_Page import *
from selenium.webdriver.common.by import By
import time
import os
from base.basePage import *
from page.login_Page import Login
from testcase.gol import gol


class SendSendCommon(Init, ReceiveCommonDocument, Login, gol):

    # def test_a_draft(self):
    #     '''功能局办公室人员-纸质收文-通用收文流程'''
    #     # globals()["tileName"] = self.get_golvalue("titlename")
    #     globals()["tileName"] =  '''【2022-01-19-20:24】 测试通用拟文'''
    #     self.loginSystem("user5","chrome")
    #     self.zzsw_tysw_process()

    def test_b_fwdw(self):
        '''收文单位接收'''
        globals()["tileName"] = self.get_golvalue("titlename")
        self.loginSystem("user5", "chrome")
        self.swcl_tysw(globals()["tileName"])


        




if __name__ == '__main__':
    unittest.main(verbosity=2)


