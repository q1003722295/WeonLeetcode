'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

'''

'''
改写二分查找法 
使二分查找法可以直接找到左右位置

时间复杂度为logn
但效率好像没那么好
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binarySearch(nums, target, left, right, LorR):
            if left > right:
                return -1
            mid = (left + right) // 2

            if target == nums[mid]:
                if LorR and (mid-1>=0 and nums[mid-1]==target):
                    return binarySearch(nums, target, left, mid-1, LorR)
                elif LorR == False and (mid+1<n and nums[mid+1]==target):
                    return binarySearch(nums, target, mid+1, right, LorR)
                else:
                    return mid
            elif target < nums[mid]:
                return binarySearch(nums, target, left, mid - 1, LorR)
            else:
                return binarySearch(nums, target, mid + 1, right, LorR)


        n = len(nums)
        if n == 0:
            return [-1, -1]
        if target < nums[0] or target > nums[n - 1]:
            return [-1, -1]


        resleft = binarySearch(nums, target, 0, n-1, True)
        resright = binarySearch(nums, target, 0, n-1, False)

        return [resleft, resright]


s = Solution()
print(s.searchRange([8, 8], 8))