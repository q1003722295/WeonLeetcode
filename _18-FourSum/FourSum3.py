'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
'''
在这基础上更妙的方法：
每次都用最大值最小值比较剪枝：
获取当前最小值，如果最小值比目标值大，说明后面越来越大的值根本没戏 直接忽略
获取当前最大值，如果最大值比目标值小，说明后面越来越小的值根本没戏 直接忽略掉

'''
import random


class Solution:
    def fourSum(self, nums, target):
        result = []
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        #数组长度
        length = len(nums)
        #定义4个指针k，i，j，h  k从0开始遍历，i从k+1开始遍历，留下j和h，j指向i+1，h指向数组最大值

        #如果最大值都小于target 或者最小值大于target 直接返回空
        max = nums[length - 4] + nums[length - 3] + nums[length - 2] + nums[length - 1]
        min = nums[0] + nums[1] + nums[2] + nums[3]
        if max < target or min > target:
            return []

        for k in range(length - 3):
            # 当k的值与前面的值相等时忽略
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 获取当前最小值，如果最小值比目标值大，说明后面越来越大的值根本没戏
            min1 = nums[k] + nums[k+1] + nums[k+2] + nums[k+3]
            if min1 > target:
                break
            # 获取当前最大值，如果最大值比目标值小，说明后面越来越小的值根本没戏，忽略
            max1 = nums[k] + nums [length-1] + nums[length - 2] + nums[length - 3]
            if max1 < target:
                continue
            for i in range(k+1, length-2):
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                j = i + 1
                h = length - 1
                min2 = nums[k] + nums[i] + nums[j] + nums[j + 1]
                if min2 > target:
                    continue
                max2 = nums[k] + nums[i] + nums[h] + nums[h - 1]
                if max2 < target:
                    continue
                # 开始j指针和h指针的表演，计算当前和，如果等于目标值，j++并去重，h--并去重，当当前和大于目标值时h--，当当前和小于目标值时j++
                while j < h:
                    curr = nums[k] + nums[i] + nums[j] + nums[h]
                    if curr == target:
                        result.append([nums[k], nums[i], nums[j], nums[h]])
                        j += 1
                        while j < h and nums[j] == nums[j - 1]:
                            j += 1
                        h -= 1
                        while j < h and i < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif curr > target:
                        h -= 1
                    elif curr < target:
                        j += 1

        return result



    #随机生成数组nums和target
    def CreateArr(self, n):
        arr = [0]*n
        for i in range(n):
            arr[i] = random.randint(-10, 10)
        return arr

    def CreeateNum(self):
        t = random.randint(-20, 20)
        return  t



s = Solution()
for i in range(10):
    temarr = s.CreateArr(10)
    temnum = s.CreeateNum()
    print(temarr)
    print(temnum)
    print(s.fourSum( temarr, temnum ))
    print()