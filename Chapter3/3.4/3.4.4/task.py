# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 10:24
# @Author  : WuatAnt
# @File    : task.py
# @Project : Python数据结构与算法分析
import random
class Task:
    def __init__(self,time):  #初始化打印任务
        self.timestamp = time  #时间戳。用于计算等待时间
        self.pages = random.randrange(1,21)  #随机生成1~21打印页数

    def getStamp(self):  #获取打印任务创建时的时间戳
        return self.timestamp

    def getPages(self):  #获取打印任务的页数
        return self.pages

    def waitTime(self,currenttime):  #根据创建时时间戳，计算任务在队列中等待的时间
        return currenttime - self.timestamp