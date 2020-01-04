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
1、 ①若数组为空 直接返回0;
    ②若target>nums[n-1] 返回n
    
2、用双指针两头搜索 降低复杂度
但总体复杂度还是O（n）

'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 or nums[0] > target:
            return 0


        i = 0
        j = n-1
        while nums[i] < target and nums[j] > target:
            i += 1
            j -= 1

        if not(nums[i] < target):
            return i
        elif nums[j] == target:
            return j
        else:
            return j + 1


