"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。

示例 1：
    输入：n = 10
    输出：12
    解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

示例 2：
    输入：n = 1
    输出：1
    解释：1 通常被视为丑数。

提示：
    1 <= n <= 1690

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq


class Solution:

    # 最小堆
    def nthUglyNumber_1(self, n: int) -> int:
        seen = {1}
        candidates = [1]
        heapq.heapify(candidates)
        for _ in range(n-1):
            item = heapq.heappop(candidates)
            for prime in [2, 3, 5]:
                tmp = item * prime
                if tmp not in seen:
                    heapq.heappush(candidates, tmp)
                    seen.add(tmp)
        return heapq.heappop(candidates)

    # 动态规划
    def nthUglyNumber(self, n: int) -> int:
        # dp[i] 表示第 i 个丑数
        dp = [1]
        # pt2, pt3, pt5 表示下一个丑数的 备选为 dp[pt2] * 2, dp[pt3] * 3, dp[pt5] * 5
        pt2, pt3, pt5 = 0, 0, 0
        while len(dp) < n:
            min_val = min(dp[pt2] * 2, dp[pt3] * 3, dp[pt5] * 5)
            if min_val == dp[pt2] * 2:
                pt2 += 1
            if min_val == dp[pt3] * 3:
                pt3 += 1
            if min_val == dp[pt5] * 5:
                pt5 += 1
            dp.append(min_val)
        return dp[-1]


n = 10
# n = 1685
print(Solution().nthUglyNumber(n))
