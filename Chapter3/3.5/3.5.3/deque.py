# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 8:52
# @Author  : WuatAnt
# @File    : deque.py
# @Project : Python数据结构与算法分析



class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
