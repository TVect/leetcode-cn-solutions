"""
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。
这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

示例：
    输入：[5,3,4,5]
    输出：true
    解释：
        亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
        假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
        如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
        如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
        这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。

提示：
    2 <= piles.length <= 500
    piles.length 是偶数。
    1 <= piles[i] <= 500
    sum(piles) 是奇数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stone-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 动态规划
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] 表示 piles[i, ..., j] 中 先手 & 后手 分别可以获得多少分
        size_piles = len(piles)
        dp = [[[0, 0] for idx in range(size_piles)] for jdx in range(size_piles)]
        for i in range(size_piles):
            dp[i][i] = [piles[i], 0]
        for i in range(size_piles-1, -1, -1):
            for j in range(i+1, size_piles):
                dp[i][j][0] = max(piles[i] + dp[i+1][j][1], piles[j] + dp[i][j-1][1])
                dp[i][j][1] = min(dp[i+1][j][0], dp[i][j-1][0])
        # return dp[0][size_piles-1]
        return dp[0][size_piles-1][0] > dp[0][size_piles-1][1]

    # 另一种动态规划
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] 表示 piles[i, ..., j] 中 当前玩家和另一个玩家分数之差的最大值
        size_piles = len(piles)
        dp = [[0] * size_piles for _ in range(size_piles)]
        for i in range(size_piles):
            dp[i][i] = piles[i]
        for i in range(size_piles-1, -1, -1):
            for j in range(i+1, size_piles):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][size_piles-1] > 0


piles = [5, 3, 4, 5]
print(Solution().stoneGame(piles))
