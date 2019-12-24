'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

进阶:

你能不将整数转为字符串来解决这个问题吗？
'''

#不转换为字符串，负数直接为false
# 直接将数字翻转 若等于原来的数则true 否则false
# 变回了第7题

class Solution(object):
    def reverse(self, x):#x只为正整数
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = pow(2, 31)
        rev = 0
        t = x
        while t != 0:
            rev = rev * 10 + t % 10
            if rev > MAX_INT:
                return 0
            t = t // 10


        return rev

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        xrev = self.reverse(x)
        if x == xrev:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(121))