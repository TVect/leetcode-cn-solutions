"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rets = []
        if not matrix:
            return rets

        num_rows, num_cols = len(matrix), len(matrix[0])
        for idx in range(min((num_rows+1)//2, (num_cols+1)//2)):
            if num_rows - idx - 1 == idx:
                rets.extend(matrix[idx][i] for i in range(idx, num_cols - idx))
                break
            if num_cols - idx - 1 == idx:
                rets.extend(matrix[i][idx] for i in range(idx, num_rows - idx))
                break
            rets.extend(matrix[idx][i] for i in range(idx, num_cols - idx))
            rets.extend(matrix[i][num_cols - idx - 1] for i in range(idx + 1, num_rows - idx))
            rets.extend(matrix[num_rows - idx - 1][i] for i in range(num_cols - idx - 2, idx - 1, -1))
            rets.extend(matrix[i][idx] for i in range(num_rows - idx - 2, idx, -1))
        return rets


matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
print(Solution().spiralOrder(matrix))
