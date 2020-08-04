# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 12:47
# @Author  : WuatAnt
# @File    : 3-7 infixToPostfix.py
# @Project : Python数据结构与算法分析
from stack import Stack
import string

"""
表达式中序转后序：
    [1]创建opStack空栈用于保存运算符，以及一个用于保存结果的空列表postfixList
    [2]使用字符串方法split(),将输入的中序表达式转换成一个列表，假设表达式是一个以空格分隔的标记串；
    [3]从左往右扫描这个标记列表：
        (1)如果标记是操作数，将其添加到结果列表的末尾，postfixList.append()；
        (2)如果标记是左括号，将其压入opStack栈中；
        (3)如果标记是右括号，循环从opStack栈中移除元素，并依次将移除的每一个运算符添加到结果列表末尾，
直到循环至对应的左括号；
        (4)如果标记的运算符，将其压入opStack栈中。但在这之前，需要先从栈中取出优先级更高或者相同优先级
的运算符，并将其添加到结果列表末尾
    [4]处理完表达式后，检查栈残留的运算符，将其全部添加到结果列表
"""
def infixToPostfix(infixexpr):
    prec = {
        '*':3,
        '/':3,
        '+':2,
        '-':2,
        '(':1
    }  #设置运算符优先级，默认以3,2,1，由高到低
    opStack = Stack()  #创建用于保存运算符的空栈
    postfixList = []  #创建用于保存结果的空列表

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in string.ascii_uppercase:  #使用string库包含所有大写字母的字符串，判断是否能为操作数
            postfixList.append(token)
        elif token == '(':   #是否为左括号，是将其压入栈
            opStack.push(token)
        elif token == ')':  #是否为右括号，是移除栈顶元素，并判断是否为对应的左括号
            topToken = opStack.pop()
            while topToken != '(':  #循环停止条件，找到对应的左括号
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty() and (prec[opStack.peek()] >= prec[token])):
                "循环条件：栈不为空且栈顶的运算符优先级大于等于当前运算符"
                postfixList.append(opStack.pop())
            opStack.push(token)  #将预算符压入栈

    while not opStack.isEmpty():  #处理完表达式后，检查栈残留的运算符，将其全部添加到结果列表
        postfixList.append(opStack.pop())

    return ''.join(postfixList)

if __name__ == '__main__':
    str = ' ( A + B ) * C - ( A - B ) * ( C + D ) '
    print(infixToPostfix(str))
    # ‘AB+C*AB-CD+*-’