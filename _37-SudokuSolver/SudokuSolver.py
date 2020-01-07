'''

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

Note:
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
'''
'''
坑：
python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。这种方式相当于传值和传引用的一种综合。
如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。
如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。

这个坑陷进去不能自拔！数组 字典在回溯的时候已经发生改变了！！！这还回溯个锤子！

痛定思痛
以后递归回溯遵循一下两点：
1、既然这样 那就化敌为友 运用改变这一性质 ！！！不去返回数组、字典类型！！！（可以返回字符 数字）而是返回FALSE TRUE用于判断  反正board数组发生改变了！
2、记得回溯的时候将所用数组、字典还原！（可以用返回的TRUE FALSE判断）

题解：
解数独思路：
类似人的思考方式去尝试，行，列，还有 3*3 的方格内数字是 1~9 不能重复。

我们尝试填充，如果发现重复了，那么擦除重新进行新一轮的尝试，直到把整个数组填充完成。

算法步骤:
1数独首先行，列，还有 3*3 的方格内数字是 1~9 不能重复。

2声明布尔数组，表明行列中某个数字是否被使用了， 被用过视为 true，没用过为 false。

3初始化布尔数组，表明哪些数字已经被使用过了。

4尝试去填充数组，只要行，列， 还有 3*3 的方格内 出现已经被使用过的数字，我们就不填充，否则尝试填充。

5如果填充失败，那么我们需要回溯。将原来尝试填充的地方改回来。

6递归直到数独被填充完成。

'''
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def __solveSuduku(board, inter, needFillnum,alllist):

            if inter == 81 or needFillnum == 0:
                return True

            i = inter // 9
            j = inter % 9
            if board[i][j] != '.':
                return  __solveSuduku(board, inter + 1,  needFillnum, alllist)
            else:
                for num in range(1, 10):
                    if alllist[0][i].get(num, 0) == 0 and alllist[1][j].get(num, 0) == 0 and alllist[2][(i // 3) * 3 + j // 3].get(num, 0) == 0:
                        # print(alllist)
                        board[i][j] = str(num)
                        alllist[0][i][num] = alllist[0][i].get(num, 0) + 1
                        alllist[1][j][num] = alllist[1][j].get(num, 0) + 1
                        alllist[2][(i // 3) * 3 + j // 3][num] = alllist[2][(i // 3) * 3 + j // 3].get(num, 0) + 1

                        if  __solveSuduku(board, inter + 1,  needFillnum - 1, alllist):
                            return True

                        board[i][j] = '.'
                        alllist[0][i][num] = 0
                        alllist[1][j][num] = 0
                        alllist[2][(i // 3) * 3 + j // 3][num] = 0


            return False

        rowdiclist = [{} for i in range(9)]
        coldiclist = [{} for i in range(9)]
        boxdiclist = [{} for i in range(9)]

        needFillnum = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = (int)(board[i][j])

                    rowdiclist[i][num] = rowdiclist[i].get(num, 0) + 1
                    coldiclist[j][num] = coldiclist[j].get(num, 0) + 1
                    boxdiclist[(i//3) * 3 + j // 3][num] = boxdiclist[(i//3) * 3 + j // 3].get(num, 0) + 1

                else:
                    needFillnum += 1
        alllist = [rowdiclist, coldiclist, boxdiclist]

        __solveSuduku(board, 0,  needFillnum,alllist)




s = Solution()
print(s.solveSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

[['5', '3', '4', '6', '7', '8', '9', '1', '2'],
 ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
 ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
 ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
 ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
 ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
 ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
 ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
 ['3', '4', '5', '2', '8', '6', '1', '7', '9']]






