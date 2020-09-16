"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1

示例 2:
输入: coins = [2], amount = 3
输出: -1
 
说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 表示凑成总金额为 i 所需的最少硬币个数.
        dp = [0] + [float('inf')] * amount
        for idx in range(1, amount+1):
            dp[idx] = min([dp[idx-coin] + 1 for coin in coins if coin <= idx] + [dp[idx]])
        return dp[-1] if dp[-1] != float('inf') else -1


coins = [1, 2, 5]
amount = 11

coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))