'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

'''

'''
但是突然发现了一个问题：排序需要O（n）的空间复杂度
虽然通过了测试 但是还是违反了规则
既然用到排序 怎么不想想怎么排序更好呢

'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        # 若数组为空 直接返回1
        if n == 0:
            return 1

        # 将数组排序
        nums.sort()
        # 若第一个元素为正整数 且不为1 说明最小的1没有出现过 直接返回1
        if nums[0] > 0 and nums[0] > 1:
            return 1

        #若最后一个元素为负数或零，说明该数组没有正整数 直接返回最小的正整数1
        if nums[-1] <= 0:
            return 1

        # 开始判断其他的情况
        tempnum = 0
        for i in range(n-1):
            if nums[i] == nums[i+1]: #这里容易忽略  防止有重复元素影响结果
                continue

            #nums[i]大于0 的时候判断第一个没出现的最小的正整数是哪个
            if nums[i] > 0:
                tempnum = nums[i]
                if tempnum + 1 != nums[i + 1] :
                    return tempnum + 1
            else:#第一个大于0的数都比1大 直接返回1
                if nums[i+1] > 0 and nums[i+1] > 1:
                    return 1

        return tempnum + 2


s = Solution()
print(s.firstMissingPositive([1]))

