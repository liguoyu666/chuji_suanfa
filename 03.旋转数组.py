# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 上午9:56
# @Author  : liguoyu
# @FileName: 03.旋转数组.py
# @Software: PyCharm


# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。


def rotate_1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    new_nums = nums.copy()
    for i in range(len(nums)):
        offset = i + k
        if offset >= len(nums):
            offset = i + k - len(nums)
        new_nums[offset] = nums[i]
    return new_nums


def rotate_2(nums, k):
    length = len(nums)
    new_nums = nums[length-k:] + nums[:length-k]
    return new_nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    y1 = rotate_1(nums,k)
    y2 = rotate_2(nums,k)
    print(y1, y2)