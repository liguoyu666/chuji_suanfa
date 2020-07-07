# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 下午4:40
# @Author  : liguoyu
# @FileName: 13.整数反转.py
# @Software: PyCharm

"""
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if -2**31 < x < 2**31 - 1:
        n = abs(x)
        s = str(n)
        s = s[::-1]
        if x < 0:
            return '-' + s
        else:
            return s
    else:
        return 0


if __name__ == '__main__':
    x1 = -1234
    x2 = 568
    out1 = reverse(x1)
    out2 = reverse(x2)
    print(out1, out2)