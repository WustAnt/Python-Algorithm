# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 9:01
# @Author  : WuatAnt
# @File    : hotPotato.py
# @Project : Python数据结构与算法分析
"""
模拟传土豆游戏：
[1]创建一个用于保存孩子名字的空队列simqueue;
[2]假设握着土豆的孩子在队列头部，模拟传土豆过程中，程序将这个孩子移除队列然后从队列尾部插入队列；
[3]随后这个孩子会一直等待，直到再次到达队列的头部，在出列入列Num次后，此时位于队列头部的孩子出局，新一轮游戏开始；
[4]如此反复，直到队列只剩下一个名字
"""
from queue import Queue

def hotPotato(namelist,num):
    """
    :param namelist: 传入一个孩子名字的列表
    :param num: 循环次数
    :return: 返回最后剩下的孩子名字
    """
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())  #使用队列来模拟一个环，从队列头部移除从尾部入列

        simqueue.dequeue()  #出局，一轮游戏结束

    return simqueue.dequeue()  #返回剩下的一个孩子

if __name__ == '__main__':
    p = ['A','B','C','D','E','F','G']
    print(hotPotato(p,6))