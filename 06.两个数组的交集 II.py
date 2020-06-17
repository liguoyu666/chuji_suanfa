# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 上午11:07
# @Author  : liguoyu
# @FileName: 06.两个数组的交集 II.py
# @Software: PyCharm

"""
 给定两个数组，编写一个函数来计算它们的交集。
示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""


def intersect_1(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    temp = []
    if len(nums1) < len(nums2):
        for i in nums1:
            if i in nums2:
                temp.append(i)
                nums2.remove(i)
    else:
        for j in nums2:
            if j in nums1:
                temp.append(j)
                nums1.remove(j)
    return temp


def intersect_2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()
    temp = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            temp.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return temp


if __name__ == '__main__':
    n_1 = [2,3,4,5,3,5,3]
    n_2 = [3,2,3,6,5]

    y1 = intersect_1(nums1=n_1,nums2=n_2)
    # print(n_1)
    y2 = intersect_2(nums1=n_1,nums2=n_2)
    # print(y1, y2)