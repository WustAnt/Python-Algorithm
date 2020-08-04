# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 8:52
# @Author  : WuatAnt
# @File    : deque.py
# @Project : Python数据结构与算法分析



class Deque:
    def __init__(self):
        self.items = []  #使用列表来保存队列

    def isEmpty(self):
        '检查双端队列是否为空,返回布尔值'
        return self.items == []

    def addFront(self, item):
        '将一个元素添加到双端队列的前端'
        self.items.append(item)

    def addRear(self, item):
        '将一个元素添加到双端队列的后端'
        self.items.insert(0,item)

    def removeFront(self):
        '从双端队列前端移除一个元素'
        return self.items.pop()

    def removeRear(self):
        '从双端队列后端移除一个元素'
        return self.items.pop(0)

    def size(self):
        '返回双端队列的长度'
        return len(self.items)

if __name__ == '__main__':
    q  = Deque()
    q.addRear(1)
    q.addFront(2)
    print(q.items)
    print(q.size())
    q.removeFront()
    print(q.items)
