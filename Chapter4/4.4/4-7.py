# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 16:02
# @Author  : WuatAnt
# @File    : 4-7.py
# @Project : Python数据结构与算法分析
from turtle import *
import random

def drawTriangle(points, color ,myTurtle):
    myTurtle.fillcolor(color)  #填充颜色
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()  #开始填充
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()  #结束填充

def getMid(p1,p2):
    return ((p1[0]+p2[0]) /2, (p1[1]+p2[1]) /2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow','violet','orange']

    drawTriangle(points,random.choice(colormap),myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)
        sierpinski([points[1],
                    getMid(points[0],points[1]),
                    getMid(points[1],points[2])],
                   degree-1,myTurtle)
        sierpinski([points[2],
                    getMid(points[2],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)
        sierpinski([getMid(points[0], points[2]),
                    getMid(points[0],points[1]),
                    getMid(points[1], points[2])],
                   degree - 1, myTurtle)

myTurtle = Turtle()
myTurtle.speed(10)
myWin = myTurtle.getscreen()
mypoints = [(-500,-250),(0,500),(500,-250)]
sierpinski(mypoints,5,myTurtle)
myWin.exitonclick()
