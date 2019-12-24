'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''
'''
非动态规划

dp[0] = 0
dp表示每一个前面的构成盛水最多的下标
dp[0] = 0
dp[i] == -1 or (i - j) * min(height[i], height[j]) > (i - dp[i]) * min(height[dp[i]], height[i]

#最后发现 不是动态规划问题！  不是最后一个为最大值！
#其实是暴力！超时了 

动态规划是看前一个位置与当前位置有对应关系  显然这样做是没有联系的  根本就不是动态规划
以后想是不是能用动态规划 先想暴力的时间复杂度 
然后看动态规划到底有没有用动态规划将其优化！
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        dp = [-1] * n
        maxh = 0
        for i in range(1, n):
            for j in range(i):
                tem1 = (i - j) * min(height[i], height[j])
                temp2 = (i - dp[i]) * min(height[dp[i]], height[i])
                if dp[i] == -1 or  tem1 >= temp2:
                    dp[i] = j

                temp2 = (i - dp[i]) * min(height[dp[i]], height[i])
                if temp2 > maxh:
                    maxh = temp2

        return maxh


s = Solution()
h = [2,3,4,5,18,17,6]
print(s.maxArea(h))
# 超时！