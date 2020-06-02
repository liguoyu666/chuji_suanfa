# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 下午3:58
# @Author  : liguoyu
# @FileName: 01.删除排序数组中的重复项.py
# @Software: PyCharm

# 删除排序数组中的重复项
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 示例 1:
# 给定数组 nums = [1,1,2],
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# 你不需要考虑数组中超出新长度后面的元素。


def removeDuplicates1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    temp_num = nums[0]
    count = 0
    for index, num in enumerate(nums[1:]):
        if temp_num == num:
            del nums[index - count]
            count += 1
        else:
            temp_num = num
    return len(nums)


def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    forth = 0
    back = 1
    while back <= len(nums) - 1:
        if nums[forth] == nums[back]:
            nums.pop(back)
        else:
            forth += 1
            back += 1
    return len(nums)


def removeDuplicates3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    length = 0
    for index in range(1,len(nums)):
        if nums[index] != nums[length]:
            length += 1
            nums[length] = nums[index]
    return length+1


if __name__ == '__main__':
    num_list = [1,1,2,3,3,4,4,4,5]
    y1 = removeDuplicates1(nums=num_list)
    y2 = removeDuplicates2(nums=num_list)
    y3 = removeDuplicates3(nums=num_list)
    print(y1,y2,y3)