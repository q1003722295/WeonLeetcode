'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''
'''
关于如何提高效率快速逼近结果
举个例子：11 除以 3 。
首先11比3大，结果至少是1， 然后我让3翻倍，就是6，发现11比3翻倍后还要大，那么结果就至少是2了，那我让这个6再翻倍，得12，11不比12大，
吓死我了，差点让就让刚才的最小解2也翻倍得到4了。但是我知道最终结果肯定在2和4之间。也就是说2再加上某个数，这个数是多少呢？
我让11减去刚才最后一次的结果6，剩下5，我们计算5是3的几倍，也就是除法，看，递归出现了。
说得很乱，不严谨，大家看个大概，然后自己在纸上画一画，或者直接看我代码就好啦！
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def div(dividend, divisor):
            if dividend < divisor:
                return 0
            count = 1
            tdivisor = divisor

            while tdivisor+tdivisor <= dividend:
                count = count +count
                tdivisor = tdivisor + tdivisor


            return count + div(dividend-tdivisor, divisor)

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > INT_MIN:
                return -dividend
            return INT_MAX

        charac = True
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            charac = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        res = div(dividend, divisor)

        if charac > 0:
            return res if res < INT_MAX else INT_MAX

        else:
            return  -res


