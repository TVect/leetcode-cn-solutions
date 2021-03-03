"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n_rows, n_cols = len(matrix), len(matrix[0])
        # top_cnt[i][j] 表示 matrix[i][j] 上方的连续1的个数
        top_cnt = [[0] * n_cols for _ in range(n_rows)]
        for idx in range(n_rows):
            for jdx in range(n_cols):
                if matrix[idx][jdx] == "1":
                    if idx == 0:
                        top_cnt[idx][jdx] = 1
                    else:
                        top_cnt[idx][jdx] = top_cnt[idx-1][jdx] + 1

        # 对于 top_cnt 的每一行，计算矩形的最大面积
        # 类似于 leetcode 84:
        #   给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
        #   求在该柱状图中，能够勾勒出来的矩形的最大面积。

        def get_max_area(heights):
            heights = [0] + heights + [0]
            stack = []    # 维护一个单调不减栈，找到 next smaller number
            area = 0
            for idx in range(len(heights)):
                while stack and heights[idx] < heights[stack[-1]]:
                    last_idx = stack.pop()
                    area = max(area, (idx - stack[-1] - 1) * heights[last_idx])
                stack.append(idx)
            return area

        return max(get_max_area(row) for row in top_cnt)


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
print(Solution().maximalRectangle(matrix))
