# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 15:12
# @Author  : WuatAnt
# @File    : node.py
# @Project : Python数据结构与算法分析
"""
为了实现无序列表，我们要构建链表 。
无序列表需要维持元素之间的相对位置，但是并不需要在连续的内存空间中维护这些位置信息。
"""
class Node:
    "创建节点类，节点包含列表元素及指向下一个节点的引用"
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext