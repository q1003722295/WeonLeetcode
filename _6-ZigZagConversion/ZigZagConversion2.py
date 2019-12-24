'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
'''
# ！！！为什么一定要用二维数组存储呢  用一维字符串数组不好嘛！！！  完美！
class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):
        n = len(s)
        if numRows == 0 or numRows == 1:
            return s

        dp = [''] *numRows
        scov = ''
        i = j = 0
        while i < n:
            if j % (numRows - 1) == 0:
                for k in range(numRows):
                    if i >= n:
                        break
                    dp[k] += s[i]

                    i += 1
            else:
                k = k - 1
                dp[k] += s[i]
                i += 1
            j = j+1

        for i in range(numRows):
            scov = scov + dp[i]

        return scov


s = Solution()
print(s.convert("PAYPALISHIRING", 3))