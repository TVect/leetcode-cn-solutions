"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def maxProfit_1(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price > min_price:
                max_profit = max(max_profit, price - min_price)
            else:
                min_price = price
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        # dp[0] 当前时刻不持有的最大利润
        # dp[1] 当前时刻持有的最大利润
        dp = [0, -float('inf')]
        for price in prices:
            # 因为只能做一次购买，所以 dp[idx][1] = max(dp[idx][1], -price)
            dp = [max(dp[0], dp[1] + price), max(dp[1], -price)]
        return max(dp)


prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
