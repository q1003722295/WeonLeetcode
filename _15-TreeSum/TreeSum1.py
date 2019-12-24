'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
根据第一题twoSum 利用字典的思想  但还是超时了
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # def sortTree(arr):
        #     if len(arr) > 3 or len(arr) <= 2:
        #         return []
        #     for i in range(1, len(arr)):
        #         temp = arr[i]
        #         j = i-1
        #         while j > -1 and temp < arr[j]:
        #             arr[j+1] = arr[j]
        #             j-=1
        #         arr[j+1] = temp
        #
        #
        #     return arr

        n = len(nums)
        res = []

        for i in range(0, n):
            dic = {}
            target = nums[i]
            for j, n2 in enumerate(nums[i+1:n]):
                if -target - n2  in dic:
                    temparr = [target, n2, -target - n2]
                    temparr.sort()
                    if temparr not in res and temparr != []:
                        res.append(temparr)

                dic[n2] = j

        return res


s = Solution()
print(s.threeSum([-1, 1, -1, 1, 0, 1]))