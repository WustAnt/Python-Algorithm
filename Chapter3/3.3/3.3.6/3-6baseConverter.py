# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 11:52
# @Author  : WuatAnt
# @File    : 3-6baseConverter.py
# @Project : Python数据结构与算法分析
from stack import Stack
"""
十进制数转换任意进制数：
    decNumber：接受任意非负整数
    base:要转换进制数
    使用‘除以N’算法，待处理整数大于0，循环不停地进行十进制除以N，并记录余数
    对应的N进制数，为余数，第一个余数是最后一位
"""
def baseConverter(decNumber,base):
    digits = '0123456789ABCDEF'  #十六进制使用十位数字及六个字母来表示，创建digits来对应相应字符

    remstack = Stack()  #创建一个栈用于保存余数，利用其反转特性，得到二进制数

    while decNumber>0:
        rem = decNumber % base  #取余
        remstack.push(rem)

        decNumber = decNumber//base

    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

if __name__ == '__main__':
    decNumber = 12
    print(decNumber,'-->',baseConverter(decNumber,16))