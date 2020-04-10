# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   NowCoder 
File Name：     2.replace_blankspace
题目 :          请实现一个函数，将一个字符串中的每个空格替换成“%20”。
                例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
Description :
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-04-10 22:52
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-04-10:
-------------------------------------------------
"""


def replace(s):
    # write code here
    length_s = len(s)               # 长度
    list_s = list(s)                # 内容
    for i in range(0, length_s):
        if list_s[i] == ' ':        # 这里判断的 “ == ” 我又忘了，跑了好几次都不通过
            list_s[i] = '%20'
    print ''.join(list_s)           # 本地输出一下结果
    return ''.join(list_s)          # 添加进去


replace("hello  world")             # 包含两个空格


# 再来加几个扩展基础

