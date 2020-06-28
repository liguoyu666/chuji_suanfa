# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 上午9:45
# @Author  : liguoyu
# @FileName: 09.两数之和.py
# @Software: PyCharm

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def twoSum_1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)-1):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# 双指针（仅限于非重复有序列表的查询）
def twoSum_2(nums, target):
    result = []
    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] + nums[end] == target:
            result.append((start,end))
            break
        elif nums[start] + nums[end] < target:
            start += 1
        elif nums[start] + nums[end] > target:
            end -= 1
    return result


if __name__ == '__main__':
    nums = [2, 11, 7, 23]
    target = 9
    out = twoSum_1(nums, target)
    print(out)
    nums.sort()
    out_2 = twoSum_2(nums, target)
    print(out_2)