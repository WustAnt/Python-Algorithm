# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 11:25
# @Author  : WuatAnt
# @File    : 3-4parChecker.py
# @Project : Python数据结构与算法分析

from stack import Stack
"""
匹配括号：
由一个空栈开始，从左往右依次处理括号；
[1] 如果遇到左括号，便将其压入栈，.push()
[2] 如果遇到右括号，检测是否与栈顶的左括号匹配，
    如果两个符号不匹配，那么整个字符串也不匹配，balanced=False,
只要栈中的所有左括号都能遇到与之对应的右括号，那么整个字符串就是匹配的；
如果栈中的有任何一个左括号找不到与之对应的右括号，字符串则不匹配；
处理完全匹配完的字符串之后，栈应该是空的。
"""


def matches(open, close):
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)  #若左右括号对应的位置相同，返回True


def parCherer(symbolString):
    "判断字符串是否匹配，返回一个布尔值"
    s = Stack()
    balanced = True  #设置标识，标记字符串是否符合规则，初始值为True
    index = 0  #字符位置
    while index<len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '({[':  #判断如果是左括号,压入栈
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():  #如果所有括号匹配完且栈为空，返回True
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = '({[]}([]))'
    str2 = '({[}]())'

    print(str1,':',parCherer(str1))
    print(str2,':',parCherer(str2))