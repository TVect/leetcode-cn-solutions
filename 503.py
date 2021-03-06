"""
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1。

示例 1:
    输入: [1,2,1]
    输出: [2,-1,2]
    解释: 第一个 1 的下一个更大的数是 2；
         数字 2 找不到下一个更大的数；
         第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

注意: 输入数组的长度不会超过 10000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 单调栈: 从左往右进栈
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        double_nums = nums + nums
        next_elements = [-1] * (nums_size * 2)
        stack = []
        for idx in range(nums_size * 2):
            while stack and double_nums[idx] > double_nums[stack[-1]]:
                num_idx = stack.pop()
                next_elements[num_idx] = double_nums[idx]
            stack.append(idx)
        return next_elements[:nums_size]

    # 单调栈: 从右往左进栈
    def nextGreaterElements_1(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        double_nums = nums + nums
        next_elements = [-1] * (nums_size * 2)
        stack = []
        for idx in range(nums_size * 2 - 1, -1, -1):
            while stack and double_nums[idx] >= double_nums[stack[-1]]:
                stack.pop()
            next_elements[idx] = double_nums[stack[-1]] if stack else -1
            stack.append(idx)
        return next_elements[:nums_size]


nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))
