# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 16:17
# @Author  : WuatAnt
# @File    : modexp.py
# @Project : Python数据结构与算法分析
def modexp(x,n,p):
    '对任意整数数x的n次幂关于模p的最后一位'
    if n == 0:  #对任意数x 的 0次幂等于1
        return 1
    t = (x * x) % p
    tmp = modexp(t,n//2,p)
    if n%2 != 0:
        tmp = (tmp * x) % p
    return tmp

print(modexp(2,6,2))