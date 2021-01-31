"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：
    输入：height = [4,2,0,3,2,5]
    输出：9
 
提示：
    n == height.length
    0 <= n <= 3 * 10^4
    0 <= height[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 维护单调递减的栈，按行储水
    def trap(self, height: List[int]) -> int:
        height_size = len(height)
        stack = []
        res = 0
        for idx in range(height_size):
            while stack and height[idx] >= height[stack[-1]]:
                num_idx = stack.pop()
                # 元素 num_idx 的前后更大的元素恰好为 stack[-1] 和 idx
                if stack:
                    res += (min(height[stack[-1]], height[idx]) - height[num_idx]) * (idx - stack[-1] - 1)
            stack.append(idx)
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]
print(Solution().trap(height))
