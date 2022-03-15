# -*- coding: utf-8 -*-
# @Time    : 2022-1-18 17:11
# @Author  : Evan
# @FileName: gol.py
# @Software: PyCharm
# @Function:


class gol():
    global _global_dict
    _global_dict = {}

    def set_golvalue(self,key, value):
        """ 定义一个全局变量 """
        _global_dict[key] = value

    def get_golvalue(self,key, defValue=None):
        """ 获得一个全局变量,不存在则返回默认值 """
        try:
            return _global_dict[key]
        except KeyError:
            return defValue
