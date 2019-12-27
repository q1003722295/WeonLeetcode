'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

'''

'''
KMP算法  我不会！！！！！
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        # generate pnext
        i, k, m = 0, -1, len(needle)
        pnext = [-1] * m
        while i < m - 1:
            if k == -1 or needle[i] == needle[k]:
                i, k = i + 1, k + 1
                if needle[i] == needle[k]:
                    pnext[i] = pnext[k]
                else:
                    pnext[i] = k
            else:
                k = pnext[k]

        # matching
        h, j = 0, 0
        n = len(haystack)
        while h < m and j < n:
            if h == -1 or needle[h] == haystack[j]:
                h, j = h + 1, j + 1
            else:
                h = pnext[h]
        if h == m:
            return j - h
        return -1