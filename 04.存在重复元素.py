# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 下午2:23
# @Author  : liguoyu
# @FileName: 04.存在重复元素.py
# @Software: PyCharm

# 给定一个整数数组，判断是否存在重复元素。
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
#
# 输入: [1,2,3,1]
# 输出: true
#
# 输入: [1,2,3,4]
# 输出: false
#
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true


def containsDuplicate_1(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return False if len(nums) == len(set(nums)) else True


def containsDuplicate_2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    numsdic = {}
    for i in nums:
        if i not in numsdic:
            numsdic[i] = True
        else:
            return True
    return False


def containsDuplicate_3(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True

    return False


if __name__ == '__main__':
    nums_1 = [1,2,3,4]
    nums_2 = [1,2,3,2,4]
    y1 = containsDuplicate_1(nums_1)
    y2 = containsDuplicate_1(nums_2)
    y3 = containsDuplicate_2(nums_1)
    y4 = containsDuplicate_2(nums_2)
    y5 = containsDuplicate_3(nums_1)
    y6 = containsDuplicate_3(nums_2)
    print(y1,y2,y3,y4,y5,y6)