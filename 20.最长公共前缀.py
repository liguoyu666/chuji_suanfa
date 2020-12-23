# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 下午4:07
# @Author  : liguoyu
# @FileName: 20.最长公共前缀.py
# @Software: PyCharm

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""

解释: 输入不存在公共前缀。
说明: 所有输入只包含小写字母 a-z 。
"""

# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     if len(strs) == 0:
#         return ""
#     elif len(strs) == 1:
#         return strs[0]
#     else:
#         a = min(strs)
#         b = max(strs)
#         for i in range(len(a)):
#             if a[i] != b[i]:
#                 return a[:i]
#         return a

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    import os
    return os.path.commonprefix(strs)


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    out = longestCommonPrefix(strs)
    print(out)