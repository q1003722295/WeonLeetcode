'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''

'''
# 哈希表法
时间复杂度：O(n)
我们只遍历了包含有 n 个元素的列表一次。在表中进行的每次查找只花费 O(1)的时间。

空间复杂度：O(n)，
所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存储 n个元素。
'''

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        dic = {}

        for i,n in enumerate(nums):
            if target - n in dic:
                return [dic[target-n], i]

            dic[n] = i

        return [9999, 9999]