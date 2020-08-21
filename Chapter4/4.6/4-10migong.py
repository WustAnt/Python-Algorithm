# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 16:07
# @Author  : WuatAnt
# @File    : 4-10migong.py
# @Project : Python数据结构与算法分析
from turtle import Turtle





class Maze():
    def __init__(self,mazeFlieName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFlie = open(mazeFlieName,'r')
        rowsInMaze = 0
        for line in mazeFlie:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape='turtle')
        setup(width=600, height=600)
        setworldcoordinates(-(columnsInMaze-1)/2-0.5),\
                             -(rowsInMaze-1)/2-0.5,\
                            (columnsInMaze-1)/2+0.5,\
                              (rowsInMaze-1)/2+0.5))

    def setworldcoordinates(param):
        pass

    def drawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'tan')
        self.t.color('black','blue')

    def drawCenteredBox(self, x, y, color):
        # tracer(0)
        self.t.up()
        self.t.goto(x-0.5, y-0.5)
        self.t.color('black',color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        # update()
        # tracer(1)

    def moveTurtle(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate, -y+self.yTranslate))
        self.t.goto(x+self.xTranslate, -y+self.yTranslate)

    def dropBredcrumb(self,color):
        self.t.dot(color)

    def updatePostion(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = col
        self.moveTurtle(col,row)
        if val == PATH_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
        if color:
            self.dropBredcrumb(color)

    def isExit(self,row,col):
        return (row == 0 or
                row ==self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1)

    def __getitem__(self, idx):
        return self.mazelist[idx]

def searchFrom(maze, startRow, startColum):
    maze.updatePostion(startRow,startColum)
    #检查基本情况
    #1.遇到墙
    if maze[startRow][startColum] == OBSTACLE:
        return False
    if maze[startRow][startColum] == TRIED:
        return False
    if maze.isExit(startRow,startColum):
        maze.updatePostion(startRow,startColum,PATH_OF_PATH)
        return True
    maze.updatePostion(startRow,startColum,TRIED)

    found = searchFrom(maze, startRow-1, startColum) or \
            searchFrom(maze, startRow+1, startColum) or \
            searchFrom(maze, startRow, startColum-1) or \
            searchFrom(maze, startRow, startColum+1)
    if found:
        maze.updatePostion(startRow,startColum,PATH_OF_PATH)
    else:
        maze.updatePostion(startRow,startColum,DEAD_END)
    return found

