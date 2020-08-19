# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 16:26
# @Author  : WuatAnt
# @File    : gcd.py
# @Project : Python数据结构与算法分析

def gcd(x,y):
    '利用欧几里得算法求最大公约数'
    if y == 0:
        return x
    elif x < y:
        return gcd(y,x)
    else:
        return gcd(x-y, y)

def euclid_gcd(x,y):
    '改良后的欧几里得算法'
    if y == 0:
        return x
    else:
        return euclid_gcd(y, x%y)


