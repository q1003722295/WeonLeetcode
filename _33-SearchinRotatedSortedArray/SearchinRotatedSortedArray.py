'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''
'''
二分查找法

1、数组为空：直接返回-1
2、找出翻转的点reverseinde（前面递增数组最后一个点）（用双指针法 最坏时间n / 2）
3、二分查找法找出目标点：
    ①如果没有翻转 直接0~n-1二分查找
    ②if target == nums[reverseindex]  直接返回该点   （可以省略 但我认为一定程度上可以提高效率）
    ③其他情况target只可能<nums[reverseindex]:
        if target > nums[0]:
            在前面进行二分查找
        if target < nums[n-1]:
            在后半部分进行二分查找
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
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
            return -1


        reversindex = -1

        i = 0
        j = n-1
        while i < j:
            if nums[i] > nums[i + 1] :
                reversindex = i
                break
            if nums[j] < nums[j-1]:
                reversindex = j-1
                break

            i += 1
            j -= 1

        # 如果没有翻转
        if reversindex == -1:
            return binarySearch(nums, target, 0, n-1)


        # 相等 直接返回该点
        if target == nums[reversindex]:
            return reversindex


        if target >= nums[0]:
            return binarySearch(nums, target, 0, reversindex)

        else:
            return binarySearch(nums, target, reversindex+1, n-1)


s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
