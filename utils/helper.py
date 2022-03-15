# -*- coding: utf-8 -*-
# @Time    : 2021-11-6 19:07
# @Author  : Evan
# @FileName: helper.py
# @Software: PyCharm
# @Function:

import os
import xml.dom.minidom

class Helper(object):
    def dir_base(self, filelName, filePath = 'data'):
        # 获取data文件夹下的文件
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), filePath, filelName)

    def getXmlData(self, filename, value):
        '''
        读取单节点的数据
        :param value: xml中单节点的名称
        :return: 通过DOM对象，先获取该元素节点，再获取子文本节点，最后通过“data”属性获取文本内容
        '''
        dom = xml.dom.minidom.parse(self.dir_base(filename))
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[0]
        if nameValue.firstChild.nodeName == '#text':
            return nameValue.firstChild.data.replace('\t', '').replace('\n', '').replace('\r', '')
        else:
            return  nameValue.firstChild.data

    def getXmlAttribute(self, fileName, tagname, attributename):
        '''
        获取元素的属性值方法
        :param filename: 文件名
        :param tagname: 元素名称
        :param attributename: 属性名称
        :return: 属性值
        '''
        dom = xml.dom.minidom.parse(self.dir_base(fileName))
        db = dom.documentElement
        tagNodes = db.getElementsByTagName(tagname)
        if len(tagNodes) != 0:
            return tagNodes[0].getAttribute(attributename)


    def getXmlUser(self, filename, parent, child):
        '''
        获取父节点下的子节点的数据
        :param parent: 父节点
        :param child: 子节点
        :return: 返回第一个子节点的值
        '''
        dom = xml.dom.minidom.parse(self.dir_base(filename))
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        if  len(itemlist) != 0:
            return itemlist[0].getElementsByTagName(child)[0].childNodes[0].data.replace('\n', '')
        else:
            return None


    def getXmlList(self, fileName, parent):
        '''
        按指定文件指定父节点下的所有子节点
        :param fileName:
        :param tagName:
        :return:子节点集合
        '''
        dom = xml.dom.minidom.parse(self.dir_base(fileName))
        db = dom.documentElement
        childNodes = db.getElementsByTagName(parent)[0].childNodes
        # print(type(childNodes))
        # for node in childNodes:
        #     # 通过nodeName判断是否是文本
        #     if node.nodeName != '#text' and "{}".format(node.nodeName).index("user") != -1:
        #         for attr, attr_val in node.attributes.items():
        #             print('\t\t\t\t\t打印属性名称和值', attr, '=', attr_val)
        return childNodes

    def create_xml(self, filename):
        dom = xml.dom.minidom.Document()
        root = dom.createElement('root')
        root.setAttribute('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        dom.appendChild(root)
        with open(self.dir_base(filename), 'wb') as f:
            f.write(dom.toprettyxml(encoding='utf-8'))

    def write_xml(self, filename, parentName, childName, text):
        '''
         写入xml文档的方法
        :param filename: 文件名
        :param childName: 新增的子节点
        :param text: 节点文本
        '''
        dom = xml.dom.minidom.parse(self.dir_base(filename))
        db = dom.documentElement
        # 给根节点再创建子节点
        if len(dom.getElementsByTagName(parentName)) == 0:
            db.appendChild(dom.createElement(parentName))
        itemlist = dom.getElementsByTagName(parentName)
        text_node = dom.createElement(childName)
        itemlist[0].appendChild(text_node)
        text = dom.createTextNode(text)
        text_node.appendChild(text)
        # 保存文档了
        # f.close()
        with open(self.dir_base(filename), 'wb') as f:
            # dom.writexml(f, indent='', addindent='', newl='\n', encoding='utf-8')
            f.write(dom.toprettyxml(encoding='utf-8'))

    def splitstrTotuple(self,str,sep):
        '''
        字符串分割转成列表
        :param str:
        :param sep:
        :return:
        '''
        trans1 = str.split(sep)
        trans2 =()
        # for tuple1 in trans1:
        #     if tuple1 != ",":
        #         trans2 += (tuple1,)
        return trans1




if __name__ == '__main__':
    # print(Helper().getXmlData("cookies.xml",'username1'))
    # Helper().write_xml('cookies.xml','username1','cookies',"121212112212122212")
    # print(Helper().getXmlList("user.xml", 'user')[1].getAttribute("user-data-dir"))
    # print(Helper().getXmlAttribute("testdataCommonSend.xml", "menuName", "value" ))
    # print(Helper().getXmlUser("cookies.xml", 'djjgtest01','cookies'))
    # print(Helper().getXmlList("testdataxsdj.xml", 'username1').get)
    print(len( Helper().splitstrTotuple( "科长,股室负责人,科员,3333", ",")))
    print(Helper().splitstrTotuple("科长,股室负责人,科员,3333", ","))
