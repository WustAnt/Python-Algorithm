# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 11:43
# @Author  : WuatAnt
# @File    : tostr.py
# @Project : Python数据结构与算法分析
from stack import Stack

rStack = Stack()
def toStr(n,base):
    n = int(n)
    converString = '0123456789ABCDEF'
    if n < base:
        rStack.push(converString[n])
    else:
        rStack.push(converString[n % base])
        toStr(n // base,base)



if __name__ == '__main__':
    toStr(42,6)
    newString = ''
    while not rStack.isEmpty():
        newString = newString + rStack.pop()
    print(newString)
