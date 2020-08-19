# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 16:13
# @Author  : WuatAnt
# @File    : decrypt.py
# @Project : Python数据结构与算法分析
def decrypt(m,k):
    """
    以轮换参数作为参数的解密函数
    :param m: 原文
    :param k: 轮换参数，称为’密钥‘
    :return: 加密后内容
    """
    s = 'abcdefghijklmnopqrstuvwxyz'
    n = ''
    for i in m:
        j = (s.find(i) + 26-k) % 26  # 对原文每个字母在字母表中移动13个位置
        n = n + s[j]
    return n

x = decrypt('uryybjbeyq',13)
print(x)