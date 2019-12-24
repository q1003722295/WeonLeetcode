'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
'''


# 下边这个算法好啊！
'''
中心拓展法
回文串的中心可能是!!!一个字符或者两个字符!!!。因此，我们遍历每一个字符和每一对相邻的字符

1.特判，若ss长度为1或0，返回s

2.初试化最长回文子串的开始索引和结束索引start=0,end=0

3.拓展函数expand(l,r)，l表示传入中心字符的左界，r表示传入字符中心的右界。

    若满足条件0<=l and r<n and s[l]==s[r]，执行循环：向两侧拓展l-=1l−=1，r+=1r+=1
    返回回文串的长度r-l-1。注意！为什么是r−l−1?，r-1-(l+1)+1 = r-l-1
4.遍历s，遍历区间[0,n)：
    中心为一个字符的拓展后长度len\_1=expand(i,i)
    中心为两个字符的拓展后长度len\_2=expand(i,i+1)
    较长的子串长度len\_long=max(len\_1,len\_2)
    若满足len\_long>end-start+1，表示当前长度大于之前的最长长度，更新start和end
        start=i-(len\_long-1)//2
        end=i+len\_long//2
    解释！start和end的更新公式
    //表示向下取整
    因为有两种情况，拓展中心为一个字符或者两个字符。无论是一个还是两个，令字符串长度(len−1)//2总能得到拓展中心左侧元素的个数。
    同理，令len//2总能得到拓展中心右侧的个数。

5.返回s[start,...,end]s[start,...,end]
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while(0<=l and r<n and s[l]==s[r]):
                l-=1
                r+=1
            return r-l-1
        if(not s or len(s)==1):
            return s
        n=len(s)
        start=0
        end=0
        for i in range(n):
            len1=expand(i,i)
            len2=expand(i,i+1)
            len_long=max(len1,len2)
            if(len_long>end-start):
                start=i-(len_long-1)//2
                end=i+(len_long)//2
        return s[start:end+1]

