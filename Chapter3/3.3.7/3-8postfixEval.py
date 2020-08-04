# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 19:23
# @Author  : WuatAnt
# @File    : 3-8计算后序表达式.py
# @Project : Python数据结构与算法分析
"""
[1]创建空栈operandStack；
[2]使用字符串方法split(),将输入的后序表达式转换成一个列表；
[3]从左往右扫面这个标记列表
    如果标记是操作数，将其转换成整数并且压入operandStack栈中；
    如果标记是运算符，从operandStack栈中取出两个操作数，第一个为右操作数，第二个为左操作数，计算结果压入operandStack栈中
[4]当处理完输入表达式时，返回栈中的结果。
"""
from stack import Stack
import string

def postfixEval(postfixExpr):
    operandStack = Stack()

    tokenList = postfixExpr.split() #假设表达式以空格间隔

    for token in tokenList:
        if token in string.digits:
            operandStack.push(int(token))
        else:
            try:  #operandStack栈不为空
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
            except:
                print('栈为空，表达式错误！')
                return False
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

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

if __name__ == '__main__':
    str = '1 1 + 2 * 3 3 - 2 3 + * -'
    print(postfixEval(str))