# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   NowCoder 
File Name：     3.print_end_to_head
题目：          输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
Description :   
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-04-11 21:02
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-04-11:
-------------------------------------------------
"""


# 返回从尾部到头部的列表值序列，例如[1,2,3]
def printListFromTailToHead(listNode):
    # write code here
    temp_list = []
    head_list = listNode
    while head_list:
        temp_list.insert(0, head_list.val)
        head_list = head_list.next
    return temp_list

