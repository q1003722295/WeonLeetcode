'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''


# 采用滑动窗口的思想
from collections import defaultdict

class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    def lengthOfLongestSubstring(self, s):
        dic = defaultdict(int) #运用字典记录在前面是否有该元素  有为1 没有为0
        left = right = 0 #左右滑动指针
        templen = maxlen = 0  #记录当前长度和最大长度

        for right in range(len(s)):
            if dic[s[right]] != 0:  #已经存在该元素
                for i in range(left, right):
                    if s[i] == s[right]:
                        left = i+1 #将前面的字典中的元素都置为0  也就是代表滑动窗口到存在该元素的下一个元素上
                        break
                    dic[s[i]] = 0


                maxlen = maxlen if maxlen > templen else templen  #记录最大元素
                templen = right - left + 1 #当前长度


            else:
                dic[s[right]] = 1
                templen += 1

        maxlen = maxlen if maxlen > templen else templen

        return maxlen


