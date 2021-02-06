"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。


示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。


提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 动态规划
    def findTargetSumWays_1(self, nums: List[int], S: int) -> int:
        nums_size = len(nums)
        dp = [[0] * 2001 for _ in range(nums_size)]
        dp[0][1000 + nums[0]] += 1
        dp[0][1000 - nums[0]] += 1
        for idx in range(1, nums_size):
            for jdx in range(0, 2001):
                if dp[idx-1][jdx] != 0:
                    dp[idx][jdx + nums[idx]] += dp[idx-1][jdx]
                    dp[idx][jdx - nums[idx]] += dp[idx-1][jdx]
        return dp[-1][1000+S] if -1000 <= S <= 1000 else 0

    # 动态规划 + 空间优化
    def findTargetSumWays_2(self, nums: List[int], S: int) -> int:
        dp = [0] * 2001
        dp[1000 + nums[0]] += 1
        dp[1000 - nums[0]] += 1
        for num in nums[1:]:
            new_dp = [0] * 2001
            for jdx in range(0, 2001):
                if dp[jdx] != 0:
                    new_dp[jdx + num] += dp[jdx]
                    new_dp[jdx - num] += dp[jdx]
            dp = new_dp
        return dp[1000+S] if -1000 <= S <= 1000 else 0

    # 动态规划: 转换为背包问题
    # sum(pos_symbols) - sum(neg_symbols) = S    =>    sum(positive) = (S + sum(neg_symbols) + sum(pos_symbols)) / 2
    # 可以转换为背包问题: 寻找子集，使其和为 (S + sum(nums)) / 2
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums_sum, nums_size = sum(nums), len(nums)
        if S > nums_sum or S < -nums_sum:
            return 0
        target = int((nums_sum + S) / 2)
        if target * 2 != nums_sum + S:
            return 0
        # 动态规划：dp[i][j] 背包容量为i，且只使用 nums[:j] 时的方法总数
        # 状态压缩的动态规划：dp[j] 表示只使用到当前为止的数字，有多少种方法可以恰好选出和为 j 的子集
        dp = [1] + [0] * target
        for i in range(nums_size):
            for j in range(target, -1, -1):
                dp[j] += dp[j-nums[i]] if nums[i] <= j else 0
        return dp[-1]


nums = [1, 1, 1, 1, 1]
S = 3
print(Solution().findTargetSumWays(nums, S))
