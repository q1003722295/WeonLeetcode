'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z
'''
'''
利用python强大的功能
zip 打包成元素列表，同时利用set()函数的不重复性，大于1就结束
'''

'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
l = ['a', 'b', 'c', 'd', 'e','f']
print l

#打印列表
print zip(l[:-1],l[1:])
输出结果：
['a', 'b', 'c', 'd', 'e', 'f']
[('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]

nums = ['flower','flow','flight']
for i in zip(*nums):
    print(i)
输出结果：

('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')

set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
>>>x = set('runoob')
>>> y = set('google')
>>> x, y
(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l']))   # 重复的被删除
>>> x & y         # 交集
set(['o'])
>>> x | y         # 并集
set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
>>> x - y         # 差集
set(['r', 'b', 'u', 'n'])
'''

class Solution:
    def longestCommonPrefix(self, strs):
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s

s = Solution()
print(s.longestCommonPrefix(["aa","a"]))