'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

'''

'''
二分查找法
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """



        def binarySearch(nums, target, left, right):
            if left > right:
                return right
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binarySearch(nums, target, left, mid - 1)
            else:
                return binarySearch(nums, target, mid + 1, right)


        n = len(nums)

        if n == 0 or nums[0] > target:
            return 0

        restemp = binarySearch(nums, target, 0, n-1)

        if nums[restemp] >= target:
            return restemp

        else:
            return restemp +  1
