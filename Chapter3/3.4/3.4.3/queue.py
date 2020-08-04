# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 8:55
# @Author  : WuatAnt
# @File    : queue.py
# @Project : Python数据结构与算法分析

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):  #在队列的尾部添加一个元素
        self.items.insert(0,item)

    def dequeue(self):  #从队列头部移除一个元素
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == '__main__':
   q = Queue()
   q.enqueue('Kitty')
   q.enqueue(2)
   q.enqueue(True)
   print(q.items)
   q.dequeue()
   print(q.items)
