from collections import defaultdict

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''
# 本来是想用字典防止超时
#但最后还是超时了   =o(m^3)<=o(n^3)但还是超时
#说白了还是暴力求解
#xxxxxxxxxx  不可取
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    def isPalindromic(self,l, r, str):
        left = l
        right = r
        while(left <= right):
            if str[left] != str[right]:
                return 0
            left+=1
            right-=1

        return r - l + 1

    def longestPalindrome(self, str):
        dic = defaultdict(list)
        left = right = 0
        maxsize = 0

        # for i in range(len(str)):
        for i, n in enumerate(str):
            dic[n].append(i)
            N = len(dic[n])
            if N >1:
                for j in range(N-1):
                    flag = self.isPalindromic(dic[n][j],dic[n][N-1], str)
                    if flag != 0 and flag > maxsize:
                        left = dic[n][j]
                        right = dic[n][N-1]
                        maxsize = flag
                        break

        # print(type(left))
        return str[left:right+1]


s = Solution()
print(s.longestPalindrome("ccc"))