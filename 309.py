"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 动态规划
    def maxProfit_1(self, prices: List[int]) -> int:
        prices_size = len(prices)
        if prices_size == 0:
            return 0
        # profits[i] : 表示到第 i 天为止的最大收益
        profifs = [0] * prices_size
        for idx in range(1, prices_size):
            # 如若第 i 天卖出了股票, 则最后一次买入可能是在第0, 1, ..., idx-1 天
            profifs[idx] = max([profifs[jdx-2] + max(prices[idx]-prices[jdx], 0)
                                if jdx >= 2 else max(prices[idx]-prices[jdx], 0)
                                for jdx in range(idx)])
            # 如果第 i 天没有卖出股票
            profifs[idx] = max(profifs[idx], profifs[idx - 1])
        return profifs[-1]

    # 动态规划
    def maxProfit(self, prices: List[int]) -> int:
        prices_size = len(prices)
        if prices_size == 0:
            return 0
        # profits[i] 表示处于第i天的最大累计收益. 具体根据是否处于冷冻期，区分为了 3 种情况
        # profits[i][0] :  第 i 天手上持有股票
        #    对应于: 第 i-1 天手上持有股票+第i天未卖出, 或者 第i天不处于冷冻期+第i天购入股票
        # profits[i][1] :  第 i 天手上不持有股票, 且接下来一天处于冷冻期
        #    对应于: 第 i-1 天手上持有股票+第i天卖出了股票
        # profits[i][2] :  第 i 天手上不持有股票, 且接下来一天不处于冷冻期
        #    对应于: 第 i-1 天手上不持有股票
        profits = [[0, 0, 0] for _ in range(prices_size)]
        profits[0] = [-prices[0], 0, 0]
        for idx in range(1, prices_size):
            profits[idx][0] = max(profits[idx-1][0], profits[idx-1][2]-prices[idx])
            profits[idx][1] = profits[idx-1][0] + prices[idx]
            profits[idx][2] = max(profits[idx-1][1], profits[idx-1][2])
        return max(profits[-1])


prices = [1, 2, 3, 0, 2]
print(Solution().maxProfit(prices))
