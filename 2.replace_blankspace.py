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
# 不同整型数据类型在内存中占多大（字节）
a = 2
b = 4
c = 8
d = 8
print ('The size of short is %d bytes.' % a)        # short 2 bytes
print ('The size of int is %d bytes.' % b)          # int   4 bytes
print ('The size of long is %d bytes.' % c)         # long  8 bytes
print ('The size of long long is %d bytes.' % d)    # long long 8 bytes


# 带编号输出相应字符指令
d = 'data'
# main = ('Define', 'Input', 'Process', 'Output')
ll = ['Define', 'Input', 'Process', 'Output']     # 这里是列表 用 [] 不是 ()
count = 1
for i in ll:
    if count == 4:
        print (str(count)+'. '+'%s data.' % i)
    else:
        print (str(count)+'. '+'%s data;' % i)
    count += 1


