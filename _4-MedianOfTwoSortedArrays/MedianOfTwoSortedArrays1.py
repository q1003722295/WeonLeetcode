'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

'''




# 双指针法
class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2):
        sortarr = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                sortarr.append(nums2[j])
                j+=1
            elif j >= len(nums2):
                sortarr.append(nums1[i])
                i+=1
            elif nums1[i] < nums2[j]:
                sortarr.append(nums1[i])
                i += 1
            else:
                sortarr.append(nums2[j])
                j +=1


        lensort = len(sortarr)
        tempmid = lensort // 2
        if lensort % 2 == 0:
            return (sortarr[tempmid-1] + sortarr[tempmid]) / 2
        else:
            return sortarr[tempmid]
