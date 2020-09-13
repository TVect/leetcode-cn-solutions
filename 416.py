"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
 
示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 0-1 背包问题
    def canPartition_1(self, nums: List[int]) -> bool:
        num_size = len(nums)
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False
        target = num_sum // 2
        # dp[i][j] 表示是否可以从 nums[0, ..., i] 中选出和为 j 的子集
        dp = [[True] + [False] * target for _ in range(num_size)]
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for idx in range(1, num_size):
            for j in range(1, target + 1):
                if nums[idx] > j:
                    dp[idx][j] = dp[idx - 1][j]
                else:
                    dp[idx][j] = dp[idx - 1][j] or dp[idx - 1][j - nums[idx]]
            if dp[idx][target]:
                return True
        return dp[-1][-1]

    # 0-1 背包问题. 优化内存的动态规划
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False
        target = num_sum // 2
        # dp[j] 表示 到当前 idx 为止，是否可以从 nums[0, ..., idx] 中选出和为 j 的子集
        dp = [True] + [False] * target

        if nums[0] <= target:
            dp[nums[0]] = True

        for num in nums[1:]:
            for j in range(target, 0, -1):
                if num <= j:
                    dp[j] = dp[j] or dp[j - num]
            if dp[target]:
                return True
        return dp[-1]


nums = [1, 5, 11, 5]
nums = [1, 2, 3, 5]
nums = [2, 2, 3, 5]
print(Solution().canPartition(nums))
