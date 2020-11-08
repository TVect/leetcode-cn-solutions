"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:
    输入:
        [[1,1,1],
         [1,0,1],
         [1,1,1]]
    输出:
        [[1,0,1],
         [0,0,0],
         [1,0,1]]

示例 2:
    输入:
        [[0,1,2,0],
         [3,4,5,2],
         [1,3,1,5]]
    输出:
        [[0,0,0,0],
         [0,4,5,0],
         [0,3,1,0]]

进阶:
    一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
    一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
    你能想出一个常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # O(m + n) 的额外空间
    def setZeroes_1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows, zero_cols = set(), set()
        num_rows, num_cols = len(matrix), len(matrix[0])
        for idx in range(num_rows):
            for jdx in range(num_cols):
                if matrix[idx][jdx] == 0:
                    zero_rows.add(idx)
                    zero_cols.add(jdx)
        for idx in range(num_rows):
            for jdx in range(num_cols):
                if (idx in zero_rows) or (jdx in zero_cols):
                    matrix[idx][jdx] = 0

    # O(1) 的额外空间
    # 使用每行/每列 的第一个元素来表示 该行/列 是否需要置为零
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows, num_cols = len(matrix), len(matrix[0])
        row0_contain0 = False
        for idx in range(num_cols):
            if matrix[0][idx] == 0:
                row0_contain0 = True
                break
        col0_contain0 = False
        for idx in range(num_rows):
            if matrix[idx][0] == 0:
                col0_contain0 = True
                break
        # row0_contain0 = any(matrix[0][idx] == 0 for idx in range(num_cols))
        # col0_contain0 = any(matrix[idx][0] == 0 for idx in range(num_rows))

        for idx in range(1, num_rows):
            for jdx in range(1, num_cols):
                if matrix[idx][jdx] == 0:
                    matrix[idx][0] = 0
                    matrix[0][jdx] = 0

        for idx in range(1, num_rows):
            for jdx in range(1, num_cols):
                if matrix[idx][0] == 0 or matrix[0][jdx] == 0:
                    matrix[idx][jdx] = 0
        if row0_contain0:
            for idx in range(num_cols):
                matrix[0][idx] = 0
        if col0_contain0:
            for idx in range(num_rows):
                matrix[idx][0] = 0


matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]
Solution().setZeroes(matrix)
print(matrix)
