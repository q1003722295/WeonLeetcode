'''
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。
'''

# 这题简单 但是注意各种条件的限制！！
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAXINT = 2 ** 31 - 1
        MININT = 2 ** 31

        i = 0
        flag = 0  # flag=0则为正 否则为负

        str = str.strip()
        n = len(str)

        # 字符串为空 直接返回0
        if str == "":
            return 0

        # # 将前面为' '的字符去除
        # while i < n and str[i] == ' ': #注意i<n必须写在前面！！！
        #         i += 1
        # if i >= n: #若都是' '则直接返回0
        #     return 0

        # 判断正负号
        if str[i] == '-':
            flag = 1
            i += 1
        elif str[i] == '+':
            i += 1

        # 正式开始转换
        x = 0
        while i < n:
            if str[i] <= '9' and str[i] >= '0':
                x = x * 10 + int(str[i])
            else:  # 遇到不是0-9的数字 直接返回  注意正负号
                if flag == 1:
                    return -x
                else:
                    return x

            if x > MAXINT and flag == 0:
                return MAXINT
            elif x > MININT and flag == 1:
                return -MININT

            i += 1

        if flag == 0:
            return x
        else:
            return -x



s = Solution()
print(s.myAtoi(" -22"))
























