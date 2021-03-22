"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
    输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
    输出：7
    解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
    输入：grid = [[1,2,3],[4,5,6]]
    输出：12

提示：
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import itertools
from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        dp = list(itertools.accumulate(grid[0]))
        for row in grid[1:]:
            dp[0] += row[0]
            for idx in range(1, num_cols):
                dp[idx] = min(dp[idx - 1], dp[idx]) + row[idx]
        return dp[-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(grid))
