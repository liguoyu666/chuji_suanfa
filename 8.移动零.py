# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 下午3:23
# @Author  : liguoyu
# @FileName: 8.移动零.py
# @Software: PyCharm

"""
移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


def moveZeroes_1(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zero_list = []
    for i, num in enumerate(nums):
        if num == 0:
            zero_list.append(i)
        elif len(zero_list) != 0:
            index = zero_list.pop(0)
            nums[i], nums[index] = nums[index], nums[i]
            zero_list.append(i)

    return nums


def moveZeroes_2(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    num_zero = 0
    for i in nums:
        if i == 0:
            nums.remove(i)
            num_zero += 1
    for j in range(len(num_zero)):
        nums.append(0)

    return nums


if __name__ == '__main__':
    L = [1,0,2,0,0,3]
    new_nums_1 = moveZeroes_1(L)
    new_nums_2 = moveZeroes_1(L)
    print(new_nums_1, new_nums_2)