# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:23
# @Author  : WuatAnt
# @File    : 4-6.py
# @Project : Python数据结构与算法分析
from turtle import *

myTurtle = Turtle()

def tree(branchLen, myTurtle):
    if branchLen > 5:
        myTurtle.forward(branchLen)
        myTurtle.right(20)
        tree(branchLen-15, myTurtle)
        myTurtle.left(40)
        tree(branchLen-10, myTurtle)
        myTurtle.right(20)
        myTurtle.backward(branchLen)

if __name__ == '__main__':
    myWin = myTurtle.getscreen()
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(300)
    myTurtle.down()
    myTurtle.color('red')
    myTurtle.speed(1)
    tree(40,myTurtle)
    myWin.exitonclick()