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
暴力求解
超时了
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        charac = True
        if (divisor<0 and dividend>0) or (divisor>0 and dividend<0):
            charac = False

        dividend = abs(dividend)
        divisor = abs(divisor)
        MAXINT = 2 ** 31 - 1


        if dividend < divisor:
            return 0

        if divisor == 1:
            if dividend > MAXINT:
                if charac == True:
                    return MAXINT
                else:
                    return -MAXINT-1
            if charac == True:
                return dividend
            else:
                return -dividend

        i=0
        dtemp = divisor

        while dtemp <= dividend:
            if dtemp > MAXINT:
                return MAXINT

            dtemp += divisor
            i = i+1


        if charac == True:
            return i
        else:
            return -i
