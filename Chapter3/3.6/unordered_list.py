# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 15:28
# @Author  : WuatAnt
# @File    : unordered_list.py
# @Project : Python数据结构与算法分析
"""
无序无序列表（unordered list）是基 于节点集合来构建的，每一个节点都通过显 式的引用指向下一个节点。
只要知道第一个节点的位置（第一个节点包含第一个元 素），其后的每一个元素都能通过下一个引用找到。
因此，UnorderedList 类必须包 含指向第一个节点的引用。注意，每一个无序列表对象都保存了指向无序列表头部的引用。
"""
from node import Node
class UnorderedList:
    "无序无序列表类本身不包含任何节点对象，而只有指向整个无序列表结构的第一个节点引用"
    def __init__(self):
        self.head = None  #无序无序列表只提供一个头部没有指向任何节点

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        "由于无序列表只提供一个入口(头部)，添加其他节点只能放到第一个元素，把已有的无序列表链接到该元素的后面"
        temp = Node(item)  #添加新结点
        temp.setNext(self.head)  #将新节点的next引用指向当前无序列表的第一个节点
        self.head = temp  #将原来无序列表的头节点指向，新创建的节点

    def length(self):
        "返回无序列表长度"
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        "查找元素item是否在无序列表中，返回布尔值"
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        "从无序列表中查找并删除item元素"
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:  #要删除的元素在头部时
            self.head = current.getNext  #修改无序列表的头部指向当前节点的next
        elif current == None:
            print('要删除的元素不在无序列表中')
        else:  #修改previous的next指向currrent的next
            previous.setNext(current.getNext())
            
    def append(self,item):
        "如果元素item不在列表中将其添加到列表尾部"
        previous = None
        current  = self.head
        found = False
        temp = Node(item)
        while (not found) and (current != None):
            if current.getData()  == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            previous.setNext(temp)

    def insert(self,pos,item):
        "将元素item插入到pos之前"
        previous = None
        current = self.head
        found = False
        temp = Node(item)
        while (not found) and (current != None):
            if current.getData() == pos:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found == False:
            print('要插入的位置未找到')
        elif previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setNext(current)

    def index(self,item):
        """
        返回元素item的位置，
        :param item:
        :return: 如果不在列表中返回None；否则，就返回item所在的节点Node
        """
        current = self.head
        while current != None:
            if current.getData() == item:
                return current
            else:
                current = current.getNext()
        return None

    def pop(self):
        "移除列表中的最后一个元素，如果列表为空返回None，否则返回移除的元素"
        p_previous = None
        previous = None
        current = self.head
        while current != None:
            p_previous = previous
            previous = current
            current = current.getNext()

        if self.head == None:  #列表为空，返回None
            return None
        else:
            if p_previous == None:  #列表长度为1
                self.head = None
            else:
                p_previous.setNext(None)  #删除previous节点
            return previous.getData()

    def pop(self,pos):
        "移除列表中的指定位置元素，如果列表为空返回None，否则返回移除的元素"
        previous = None
        current = self.head
        found = False
        while not found and current != None:
            if current.getData() == pos:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found == False:  #列表为空，返回None
            if self.head == None:
                print('列表为空')
            else:
                print('{0}--元素\'{1}\'不在无列表中，无法移除'.format(IndexError,pos))
            return None
        else:
            if previous == None:  #要移除的元素在列表头部
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
    l = [1,2]
    l.pop()
    mylist = UnorderedList()
    # mylist.add(1)
    # mylist.add(2)
    # mylist.add(3)
    # mylist.add(4)
    # mylist.add(5)
    print(mylist.item())
    # mylist.append(6)
    print(mylist.pop(1))
    print(mylist.item())
    # print(mylist.item())
    # print(mylist.item())









