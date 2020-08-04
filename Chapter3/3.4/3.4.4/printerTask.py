# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 9:36
# @Author  : WuatAnt
# @File    : printerTask.py
# @Project : Python数据结构与算法分析

from queue import Queue
import random
from printer import Printer
from task import Task

def simulation(numSeconds,pagesPerMinute):
    """
    :param numSeconds:
    :param pagesPerMinute: 每分钟打印页数
    """
    labprinter  = Printer(pagesPerMinute)  #
    printQueue = Queue()  #打印队列
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrinterTask():  #
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingtimes.append(nextTask.waitTime(currentSecond))
            labprinter.startNext(nextTask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)

    print('AvarageWait %6.2f seconds %3d tasks remaing.'%(averageWait,printQueue.size()))



def newPrinterTask():
    #判断是否有新创建的打印任务
    num = random.randrange(1,181)  #模拟平均180秒，有一次打印任务
    if num == 180:
        return True
    else:
        return False

if __name__  == '__main__':
    for i in range(10):
        simulation(3600,5)