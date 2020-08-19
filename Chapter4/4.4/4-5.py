# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:16
# @Author  : WuatAnt
# @File    : 4-5.py
# @Project : Python数据结构与算法分析
from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSpiral(myTurtle,lineLen):
    if lineLen > 0 :
        myTurtle.forward(lineLen)
        myTurtle.right(45)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()