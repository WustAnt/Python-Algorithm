# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 17:14
# @Author  : WuatAnt
# @File    : 5-4.py
# @Project : Python数据结构与算法分析

def binarySearch(list,item):
    '有序列表的二分搜索递归版本'
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == item:
            return True
        else:
            if item < list[midpoint]:
                return binarySearch(list[:midpoint], item)
            else:
                return binarySearch(list[midpoint+1:], item)