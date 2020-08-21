# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 15:42
# @Author  : WuatAnt
# @File    : 4-8hanota.py
# @Project : Python数据结构与算法分析

from stack import Stack

def hanota(height,fromPole,withPole,toPole):
    """
    汉诺塔移动，利用三个栈fromPole,withPole,toPole来记录移动过程
    :param height: 塔高度，初始值等于fromPole.size
    :param fromPole: 起始栈
    :param withPole: 中间栈
    :param toPole: 最终栈
    :return: None
    """
    if height == 0:
        return
    hanota(height-1,fromPole,toPole,withPole)
    toPole.push(fromPole.pop())
    print(fromPole.items,'-->',withPole.items,'-->',toPole.items)
    hanota(height-1,withPole,fromPole,toPole)


if __name__ == '__main__':

    fromStack = Stack()  #起始栈
    withStack = Stack()  #中间栈
    toStack = Stack()  #最终栈
    '添加层数'
    fromStack.push('第六层')
    fromStack.push('第五层')
    fromStack.push('第四层')
    fromStack.push('第三层')
    fromStack.push('第二层')
    fromStack.push('第一层')
    print(fromStack.items)

    height = fromStack.size()
    hanota(height,fromStack,withStack,toStack)
    print(fromStack.items)
    print(withStack.items)
    print(toStack.items)