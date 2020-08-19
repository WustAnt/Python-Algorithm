# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 16:06
# @Author  : WuatAnt
# @File    : encrypt.py
# @Project : Python数据结构与算法分析
def encrypt(m):
    '简单的取余加密函数'
    s = 'abcdefghijklmnopqrstuvwxyz'
    n = ''
    for i in m:
        j = (s.find(i) + 13) % 26  #对原文每个字母在字母表中移动13个位置
        n = n + s[j]
    return n


