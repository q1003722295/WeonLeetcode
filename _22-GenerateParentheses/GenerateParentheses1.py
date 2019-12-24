'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
'''
递归回溯啊宝贝！
没想出来

回溯：当需要不断重复遍历的时候一定用回溯！！！ 一定是重复遍历！例：DFS， 树形结构！
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(S)
                return

            if left < n:
                backtrack(S + '(', left+1, right)

            if right < left:
                backtrack(S + ')', left, right+1)

        backtrack('', 0, 0)

        return ans


s = Solution()
print(s.generateParenthesis(3))



