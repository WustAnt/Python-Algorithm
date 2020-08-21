# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 17:03
# @Author  : WuatAnt
# @File    : 5-1.py
# @Project : Python数据结构与算法分析

def squentialSearch(alist,item):
    '无序列表的顺序搜索，返回布尔值'
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found
