
from TwoSum1 import  Solution as S1
from TwoSum2 import  Solution as S2



if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    s1 = S1()
    s2 = S2()

    print(s1.twoSum(nums, target))
    print(s2.twoSum(nums, target))