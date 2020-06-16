# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 上午9:27
# @Author  : liguoyu
# @FileName: 05.只出现一次的数字.py
# @Software: PyCharm

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4
"""


def singleNumber_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in nums:
        if nums.count(i) == 1:
            return i


def singleNumber_2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = {}
    for i in nums:
        if i in s.keys():
            s.pop(i)
        else:
            s[i] = 1
    return list(s.keys())[0]


def singleNumber_3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in nums:
        res ^= i
        print(res)
    return res


def singleNumber_4(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = set(nums)
    sum_s = sum(s)
    sum_n = sum(nums)
    res = sum_s * 2 - sum_n
    return res


if __name__ == '__main__':
    nums = [2,3,4,5,3,4,2]
    y1 = singleNumber_1(nums)
    y2 = singleNumber_2(nums)
    y3 = singleNumber_3(nums)
    y4 = singleNumber_4(nums)
