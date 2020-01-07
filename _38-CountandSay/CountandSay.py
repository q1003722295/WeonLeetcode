'''
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"

'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def _countAndSay(prestr):
            n = len(prestr)
            if n == 1:
                return '11'

            res = ''
            nums = 1
            for i in range(n-1):
                if prestr[i] == prestr[i+1]:
                    nums+=1
                else:
                    res = res +  '{}{}'.format(nums, prestr[i])
                    nums = 1

            res += '{}{}'.format(nums, prestr[n-1])

            return res

        res = '1'
        for i in range(n-1):
            res = _countAndSay(res)

        return res



s = Solution()
print(s.countAndSay(5))