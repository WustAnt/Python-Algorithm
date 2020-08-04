# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 11:43
# @Author  : WuatAnt
# @File    : 3-15palchecker.py
# @Project : Python数据结构与算法分析
"""
检测回文数：
[1]创建用于保存字符串的双端队列chardeque
[2]从左往右将字符床添加到队列末尾
[3]分别从前后端两端移除元素，并比较两个元素。只有两者相等时才继续；
[4]如果一直匹配第一个和最后一个元素，最终会处理完所有字符,或者剩下一个元素在队列中。任意一种结果都表明输入字符串是回文
"""
from deque import Deque

def palChecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True  #标识是否相等

    while chardeque.size() > 1 and stillEqual:
        '双端队列长度大于1，且两个元素相等才继续'
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False  #两个元素不等，stillEqual改为False

    return stillEqual  #返回布尔值