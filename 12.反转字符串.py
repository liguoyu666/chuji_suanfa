# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 下午4:17
# @Author  : liguoyu
# @FileName: 12.反转字符串.py
# @Software: PyCharm

"""
反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""
from functools import reduce


def reverseString_1(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    return s[::-1]


def reverseString_2(s):
    s.reverse()


def reverseString_3(s):
    return reduce(lambda x,y: y+x, s)


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    out = reverseString_1(s)
    print(out)

    print(s)
    reverseString_2(s)
    print(s)

    out_3 = reverseString_3(s)
    print(out_3)