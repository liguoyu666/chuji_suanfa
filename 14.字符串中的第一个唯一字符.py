# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 上午10:16
# @Author  : liguoyu
# @FileName: 14.字符串中的第一个唯一字符.py
# @Software: PyCharm

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
示例：
s = "leetcode"
返回 0
s = "loveleetcode"
返回 2
提示：你可以假定该字符串只包含小写字母。
"""


# def firstUniqChar(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     l = []
#     s = str(s)
#     for i in range(len(s)):
#         if s[i] not in l and s[i] not in s[i+1:]:
#             return i
#         l.append(s[i])
#     return -1

# def firstUniqChar(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     print([s.find(c) for c in 'abcdefghijklmnopqrstuvwxyz' if s.count(c) == 1])
#     return min([s.find(c) for c in 'abcdefghijklmnopqrstuvwxyz' if s.count(c) == 1] or [-1])

import collections

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    dic = collections.Counter(s)  # 使用字典
    print(dic)
    for i in range(len(s)):
        if dic[s[i]] == 1:  # 如果字典中value为1
            return i
    return -1


if __name__ == '__main__':
    s1 = "leetcode"
    s2 = "loveleetcode"
    s3 = "asdfdsfa"
    out1 = firstUniqChar(s1)
    out2 = firstUniqChar(s2)
    out3 = firstUniqChar(s3)
    print(out1,out2,out3)