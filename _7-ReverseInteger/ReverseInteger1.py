'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

示例 1:

输入: 123
输出: 321
'''


# 很简单  循环一边每次整除 就是判断不越界就行 python没有越界 所以要自己设置一下
'''
# 注：java or c++判断越界问题：
if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = pow(2, 31)
        rev = 0
        t = x if x > 0 else -x
        while t != 0:
            rev = rev * 10 + t % 10
            if rev > MAX_INT:
                return 0
            t = t // 10


        return rev if x>0 else -rev


s = Solution()
print(s.reverse(123))
