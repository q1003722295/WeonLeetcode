'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
'''

'''
栈的运用
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stacks = ['']*10000

        if len(s) == 0:
            return True

        sarr = ['(', '{', '[']
        if s[0] not in sarr:
            return False


        length = 0
        i = 0
        while i < len(s):
            if s[i] in sarr:
                stacks[length] = s[i]
                length += 1
            else:
                if s[i] == ')':
                    if stacks[length - 1] != '(':
                        return  False
                    length -= 1
                elif s[i] == '}':
                    if stacks[length - 1] != '{':
                        return  False
                    length -= 1
                else:
                    if stacks[length - 1] != '[':
                        return  False
                    length -= 1
            i+=1

        if length == 0:
            return True
        else:
            return  False


s = Solution()
print(s.isValid("{[]}"))
