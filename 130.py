"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
    X X X X
    X O O X
    X X O X
    X O X X
  运行你的函数后，矩阵变为：
    X X X X
    X X X X
    X X X X
    X O X X
解释:
    被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
    任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
    如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 深度优先: 对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O
    def solve_1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        num_rows, num_cols = len(board), len(board[0])

        def dfs(idx, jdx):
            if 0 <= idx < num_rows and 0 <= jdx < num_cols and board[idx][jdx] == 'O':
                board[idx][jdx] = 'A'
                dfs(idx, jdx+1)
                dfs(idx, jdx-1)
                dfs(idx+1, jdx)
                dfs(idx-1, jdx)

        for idx in range(num_rows):
            dfs(idx, 0)
            dfs(idx, num_cols-1)
        for jdx in range(num_cols):
            dfs(0, jdx)
            dfs(num_rows-1, jdx)

        for idx in range(num_rows):
            for jdx in range(num_cols):
                if board[idx][jdx] == 'A': board[idx][jdx] = 'O'
                elif board[idx][jdx] == 'O': board[idx][jdx] = 'X'

    # 广度优先: 对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        num_rows, num_cols = len(board), len(board[0])

        stack = [[idx, jdx] for idx in range(num_rows) for jdx in range(num_cols)
                 if (idx == 0 or idx == num_rows-1 or jdx == 0 or jdx == num_cols-1) and
                 board[idx][jdx] == 'O']
        while len(stack) > 0:
            idx, jdx = stack.pop()
            board[idx][jdx] = 'A'
            for new_idx, new_jdx in [[idx-1, jdx], [idx+1, jdx], [idx, jdx-1], [idx, jdx+1]]:
                if 0 <= new_idx < num_rows and 0 <= new_jdx < num_cols and board[new_idx][new_jdx] == 'O':
                    stack.append([new_idx, new_jdx])
        for idx in range(num_rows):
            for jdx in range(num_cols):
                if board[idx][jdx] == 'A': board[idx][jdx] = 'O'
                elif board[idx][jdx] == 'O': board[idx][jdx] = 'X'


board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]
Solution().solve(board)
print(board)
