# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 上午11:16
# @Author  : liguoyu
# @FileName: 07.加一.py
# @Software: PyCharm

"""
加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


def plusOne_1(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    length = len(digits)
    sum = 0
    for i in range(1,length+1):
        sum += digits[-i] * 10**(i-1)
    sum += 1
    new_dig = []
    for j in str(sum):
        new_dig.append(j)
    return new_dig


def plusOne_2(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    extra = 0
    one = 1
    digits = digits[::-1]
    for index, num in enumerate(digits):
        if num + one + extra == 10:
            extra = 1
            one = 0
            digits[index] = 0
        else:
            digits[index] = num + one + extra
            one = 0
            extra = 0

    return digits[::-1]


if __name__ == '__main__':
    dig_list = [1,2,9,4,9]
    y1 = plusOne_1(dig_list)
    y2 = plusOne_2(dig_list)
    print(y1, y2)