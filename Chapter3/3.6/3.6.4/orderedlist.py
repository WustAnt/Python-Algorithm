# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 10:49
# @Author  : WuatAnt
# @File    : orderedlist.py
# @Project : Python数据结构与算法分析

from node import Node
class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        "检查列表是否为空，返回布尔值"
        return self.head == None

    def length(self):
        "返回无序列表长度"
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self,item):
        "移除列表中的元素item"
        current = self.head
        previous = None
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:  # 查找到元素
                found = True
            elif current.getData() > item:  # 有序列表，发现当前元素比要查找的大，停止查找
                stop = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:  #item在头部
            self.head = current.getNext()
        elif stop == True or current == None:  #没有找到item
            print('要删除的元素%s不在列表中'%item)
        else:  #已找到item,修改列表删除
            previous.setNext(current.getNext())

    def search(self,item):
        "在列表中搜索元素item,返回布尔值"
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:  #查找到元素
                found = True
            elif current.getData() > item:  #有序列表，发现当前元素比要查找的大，停止查找
                stop = True
            else:
                current = current.getNext()
        return found

    def index(self,item):
        "返回item该元素在列表中的位置,如果不在列表中返回None；否则，就返回item所在的节点Node"
        current = self.head
        while current != None:
            if current.getData() == item:
                return current
            elif current.getData() > item:
                return None
            else:
                current = current.getNext()
        return None

    def pop(self):
        "移除列表中最后一个元素"
        p_previous = None
        previous = None
        current = self.head
        while current != None:
            p_previous = previous
            previous = current
            current = current.getNext()

        if self.head == None:  # 列表为空，返回None
            return None
        else:
            if p_previous == None:  # 列表长度为1
                self.head = None
            else:
                p_previous.setNext(None)  # 删除previous节点
            return previous.getData()


    def pop(self,pos):
        "移除指定位置上的元素"
        previous = None
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == pos:
                found = True
            elif current.getData() > pos:
                stop = True
            else:
                previous = current
                current = current.getNext()

        if self.head == None:
            print('列表为空')
        elif stop == True or found == False:
            print('在列表中查找不%s位置'%pos)
            return None
        elif found == True and previous == None:  # 要移除的元素在列表头部
            self.head = current.getNext()
            return None
        else:
            previous.setNext(current.getNext())
            return pos

    def item(self):
        "仅为了测试时方便打印使用"
        item = []
        current = self.head
        while current != None:
            item.append(current.getData())
            current = current.getNext()
        return item

if __name__ == '__main__':
    p = OrderedList()
    print(p.isEmpty())

    p.add(1)
    p.add(3)
    p.add(2)
    p.add(5)
    p.add(4)
    print(p.item())
    p.pop()
    print(p.item())
