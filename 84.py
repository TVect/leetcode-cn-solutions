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
    def largestRectangleArea_2(self, heights: List[int]) -> int:
        # 维护一个单调不减栈，找到 NextSmallerNumber，此时栈中保存的是前面比这个数小的元素
        ascent_stack = []
        heights = [0] + heights + [0]
        max_area = 0
        for idx in range(len(heights)):
            while len(ascent_stack) > 0 and heights[ascent_stack[-1]] > heights[idx]:
                tmp_idx = ascent_stack.pop(-1)
                # 可知 stack[-1] 是前面不大于 tmp_idx 的最近的数, idx 是后面不大于 num 的最近的数
                area = heights[tmp_idx] * (idx - ascent_stack[-1] -1)
                max_area = max(max_area, area)
            ascent_stack.append(idx)
        return max_area

    # 和前面的单调栈一样，这里更显式的维护了单调递增的栈，只在下一个元素更小时才判断新的 area
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights = [0] + heights + [0]
        heights_size = len(heights)
        for idx in range(heights_size):
            while stack and heights[idx] <= heights[stack[-1]]:
                num_idx = stack.pop()
                # 只在下一个元素更小时才判断新的 area
                if heights[num_idx] != heights[idx]:
                    max_area = max(max_area, heights[num_idx] * (idx - stack[-1] - 1))
            stack.append(idx)
        return max_area


heights = [2, 1, 5, 6, 2, 3]
# heights = [1]
# heights = [2, 1, 2]
heights = [0, 9]
print(Solution().largestRectangleArea(heights))






