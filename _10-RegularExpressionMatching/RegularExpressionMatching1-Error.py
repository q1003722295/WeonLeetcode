'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
'''


# cdaab   cdaab


# 考虑每一个的方法  不行！！！  第一容易少考虑  第二很麻烦  根本考虑不过来的！  这种方法错误！
# 这次的错误 主要是 *匹配几次出现了错误！！！
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ns = len(s)
        np = len(p)
        i = j = 0
        pre = ''
        while i < ns and j < np:
            if s[i] == p[j]:
                pre = s[i]
                i += 1
                j += 1
            else:
                if p[j] == '.':
                    pre = p[j]
                    i += 1
                    j += 1
                elif p[j] == '*':
                    if pre == s[i] or pre == '.':
                        stemp = s[i]
                        while i<ns and s[i] == stemp:
                            i += 1
                        j += 1
                    else:
                        j += 1
                elif j+1 < np and p[j+1] == '*':
                    j += 2
                elif j+1 < np and p[j+1] != '*':
                    return False

        if i < ns:
            return False
        elif i >= ns and j < np:
            while j < np:
                if p[j] != '*':
                    return False
        else:
            return True



S = Solution()
s = "aaa"
p = "a*a"
print(S.isMatch(s, p))
# 该是True  但输出是False  错误了









