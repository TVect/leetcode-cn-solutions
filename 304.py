"""
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例：
    给定 matrix = [[3, 0, 1, 4, 2],
                  [5, 6, 3, 2, 1],
                  [1, 2, 0, 1, 5],
                  [4, 1, 0, 1, 7],
                  [1, 0, 3, 0, 5]]

    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12

提示：
    你可以假设矩阵不可变。
    会多次调用 sumRegion 方法。
    你可以假设 row1 ≤ row2 且 col1 ≤ col2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n_rows, n_cols = len(matrix), len(matrix[0])
        self.partial_sum = [[0] * (n_cols + 1) for _ in range(n_rows + 1)]
        for idx in range(1, n_rows+1):
            for jdx in range(1, n_cols+1):
                self.partial_sum[idx][jdx] = self.partial_sum[idx - 1][jdx] + \
                                             self.partial_sum[idx][jdx - 1] - \
                                             self.partial_sum[idx - 1][jdx - 1] + \
                                             matrix[idx-1][jdx-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.partial_sum[row2+1][col2+1] - \
               self.partial_sum[row1][col2+1] - \
               self.partial_sum[row2+1][col1] + \
               self.partial_sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
