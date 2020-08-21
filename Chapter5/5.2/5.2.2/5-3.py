# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 17:10
# @Author  : WuatAnt
# @File    : 5-3.py
# @Project : Python数据结构与算法分析

def binarySearch(list,item):
    '有序列表的二分查找'
    first = 0
    last = len(list)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found