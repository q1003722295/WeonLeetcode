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
1 ①若数组为空 返回【-1,-1】
  ②若目标值小于最小值大于最大值 返回[-1,-1】

2、使用二分查找法：
    ①若没找到 返回[-1,-1]
    ②找到目标值的某个位置：双指针法找到开始位置和结束位置 
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binarySearch(nums, target, left, right):
            if left > right:
                return -1
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binarySearch(nums, target, left, mid - 1)
            else:
                return binarySearch(nums, target, mid + 1, right)


        n = len(nums)
        if n == 0:
            return [-1, -1]
        if target < nums[0] or target > nums[n - 1]:
            return [-1, -1]


        tempPos = binarySearch(nums, target, 0, n-1)
        if tempPos == -1:
            return [-1, -1]

        i =  tempPos - 1
        j = tempPos + 1
        while i >= 0 and j < n:
            if nums[i] != target or nums[j] != target:
                break

            i -= 1
            j += 1

        while j < n and nums[j] == target:
            j += 1

        while i >= 0 and nums[i] == target:
            i -= 1

        return [i+1, j-1]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))