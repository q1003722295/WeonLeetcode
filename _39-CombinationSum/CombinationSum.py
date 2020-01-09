'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

'''
递归回溯 即dfs
    
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def _combinationSum(candidates, target, alternative, altersize,  res):


            for candidate in candidates:
                if target < candidate: #剪枝
                    return

                if altersize > 0 and candidate < alternative[altersize-1]: #防止重复的组合的出现
                    continue

                alternative[altersize] = candidate #将该元素加入可能候选集

                if target == candidate: #匹配成功 加入到res中
                    res.append(alternative[0:altersize+1])
                    return

                _combinationSum(candidates, target - candidate, alternative, altersize+1, res)  #继续递归寻找



        if candidates == []:
            return []
        candidates.sort()
        if candidates[0] > target:
            return []
        res = []
        maxsize = target // candidates[0]
        alternative = [0]*maxsize
        _combinationSum(candidates, target, alternative, 0, res)

        return res


s = Solution()
print(s.combinationSum(candidates = [1, 2, 3, 4], target = 7))



