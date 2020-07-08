# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 下午2:43
# @Author  : liguoyu
# @FileName: 15.有效的字母异位词.py
# @Software: PyCharm

"""
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true
示例 2:
输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    out1 = isAnagram(s,t)
    print(out1)