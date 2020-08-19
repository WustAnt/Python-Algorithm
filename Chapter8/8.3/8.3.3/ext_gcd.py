# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 11:17
# @Author  : WuatAnt
# @File    : ext_gcd.py
# @Project : Python数据结构与算法分析
def ext_gcd(x,y):
    if y == 0:
        return (x,1,0)
    else:
        (d,a,b) = ext_gcd(y,x%y)
        return (d,b,a-(x//y)*b)

print(ext_gcd(25,9))