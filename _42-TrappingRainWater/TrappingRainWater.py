'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


（图一---题目.png）
上图是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

'''

'''
1.当n<3时，不可能出现闭合的区域 结果肯定为0
2.首先要找到第一个出现的不为0的高度：
    若这个高度出现在倒数第二个或倒数第一个位置上或者根本就没有不为0的高度 说明没有闭合区域  结果也肯定为0
    设置当前可能接到水的候选高度candidate = 0
    设置cur_height_i = 第一个高度位置cur_start
    设置一个比cur_start位置的高度小的最大高度maxheight（后边就知道它的妙处了）
    从cur_height_i的下一个位置开始寻找（记为cur_i）：（寻找比cur_height_i位置的高度大的位置形成闭合区域）
        若当前高度小于cur_start位置的高度:（还未找到闭合的空间）
            更新candidate：candidate += height[cur_height_i] - height[cur_i]
            更新maxheight
        否则（即找到了闭合的区域）:
            将candidate与结果相加 更新结果
            重置candidate为0
            更新cur_height_i为当前的高度位置 继续寻找闭合空间

3.喂！上面啰里啰嗦烦不烦人！（奈何笔者语文功底差！不说多点讲不清楚啊！）
  OK！接下来到重点了！：（递归回溯开始）
    把整个数组遍历完之后  有可能没有找到与cur_height_i位置相匹配的闭合空间 
    说明它太“高”了，没办法找到后边比他更高的元素产生闭合空间！
    也就是说 他高出的一部分是“无用的”！
    那就把无用的那部分给它“砍掉”：height[cur_height_i] = maxheight
    将砍完之后再将cur_height_i当做cur_start开始执行步骤2（即递归回溯的过程）
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        def _trap(height, cur_start, res):
            if cur_start >= len(height)-1:
                return res

            candidate = 0
            cur_height_i = cur_start
            maxheight = 0
            for cur_i in range(cur_start+1, len(height)):
                if height[cur_i] < height[cur_height_i]:
                    candidate += height[cur_height_i] - height[cur_i]
                    if maxheight < height[cur_i]:
                        maxheight = height[cur_i]

                else:
                    res += candidate
                    candidate = 0
                    cur_height_i = cur_i

            height[cur_height_i] = maxheight
            return _trap(height, cur_height_i, res)

        n = len(height)
        if n < 3:
            return 0

        i = 0
        while i < n and height[i] == 0:
            i += 1

        if i == n-1 or i == n-2 or i == n :
            return 0

        res = _trap(height, i, 0)

        return res

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,1,1,2,1]))


