'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''
'''
递归回溯法

注意append的坑 list1.append（list2）若之后list2改变 则list1加入过的list2也会改变 也就是说 他们公用一块空间
修改：list1.append（list2[:])相当于append的时候复制了一份list2
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def rankTimes(n):
            if n < 0:
                return 0
            if n == 1:
                return 1
            return n * rankTimes(n-1)

        rtimes = rankTimes(len(nums))
        def _pernute(nums, cur_i,  times, res, temparr, temparr_n, visited):
            '''

            :param nums: List[int]
            :param cur_i:int 当前的遍历到的值
            :param times: int 已经加入res的个数
            :param res: List[List[int]] 结果
            :param temparr: List[int] 暂放数组
            :param temparr_n:int 暂放数组的截止地址
            :param visited:bool 某元素是否已经被访问
            :return: 无
            '''
            if times == rtimes:
                return
            if cur_i >= 0:
                temparr_n += 1
                temparr[temparr_n - 1] = nums[cur_i]
                visited[cur_i] = True

            if temparr_n == len(nums):
                times += 1
                res.append(temparr[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    _pernute(nums, i, times, res, temparr, temparr_n, visited)
                    visited[i] = False


        n = len(nums)
        res = []
        temparr = [-1] * n
        visited = [False] * n
        _pernute(nums, -1, 0, res, temparr, 0, visited)

        return res

s = Solution()
print(s.permute([1, 2]))