"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:
    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

说明:
    假设你总是可以到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def jump_1(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 1:
            return 0
        # steps[i] 表示到 nums[i] 的最小跳跃度
        steps = [0] + [-1] * (nums_size - 1)
        max_range = 0
        for idx in range(nums_size):
            if nums[idx] + idx >= nums_size - 1:
                return steps[idx] + 1
            if nums[idx] + idx > max_range:
                for jdx in range(max_range + 1, nums[idx] + idx + 1):
                    steps[jdx] = steps[idx] + 1
                    max_range = nums[idx] + idx
        return -1

    def jump_2(self, nums: List[int]) -> int:
        nums_size = len(nums)
        # max_range 表示 step 步至多能走到多远
        step, max_range = 0, 0
        idx = 0
        while max_range < nums_size - 1:
            tmp = 0
            while idx <= min(max_range, nums_size-1):
                tmp = max(tmp, nums[idx] + idx)
                idx += 1
            step += 1
            max_range = tmp
        return step

    # 动态规划
    def jump_3(self, nums: List[int]) -> int:
        nums_size = len(nums)
        # dp[i] 表示从 i 到 最后一个位置至少需要多少步
        dp = [-1] * (nums_size - 1) + [0]
        for idx in range(nums_size - 2, -1, -1):
            dp[idx] = min([1 + dp[jdx] for jdx in range(idx + 1, min(idx + nums[idx] + 1, nums_size)) if dp[jdx] >= 0],
                          default=-1)
        return dp[0]

    # 正向查找最大可以到达的位置
    def jump(self, nums: List[int]) -> int:
        nums_size = len(nums)
        # max_range 表示 step 步至多能走到多远
        step, end, max_range = 0, 0, 0
        for idx in range(nums_size - 1):
            max_range = max(max_range, nums[idx] + idx)
            if idx == end:
                step += 1
                end = max_range
        return step


nums = [2, 3, 1, 1, 4]
# nums = [2, 0, 2, 4, 6, 0, 0, 3]
# nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
print(Solution().jump(nums))
