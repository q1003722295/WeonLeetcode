'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''

'''
字典序如下：
设P是1～n的一个全排列:p=p1p2......pn=p1p2......pj-1pjpj+1......pk-1pkpk+1......pn
1）从排列的右端开始，找出第一个比右边数字小的数字的序号j（j从左端开始计算），即 j=max{i|pi<pi+1}
2）在pj的右边的数字中，找出所有比pj大的数中最小的数字pk，即 k=max{i|pi>pj}（右边的数从右至左是递增的，因此k是所有大于pj的数字中序号最大者）
3）对换pj，pk
4）再将pj+1......pk-1pkpk+1......pn倒转得到排列p'=p1p2.....pj-1pjpn.....pk+1pkpk-1.....pj+1，这就是排列p的下一个排列。

理解了字典序的定义 该题按照步骤编码即可 就不难了
'''

class Solution(object):


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def shellSort(arr):

            n = len(arr)
            gap = int(n / 2)

            while gap > 0:

                for i in range(gap, n):

                    temp = arr[i]
                    j = i
                    while j >= gap and arr[j - gap] > temp:
                        arr[j] = arr[j - gap]
                        j -= gap
                    arr[j] = temp
                gap = int(gap / 2)


        def  reverse(nums, left, right):
            i = left
            j = right
            while i < j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t

                i += 1
                j -= 1

        # 开始寻找字典序的下一个排列
        n = len(nums)
        # 若数组为空或者只有一个数字 直接返回
        if n == 0 or n == 1:
            return

        # 1）从排列的右端开始，找出第一个比右边数字小的数字的序号j（j从左端开始计算），即 j=max{i|pi<pi+1}
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                e = nums[i-1]
                # 2）在pj的右边的数字中，找出所有比pj大的数中最小的数字pk，即 k=max{i|pi>pj}（右边的数从右至左是递增的，因此k是所有大于pj的数字中序号最大者）
                minjton = i
                for j in range(i, n):
                    if nums[j] > e and nums[j] <= nums[minjton]:#注意这里相等也得算！
                        minjton = j
                # 3）对换pj，pk
                t = nums[i-1]
                nums[i-1] = nums[minjton]
                nums[minjton] = t
                # 4）再将pj+1......pk-1pkpk+1......pn倒转得到排列p'=p1p2.....pj-1pjpn.....pk+1pkpk-1.....pj+1，这就是排列p的下一个排列。
                reverse(nums, i, n-1)
                return

        shellSort(nums)

