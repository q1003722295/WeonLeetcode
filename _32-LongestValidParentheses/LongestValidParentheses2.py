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
动态规划
1特判，若s为空，返回0

2初试化dp=[0,...,0]，长度为n。dp[i]表示到i位置的最长有效括号的长度。
显然，当s[i]为(时，dp[i]=0

3遍历字符串，遍历区间[1,n)：

    当s[i]==)时，若s[i−1]==(，说明这两个有效。则dp[i]=dp[i-2]+2
    
    否则s[i-1]==)，此时找到上一匹配字符串的上一位i-dp[i-1]-1:
        若s[i-dp[i-1]-1]==(，说明s[i]s[i]可以和s[i-dp[i-1]-1]匹配：则dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2，
        表示当前位置的最长有效括号长度等于上一位有效括号的长度加上自身匹配的上一位的有效括号的长度加上2。
        
    更新res，res=max(res,dp[i])
    
4返回res

'''

class Solution:
    def longestValidParentheses(self, s):
        if(not s):
            return 0
        res=0
        n=len(s)
        dp=[0]*n
        for i in range(1,len(s)):
            if(s[i]==")"):
                if(s[i-1]=="("):
                    dp[i]=dp[i-2]+2
                if(s[i-1]==")" and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="("):
                    dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
                res=max(res,dp[i])
        return res


s = Solution()
print(s.longestValidParentheses('(()((()((()()()()((((()()()()))))'))