'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

'''
与三数之和类似 排序+双指针
不过是多了层循环罢了
注意的是不要重复计算加入数组
[
保证nums[i]改变了
保证nums[j]改变了
保证nums[l]改变了
保证nums[r]改变了
]
'''
import random


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums)
        if n < 4:
            return []

        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: #保证nums[i]改变了
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]: #保证nums[j]改变了
                    continue
                l = j+1
                r = n-1
                while l < r:
                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if  cur_sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:  #保证nums[l]改变了
                            l+=1
                        while l < r and nums[r] == nums[r-1]: #保证nums[r]改变了
                            r-=1
                        l += 1
                        r -= 1
                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1

        return  res


#随机生成数组nums和target
    def CreateArr(self, n):
        arr = [0]*n
        for i in range(n):
            arr[i] = random.randint(-10, 10)
        return arr

    def CreeateNum(self):
        t = random.randint(-20, 20)
        return  t

s = Solution()
for i in range(10):
    temarr = s.CreateArr(10)
    temnum = s.CreeateNum()
    print(temarr)
    print(temnum)
    print(s.fourSum( temarr, temnum ))
    print()
