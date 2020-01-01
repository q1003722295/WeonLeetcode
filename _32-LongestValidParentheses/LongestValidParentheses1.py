'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

'''
'''
暴力求解法
超时！
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        ())()))
        '''

        def isValidPar(s, left, right):

            nlr = right - left + 1
            stack = [''] * n
            top = -1

            if nlr  == 0:
                return  False

            if nlr % 2 != 0:
                return False

            i = left
            while i <= right:
                if s[i] == '(':
                    stack[top + 1] = '('
                    top += 1
                else:
                    if top == -1:
                        return False

                    top -= 1

                i +=1

            if top != -1:
                return False

            return True

        max_long = 0
        n = len(s)
        for i in range(n-1):
            for j in range(i+1, n, 2):
                if isValidPar(s, i, j) and max_long < j - i + 1 :
                    max_long = j - i +1


        return max_long


s = Solution()
print(s.longestValidParentheses('(()((()((()()()()((((()()()()))))'))

