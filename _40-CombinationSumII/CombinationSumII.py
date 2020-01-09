'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''
'''
依旧试试用递归回溯 dfs
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def _combinationSum(candidates, candstart,  target, alternative, altersize, res):

            for i in range(candstart, len(candidates)):
                candidate = candidates[i]
                if target < candidate:  # 剪枝
                    return


                alternative[altersize] = candidate  # 将该元素加入可能候选集

                if i > candstart and candidates[i-1] == candidates[i]:  # 防止重复的组合的出现 剪枝精髓--第一次出现相同的元素的不用continue
                    continue


                if target == candidate :  # 匹配成功 加入到res中
                    res.append(alternative[0:altersize + 1])
                    return

                _combinationSum(candidates, i+1, target - candidate, alternative, altersize + 1, res)  # 继续递归寻找 1 2 2 2 5

        if candidates == []:
            return []
        candidates.sort()
        if candidates[0] > target:
            return []
        res = []
        maxsize = target // candidates[0]
        alternative = [0] * maxsize
        _combinationSum(candidates, 0, target, alternative, 0, res)

        return res


s = Solution()
print(s.combinationSum2(candidates = [2,5,2,1,2], target = 7))