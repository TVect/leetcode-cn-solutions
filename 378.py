"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：
    matrix = [[ 1,  5,  9],
              [10, 11, 13],
              [12, 13, 15]],
    k = 8,
    返回 13。

提示：
    你可以假设 k 的值永远是有效的，1 ≤ k ≤ n^2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import heapq


class Solution:

    # 堆 + 归并排序（使用小根堆）
    def kthSmallest_1(self, matrix: List[List[int]], k: int) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])
        head_eles = [[matrix[idx][0], idx, 0] for idx in range(n_rows)]
        index_cnt = 0
        while True:
            item = heapq.heappop(head_eles)
            row_id, col_id = item[1], item[2] + 1
            if col_id < n_cols:
                heapq.heappush(head_eles, [matrix[row_id][col_id], row_id, col_id])
            index_cnt += 1
            if index_cnt == k:
                return item[0]

    # 二分查找
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])

        # 寻找某个元素的 index
        def find_element_indx(ele):
            row_id, col_id = n_rows-1, 0
            cnt = 0
            while row_id >= 0:
                if col_id < n_cols and matrix[row_id][col_id] <= ele:
                    col_id += 1
                else:
                    row_id -= 1
                    cnt += col_id
            return cnt

        small_value, large_value = matrix[0][0], matrix[n_rows - 1][n_cols - 1]
        while small_value < large_value:
            element = (small_value + large_value) // 2
            idx = find_element_indx(element)
            if idx < k:
                small_value = element + 1
            else:
                large_value = element
        return small_value


matrix = [[1,  5,  9],
          [10, 11, 13],
          [12, 13, 15]]
k = 8
print(Solution().kthSmallest(matrix, k))
