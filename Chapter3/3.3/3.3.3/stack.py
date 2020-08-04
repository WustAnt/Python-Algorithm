# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 9:25
# @Author  : WuatAnt
# @File    : stack.py
# @Project : Python数据结构与算法分析
"""
Stack()使用列表保存数据，默认将列表的尾部作为栈的顶端
"""
class Stack:
    """
    Stack():创建空栈
    .push(item):将一个元素添加到栈的顶端
    .pop():将栈顶端的元素移除，返回一个参数item
    .peek():返回栈顶端的元素
    .isEmpty():检查栈是否为空，返回布尔值
    .size():返回栈中元素的数目
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
