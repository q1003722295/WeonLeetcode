'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]， #[-4, -1, -1, 0, 1, 2]

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
'''
未做出
'''
'''
排序 + 双指针
本题的难点在于如何去除重复解。

算法流程：
特判，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
对数组进行排序。
遍历排序后数组：
若 0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
对于重复元素：跳过，避免出现重复解
令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
若和大于 0，说明 nums[R]太大，R 左移
若和小于 0，说明 nums[L] 太小，L 右移
'''

class Solution(object):
    def threeSum(self, nums):


        nums.sort()
        n = len(nums)
        res = []

        if n < 3:
            return []

        for i in range(n):
            if nums[i] > 0:
                return res
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n-1
            while l < r:

                sumtr = nums[i] + nums[l] + nums[r]
                if  sumtr == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        r = r - 1
                    l += 1
                    r -= 1
                elif sumtr < 0:
                    l += 1
                else:
                    r -= 1


        return res

s = Solution()
print(s.threeSum([-1, 1, -1, 1, 0, 1]))