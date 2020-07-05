"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。


示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # basic
    def largestRectangleArea_1(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            left_idx, right_idx = i, i
            while left_idx >= 0 and heights[left_idx] >= heights[i]:
                left_idx -= 1
            while right_idx < len(heights) and heights[right_idx] >= heights[i]:
                right_idx += 1
            max_area = max(max_area, heights[i] * (right_idx - left_idx - 1))
        return max_area

    # 单调栈
    def largestRectangleArea(self, heights: List[int]) -> int:
        ascent_stack = []
        heights = [0] + heights + [0]
        max_area = 0
        for idx in range(len(heights)):
            while len(ascent_stack) > 0 and heights[ascent_stack[-1]] > heights[idx]:
                tmp_idx = ascent_stack.pop(-1)
                area = heights[tmp_idx] * (idx - ascent_stack[-1] -1)
                max_area = max(max_area, area)
            ascent_stack.append(idx)
        return max_area


heights = [2, 1, 5, 6, 2, 3]
heights = [1]
heights = [2, 0, 2]
print(Solution().largestRectangleArea(heights))
