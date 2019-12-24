'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''


'''
与以前做过的一个手撕分词（已导入）类似
回溯算法！！  关键想清楚第一步和最后一步 其他的递归只考虑当前
'''
class Solution(object):


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicDigits = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                     '9': 'wxyz'}

        def _letterCombinations(self, digits):
            res = []

            n = len(digits)
            if n == 0:
                return []

            if n > 1:
                firstsel = dicDigits[digits[0]]
                for ds in firstsel:
                    res = res + [(ds + dsnext) for dsnext in _letterCombinations(self, digits[1:n])]
            else:
                firstsel = dicDigits[digits[0]]
                return  firstsel

            return res
        res = []
        return _letterCombinations(self,digits)

s = Solution()
arr = s.letterCombinations('234')
print(arr)
print(len(arr))