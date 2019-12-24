'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z
'''
'''
水平扫描法
我们从前往后枚举字符串的每一列，先比较每个字符串相同列上的字符（即不同字符串相同下标的字符）然后再进行对下一列的比较。
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        s = ''
        n = len(strs)
        j=0
        while j < len(strs[0]):
            for i in range(1, n):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return s


            s = s + strs[0][j]
            j += 1

        return s

s = Solution()
print(s.longestCommonPrefix(["aa","a"]))