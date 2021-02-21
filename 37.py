"""
编写一个程序，通过填充空格来解决数独问题。

一个数独的解法需遵循如下规则：
    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    空白格用 '.' 表示。

提示：
    给定的数独序列只包含数字 1-9 和字符 '.' 。
    你可以假设给定的数独只有唯一解。
    给定数独永远是 9x9 形式的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrace(idx):
            # print(idx)
            if idx >= 81:
                return True

            row_idx = idx // 9
            col_idx = idx % 9

            if board[row_idx][col_idx] != '.':
                return backtrace(idx + 1)
            else:
                for val in range(1, 10):
                    if is_valid(row_idx, col_idx, f'{val}'):
                        board[row_idx][col_idx] = f'{val}'
                        if backtrace(idx + 1):
                            return True
                        board[row_idx][col_idx] = '.'

        def is_valid(row_idx, col_idx, val):
            for idx in range(9):
                if board[row_idx][idx] == val:
                    return False
                if board[idx][col_idx] == val:
                    return False
                if board[row_idx // 3 * 3 + idx // 3][col_idx // 3 * 3 + idx % 3] == val:
                    return False
            return True

        backtrace(0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(board)
print(board)
