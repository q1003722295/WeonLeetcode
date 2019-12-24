'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''

'''
与15三数之和类似  排序加双指针
只不过判断的是dif = target - (nums[i] + nums[l] + nums[r]) 的大小
若dif<0 则r-1 否则l+1
每次保存最接近的和
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import  sys
        nums.sort()
        n = len(nums)

        if n < 3:
            return sys.maxsize

        minvalue = nums[0] + nums[1] + nums[n-1]
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                dif = target - (nums[i] + nums[l] + nums[r])
                if dif == 0:
                    return (nums[i] + nums[l] + nums[r])
                elif dif < 0:
                    if abs(dif) < abs(target - minvalue):
                        minvalue = nums[i] + nums[l] + nums[r]
                    r -= 1
                else:
                    if abs(dif) < abs(target - minvalue):
                        minvalue = nums[i] + nums[l] + nums[r]
                    l += 1
        return  minvalue

s = Solution()
print(s.threeSumClosest([0, -2, -1, -3, -2, -4], -3)) #-3 0 1 2 2 4