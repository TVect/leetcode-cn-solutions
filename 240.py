"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def searchMatrix_1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        num_rows, num_cols = len(matrix), len(matrix[0])

        def find_target(in_list, left_idx, right_idx):
            # 二分查找 target 是否在 in_list[left_idx, ..., right_idx] 中
            # 如果在，返回位置
            # 如果不再，返回 -(pos+1), pos 表示应该插入的位置
            if right_idx < left_idx:
                return -1

            mid_idx = (left_idx + right_idx) // 2
            if in_list[mid_idx] == target:
                return mid_idx
            elif in_list[mid_idx] > target:
                if mid_idx - 1 < left_idx:
                    # 应该被插入到 left_idx 的位置
                    return -(left_idx+1)
                return find_target(in_list, left_idx, mid_idx - 1)
            else:
                # in_list[mid_idx] < target
                if mid_idx + 1 > right_idx:
                    # 应该被插入到 right_idx + 1 的位置
                    return -(right_idx+2)
                return find_target(in_list, mid_idx + 1, right_idx)

        row_spans = [0, num_rows-1]
        col_spans = [0, num_cols-1]
        while True:
            pos = find_target(matrix[row_spans[0]], col_spans[0], col_spans[1])
            if pos >= 0:
                return True
            col_spans[1] = -pos-2

            pos = find_target(matrix[row_spans[1]], col_spans[0], col_spans[1])
            if pos >= 0:
                return True
            col_spans[0] = -pos-1

            if col_spans[0] > col_spans[1]:
                return False

            pos = find_target([row[col_spans[0]] for row in matrix], row_spans[0], row_spans[1])
            if pos >= 0:
                return True
            row_spans[1] = -pos - 2

            pos = find_target([row[col_spans[1]] for row in matrix], row_spans[0], row_spans[1])
            if pos >= 0:
                return True
            row_spans[0] = -pos - 1

            if row_spans[0] > row_spans[1]:
                return False

    # Approach: 考虑中间列，找到 target 应该所属的位置，接下来在 左下角矩阵和右上角矩阵中递归查找
    def searchMatrix_1(self, matrix, target):
        if not matrix:
            return False
        num_rows, num_cols = len(matrix), len(matrix[0])

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, num_cols-1, num_rows-1)

    # Approach: 从左下角开始, 根据当前元素 和 target 之间的大小关系，向上/向右移动一格，直到找到指定元素
    # 时间复杂度: O(m+n)
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        num_rows, num_cols = len(matrix), len(matrix[0])
        pos = [num_rows-1, 0]
        while True:
            if pos[0] < 0 or pos[1] >= num_cols:
                return False
            if matrix[pos[0]][pos[1]] == target:
                return True
            elif matrix[pos[0]][pos[1]] < target:
                pos[1] += 1
            elif matrix[pos[0]][pos[1]] > target:
                pos[0] -= 1


matrix = [[1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
target = 5
target = 20

print(Solution().searchMatrix(matrix, target))