# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   NowCoder 
File Name：     1.search_in_2-D
Description :   在二维数组中的查找

题目描述：      在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
                每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
                判断数组中是否含有该整数。

Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-04-09 20:37
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-04-09:
-------------------------------------------------
"""


# 铺垫一下数组、矩阵
def show_example():
    a = [1, 2, 3, 4]                                # 一个数组
    b = [[1, 2, 3, 4],
         [5, 6, 7, 8]]                              # 这里就当表示了一个2维矩阵
    print "a is", a
    print "b is", b
    # 针对矩阵的行数 列数 进行输出有
    row_b = len(b)                                  # 矩阵b 的行数
    col_b = len(b[0])                               # 矩阵b 的列数
    print "num of row_b is", row_b
    print "num of col_b is", col_b
    # 这里要学一下 b[0] b[1] 索引是从0开始的
    print "1st row of b is", b[0]                   # [1, 2, 3, 4]
    print "2nd row of b is", b[1]                   # [5, 6, 7, 8]
    print "val of element b(1,2) is", b[0][1]       # 表示矩阵b的(x,y)元素，b[0][1]表示第一行 第二列所在元素值 理论值为2


show_example()


# array 二维列表
def Find(target, array):
    # write code here
    rows = len(array)
    cols = len(array[0])
    # 看一下矩阵的行数、列数，理论上应该是4x4
    print "num of row is", rows                     # 4
    print "num of col is", cols                     # 4
    if rows > 0 and cols > 0:
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if target == array[row][col]:           # 这里的判断“相等”关系的时候用“==”
                return True
            elif target < array[row][col]:          # 这里观察矩阵，目标值小于当前元素，那么说明在左侧/下侧 row加 col减
                col -= 1
            else:
                row += 1
    return False


Find(7, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
