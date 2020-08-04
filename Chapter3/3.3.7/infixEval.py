# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 19:48
# @Author  : WuatAnt
# @File    : 直接计算中序表达式.py
# @Project : Python数据结构与算法分析
"""
直接计算中序表达式：
    [1]创建两个空栈，一个用于保存运算符opStack，另一个用于保存操作数oprandStack
    [2]使用字符串方法split(),将输入的中序表达式转换成一个列表，假设表达式是一个以空格分隔的标记串；
    [3]从左往右扫描这个标记列表：
        (1)如果标记是操作数，将其压入oprandStack栈中；
        (2)如果标记是左括号，将其压入opStack栈中；
        (3)如果标记是右括号，循环从opStack栈中移除元素及从oprandStack栈中移除两个操作数，并依次将移除的
每一个运算符和操作数作运算，将运算结果result压入oprandStack栈中，直到循环至对应的左括号；
        (4)如果标记的运算符，将其压入opStack栈中。但在这之前，需要先从栈中取出优先级更高或者相同优先级
的运算符，并从oprandStack栈中取出两个操作数作运算，将其运算结果压入oprandStack栈中
    [4]处理完表达式后，检查两个栈残留的运算符及操作数，依次取出作运算，将其运算结果压入oprandStack栈中
"""


from stack import Stack
import re

def doMath(op,op1,op2):
    #根据运算符进行简单计算，返回结果
    try:
        if op == '+':
            return op1 + op2
        elif op  == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        else:
            return op1 / op2
    except Exception as e:
        print(e)

def infixEval(infixexpr):
    oprandStack = Stack()  #创建用于保存操作数的空栈oprandStack
    opStack = Stack()  #创建用于保存运算符的空栈opStack

    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }  # 设置运算符优先级，默认以3,2,1，由高到低

    tokenList = infixexpr.split()
    for token in tokenList:
        if re.match():
            oprandStack.push(int(token))  #记得字符串转换成整数
        elif token == '(':  #左括号压入opStack栈
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':  #循环取出opStack栈中运算符，直至找到对应的左括号
                operand2 = oprandStack.pop()  #右操作数
                operand1 = oprandStack.pop()  #左操作数
                result = doMath(topToken,operand1, operand2)
                oprandStack.push(result)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                operand2 = oprandStack.pop()
                operand1 = oprandStack.pop()
                result = doMath(opStack.pop(), operand1, operand2)
                oprandStack.push(result)
            opStack.push(token)  # 将运算符压入opStack栈

    while (not opStack.isEmpty()) and (oprandStack.size() > 1):
        #检查两个栈残留的运算符及操作数，依次取出作运算，将其运算结果压入oprandStack栈中
        operand2 = oprandStack.pop()
        operand1 = oprandStack.pop()
        result = doMath(opStack.pop(), operand1, operand2)
        oprandStack.push(result)
    return oprandStack.pop()  #返回运算结果

if __name__ == '__main__':
    str = '( ( 1 + 2 ) * ( ( 1 + 2 ) / 5 ) )'
    print(infixEval(str))