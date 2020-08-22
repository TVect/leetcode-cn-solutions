"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:

    输入:
    [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
    ]
    输出: 1


示例 2:

    输入:
    [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
    ]
    输出: 3
    解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 深度优先
    def numIslands_1(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        checked = [[0] * num_cols for _ in range(num_rows)]

        def dfs(row_id, col_id):
            if (0 <= row_id < num_rows) and (0 <= col_id < num_cols) and (grid[row_id][col_id] == '1'):
                if checked[row_id][col_id] == 1:
                    return
                else:
                    checked[row_id][col_id] = 1
                    dfs(row_id + 1, col_id)
                    dfs(row_id - 1, col_id)
                    dfs(row_id, col_id - 1)
                    dfs(row_id, col_id + 1)

        num_islands = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1' and checked[row][col] == 0:
                    dfs(row, col)
                    num_islands += 1
        return num_islands

    # 广度优先
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    num_islands += 1
                    grid[row][col] = '0'
                    neighbors = [[row, col]]
                    while len(neighbors) > 0:
                        neighbor_row, neighbor_col = neighbors.pop(0)

                        for row_id, col_id in [(neighbor_row - 1, neighbor_col),
                                               (neighbor_row + 1, neighbor_col),
                                               (neighbor_row, neighbor_col - 1),
                                               (neighbor_row, neighbor_col + 1)]:
                            if (0 <= row_id < num_rows) and (0 <= col_id < num_cols) and (grid[row_id][col_id] == '1'):
                                grid[row_id][col_id] = '0'
                                neighbors.append([row_id, col_id])
        return num_islands


grid = [['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']]

grid = [['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']]

grid = [["1", "1", "1"],
        ["1", "0", "1"],
        ["1", "1", "1"]]

print(Solution().numIslands(grid))
