'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

'''


'''
a数组长度为n，b数组长度为m；
首先，找a和b两个有序数组中第K小，就是在a中找某个位置i，在b中找某个位置j，其满足条件为：
1、i+j=k  即j = k-i
2、a[i-1]<=b[j]&&b[j-1]<=a[i]
这样第K小即为：max(a[i-1],b[j-1]);
'''


# 自己没有写出来  别人的代码  太复杂
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 为了让搜索范围更小，我们始终让 num1 是那个更短的数组，PPT 第 9 张
        if len(nums1) > len(nums2):
            # 这里使用了 pythonic 的写法，即只有在 Python，中可以这样写
            # 在一般的编程语言中，得使用一个额外变量，通过"循环赋值"的方式完成两个变量的地址的交换
            nums1, nums2 = nums2, nums1

        # 上述交换保证了 m <= n，在更短的区间 [0, m] 中搜索，会更快一些
        m = len(nums1)
        n = len(nums2)

        # 使用二分查找算法在数组 nums1 中搜索一个索引 i，PPT 第 9 张
        left = 0
        right = m

        # 这里使用的是最简单的、"传统"的二分查找法模板
        while left <= right:
            # 尝试要找的索引，在区间里完成二分，为了保证语义，这里就不定义成 mid 了
            # 用加号和右移是安全的做法，即使在溢出的时候都能保证结果正确，但是 Python 中不存在溢出
            # 参考：https://leetcode-cn.com/problems/guess-number-higher-or-lower/solution/shi-fen-hao-yong-de-er-fen-cha-zhao-fa-mo-ban-pyth/
            i = (left + right) >> 1
            j = ((m + n + 1) >> 1) - i

            # 边界值的特殊取法的原因在 PPT 第 10 张
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]

            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # 交叉小于等于关系成立，那么中位数就可以从"边界线"两边的数得到，原因在 PPT 第 2 张、第 3 张
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 已经找到解了，分数组之和是奇数还是偶数得到不同的结果，原因在 PPT 第 2 张
                if (m + n) & 1:
                    return max(nums1_left_max, nums2_left_max)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                # 这个分支缩短边界的原因在 PPT 第 8 张，情况 ②
                right = i - 1
            else:
                # 这个分支缩短边界的原因在 PPT 第 8 张，情况 ①
                left = i + 1
        raise ValueError('传入无效的参数，输入的数组不是有序数组，算法失效')

