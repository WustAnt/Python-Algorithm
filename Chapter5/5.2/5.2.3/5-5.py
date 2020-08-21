# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 17:18
# @Author  : WuatAnt
# @File    : 5-5.py
# @Project : Python数据结构与算法分析

def hash(string, tablesize):
    """
    为字符串构建简单的散列函数
    :param string: 传入一个字符串
    :param tablesize: 散列表的大小
    :return: 返回散列值
    """
    sum = 0
    for pos in range(len(string)):
        sum = sum + ord(string[pos])  #ord(): Return the Unicode code point for a one-character string.

    return  sum % tablesize