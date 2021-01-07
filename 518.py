"""
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:
    输入: amount = 5, coins = [1, 2, 5]
    输出: 4
    解释: 有四种方式可以凑成总金额:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1

示例 2:
    输入: amount = 3, coins = [2]
    输出: 0
    解释: 只用面额2的硬币不能凑成总金额3。

示例 3:
    输入: amount = 10, coins = [10]
    输出: 1

注意:
    你可以假设：
        0 <= amount (总金额) <= 5000
        1 <= coin (硬币面额) <= 5000
        硬币种类不超过 500 种
        结果符合 32 位符号整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 完全背包问题：动态规划
    def change_1(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        num_coins = len(coins)
        if num_coins == 0:
            return 0

        # dp[i][j]: 表示使用硬币 coins[0, ..., i] 有几种方式可以凑成金额 j
        dp = [[1] + [0] * amount for _ in range(num_coins)]
        for idx in range(0, num_coins):
            for jdx in range(1, amount+1):
                if coins[idx] > jdx:
                    dp[idx][jdx] = dp[idx-1][jdx]
                else:
                    dp[idx][jdx] = dp[idx-1][jdx] + dp[idx][jdx - coins[idx]]
        return dp[-1][-1]

    # 完全背包问题：动态规划 + 空间优化
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        num_coins = len(coins)
        if num_coins == 0:
            return 0

        # dp[i][j]: 表示使用硬币 coins[0, ..., i] 有几种方式可以凑成金额 j
        num_coins = len(coins)
        dp = [1] + [0] * amount
        for idx in range(0, num_coins):
            for jdx in range(1, amount+1):
                if coins[idx] <= jdx:
                    dp[jdx] += dp[jdx - coins[idx]]
        return dp[-1]


amount, coins = 5, [1, 2, 5]
amount, coins = 0, []
print(Solution().change(amount, coins))
