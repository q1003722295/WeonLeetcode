'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

示例 1:

输入: 123
输出: 321
'''

# 利用python强大功能的赖皮解法
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = int(str(abs(x))[::-1])
        if (num >= -2 ** 31) and (num <= 2 ** 31 - 1):
            if x < 0:
                return -num
            else:
                return num
        else:
            return 0


s = Solution()
print(s.reverse(123))