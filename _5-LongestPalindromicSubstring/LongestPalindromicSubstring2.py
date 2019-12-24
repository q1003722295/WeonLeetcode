
'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''
# 该题用 动态规划！！！！！！！  本身想到了但感觉不能用  其实是可以用的！！！！！！
'''
1特判，当s的长度为1或者0时，返回s。

2初试化最长回文子串的开始索引start和最长长度max_len=1

3初试化dp数组，为n*n，全部初始化为False。dp[i][j]表示s[i-j]是否为回文串。

4将dp中，所有单个字符处都是回文串，置为True。s中若相邻的字符串相同，则同样将着两个字符对应的位置置为True。即遍历s：
    dp[i][i]=True，表示单个字符一定是回文串。
    若i<n-1 and s[i]==s[i+1]，表示相邻的字符相同。则dp[i][i+1]=True，并更新最长回文子串的开始索引start=i和长度max_len=2

5此时，从长度3，开始遍历，遍历区间[3,n+1)，表示所有最长子串可能的长度。因为长度为1和2的已经在上一步找完了。对于可能的长度l：
    从索引0开始遍历，遍历区间[0,n-l+1)，对于开始索引i。**遍历区间解释：**因为开始索引为i，长度为l，则子串右侧索引为i+l-1，为了保证不越界，i+l-1<n，
即i<n-l+1
    令子串右侧索引r=i+l-1
    若满足s[i]==s[r] and dp[i+1][r-1]==True。表示子串s[i+1,...,r-1]为回文且s[i]==s[r]，说明s[i,...,r]也是回文。则此时，更新dp[i][r]=True，
并更新最长子串开始索引start=i和长度max_len=l
返回s[start,...,start+max_len−1]

'''
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, str):
        n = len(str)
        dp = [[False]*n for _ in range(n)]
        start = 0
        max_len = 1
        # 当回文串长度为1或2时
        for i in range(n):
            dp[i][i] = True
            if i < n-1 and str[i] == str[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
        # 当回文串长度大于2时
        for l in range(3, n+1):
            for i in range(n-l+1):
                r = i + l -1
                if dp[i+1][r-1] == True and str[i] == str[r]:
                    dp[i][r] = True
                    start = i
                    max_len = l


        return str[start:start + max_len ]


s = Solution()
print(s.longestPalindrome("babad"))