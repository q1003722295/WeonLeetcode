'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false

'''
'''
暴力递归回溯法
超时
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


        def _isMatch(s, p, s_i, p_i):
            if s_i == len(s) and p_i == len(p):
                return True
            elif s_i != len(s) and p_i == len(p):
                return False
            elif s_i == len(s) and p_i != len(p):
                for i in range(p_i, len(p)):
                    if p[i] != '*':
                        return False
                return True


            i = s_i
            j = p_i
            while i<len(s) and j < len(p):
                if p[j]  == '*':
                    while j+1<len(p) and p[j+1] =='*':
                        j+=1

                    for skip in range(0, len(s) - i + 1 ):
                        if _isMatch(s, p, i + skip, j + 1):
                            return True

                    return False

                else:
                    if not (s[i] == p[j] or p[j] == '?'):
                        return False

                    i += 1
                    j += 1

            if i == len(s) and j == len(p):
                return True
            elif i != len(s) and j == len(p):
                return False
            elif i == len(s) and j != len(p):
                for k in range(j, len(p)):
                    if p[k] != '*':
                        return False
                return True

        return _isMatch(s, p, 0, 0)

s = Solution()
print(s.isMatch("babbaabbaaabbaabbbaaa", "*****aab"))
