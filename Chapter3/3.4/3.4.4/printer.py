# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 10:19
# @Author  : WuatAnt
# @File    : printer.py
# @Project : Python数据结构与算法分析
class Printer:
    #创建Printer类，模拟打印机
    def __init__(self,ppm):
        self.pagerate = ppm  #构造打印机时，初始化打印速度，即每分钟打印多少页
        self.currentTask = None
        self.timeRemaining = 0  #打印所需时间

    def tick(self):
        if self.currentTask != None:  #打印工作时，会减量计时
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0 :  #打印完成后将打印机设置为空闲状态
                self.currentTask = None

    def busy(self):  #检查打印机当前是否有待完成的任务，如果有，那么打印机就处于工作状态
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):  #新建打印任务，传入Task类
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate  #设置打印所需时间