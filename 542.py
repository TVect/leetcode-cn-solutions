"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

示例 1：
    输入：
        [[0,0,0],
         [0,1,0],
         [0,0,0]]
    输出：
        [[0,0,0],
         [0,1,0],
         [0,0,0]]

示例 2：
    输入：
        [[0,0,0],
         [0,1,0],
         [1,1,1]]
    输出：
        [[0,0,0],
         [0,1,0],
         [1,2,1]]
 
提示：
    给定矩阵的元素个数不超过 10000。
    给定矩阵中至少有一个元素是 0。
    矩阵中的元素只在四个方向上相邻: 上、下、左、右。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 方法一：从 0 区域开始做广度搜索
    # 方法二：动态规划. 从左上到右下做一次 DP，从右下到左上做一次 DP
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(matrix), len(matrix[0])

        res = [[float('inf')] * n_cols for _ in range(n_rows)]
        # 离左上方的 0 的距离
        for row_idx in range(n_rows):
            for col_idx in range(n_cols):
                if matrix[row_idx][col_idx] == 0:
                    res[row_idx][col_idx] = 0
                else:
                    if row_idx > 0:
                        res[row_idx][col_idx] = min(res[row_idx][col_idx], res[row_idx-1][col_idx] + 1)
                    if col_idx > 0:
                        res[row_idx][col_idx] = min(res[row_idx][col_idx], res[row_idx][col_idx-1] + 1)

        # 离右下方的 0 的距离
        for row_idx in range(n_rows - 1, -1, -1):
            for col_idx in range(n_cols - 1, -1, -1):
                if matrix[row_idx][col_idx] != 0:
                    if row_idx < n_rows - 1:
                        res[row_idx][col_idx] = min(res[row_idx][col_idx], res[row_idx+1][col_idx] + 1)
                    if col_idx < n_cols - 1:
                        res[row_idx][col_idx] = min(res[row_idx][col_idx], res[row_idx][col_idx+1] + 1)
        return res


matrix = [[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]]
matrix = [[0, 0, 0],
          [0, 1, 0],
          [1, 1, 1]]
matrix = [[1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
          [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
          [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]
print(Solution().updateMatrix(matrix))
