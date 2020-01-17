'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

'''
'''
动态规划----图的最短路径
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0 or n == 1:
            return 0

        # 设置最大值
        MAXSIZE = 9999999
        #  dp代表跳跃到该位置的最少跳跃次数
        dp = [MAXSIZE] * n
        dp[0] = 0 #初始化dp[0]
        # 初始化第一个最小跳跃次数的点
        min_i = 0
        addstart =0#维护dp的起始增量
        while dp[n-1] == MAXSIZE:
            for j in range(min_i+addstart, min_i+nums[min_i]+1): #上一层已经更新了的dp无需再更新，因为它的跳跃次数一定比上一层要大 该层维护从上一层更新后的下一个点开始更新 即从min_i + nums[min_i-1]开始
                if j < n and dp[j] > dp[min_i]+1 :
                    dp[j] = dp[min_i] + 1

            if dp[-1] != MAXSIZE: #只要发现要找的最后一个点已经被维护了，停止寻找！
                break

            addstart = nums[min_i] #更新增量
            min_i += 1



        return dp[-1]

s = Solution()
print(s.jump([2,3,1,1,4]))



