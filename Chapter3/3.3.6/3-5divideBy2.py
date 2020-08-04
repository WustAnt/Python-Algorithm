# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 11:36
# @Author  : WuatAnt
# @File    : 3-5divideBy2.py
# @Project : Python数据结构与算法分析
from stack import Stack
"""
十进制数转换二进制数：
    使用‘除以2’算法，待处理整数大于0，循环不停地进行十进制除以2，并记录余数
    对应的二进制数，为余数，第一个余数是最后一位
"""
def divideBy2(decNumber):
    remstack = Stack()  #创建一个栈用于保存余数，利用其反转特性，得到二进制数

    while decNumber>0:
        rem = decNumber % 2  #取余
        remstack.push(rem)

        decNumber = decNumber//2

    binString = ''
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

if __name__ == '__main__':
    decNumber = 800
    print(decNumber,'-->',divideBy2(decNumber))