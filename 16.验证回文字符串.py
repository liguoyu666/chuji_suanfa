# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 上午10:03
# @Author  : liguoyu
# @FileName: 16.验证回文字符串.py
# @Software: PyCharm

"""
验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false
"""

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.strip()
    l = []
    for i in s:
        if i.isalnum():
            l.append(i)
    return True if l == l[::-1] else False


if __name__ == '__main__':
    s = 'as fs,a!a'
    s2 = 'g. h f?f hg'
    out1 = isPalindrome(s)
    out2 = isPalindrome(s2)
    print(out1, out2)