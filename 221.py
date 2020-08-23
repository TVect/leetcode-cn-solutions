"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        num_rows, num_cols = len(matrix), len(matrix[0])
        # maxima_square_edge[i][j] 表示以 i,j 位置为结束的最大正方形边长
        maxima_square_edge = [[0] * num_cols for _ in range(num_rows)]

        for row in range(num_rows):
            for col in range(num_cols):
                if (row == 0) or (col == 0) or (matrix[row - 1][col - 1] == 0) or (matrix[row][col] == '0'):
                    maxima_square_edge[row][col] = 1 if matrix[row][col] == '1' else 0
                else:
                    '''
                    last_edge = maxima_square_edge[row - 1][col - 1]
                    # check 从 matrix[row][col] 到 matrix[row][col-edge] 有多少个连续的 1
                    current_edge = 0
                    for idx in range(0, last_edge + 1):
                        if (matrix[row][col - idx] == '0') or (matrix[row - idx][col] == '0'):
                            break
                        current_edge += 1
                    maxima_square_edge[row][col] = current_edge
                    '''
                    maxima_square_edge[row][col] = min(maxima_square_edge[row-1][col-1],
                                                       maxima_square_edge[row][col-1],
                                                       maxima_square_edge[row-1][col]) + 1

        max_edge = max(map(max,maxima_square_edge))
        return max_edge * max_edge


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
matrix = []
matrix = [["0", "0", "0", "1"],
          ["1", "1", "0", "1"],
          ["1", "1", "1", "1"],
          ["0", "1", "1", "1"],
          ["0", "1", "1", "1"]]

print(Solution().maximalSquare(matrix))
