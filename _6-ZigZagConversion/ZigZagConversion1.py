'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

'''

# 将Z图形保存在数组里 然后逐个打印
# 当列下标j%numRows-1 ==0时该列的元素为numsRows个  反之 则只有1个
# ！！！注意numsRows=1时  j%numsRows-1没法除！！！
class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):
        n = len(s)
        if numRows==0 or numRows==1:
            return s

        dp = [['']*n for _ in range(numRows)]
        scov = ''
        i = j = 0
        while i < n:
            if j % (numRows-1) == 0:
                for k in range(numRows):
                    if i >= n:
                        break
                    dp[k][j] = s[i]

                    i +=1
            else:
                k = k - 1
                dp[k][j] = s[i]
                i+=1
            j+=1

        for i in range(numRows):
            for j in range(n):
                if dp[i][j] != '':
                    scov = scov + dp[i][j]

        return  scov

s = Solution()
print(s.convert("PAYPALISHIRING", 3))