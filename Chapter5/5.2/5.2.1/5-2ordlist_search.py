# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 17:07
# @Author  : WuatAnt
# @File    : 5-2ordlist_search.py
# @Project : Python数据结构与算法分析

def orderedSquentialSearch(alist,item):
    '有序列表的顺序搜索，返回布尔值。默认是升序'
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:  #判断当前值是否大于item。是：停止搜索
                stop = True
            pos = pos + 1

    return found