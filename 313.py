"""
编写一段程序来查找第 n 个超级丑数。
超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:
    输入: n = 12, primes = [2,7,13,19]
    输出: 32
    解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
    说明:
        1 是任何给定 primes 的超级丑数。
         给定 primes 中的数字以升序排列。
        0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000 。
        第 n 个超级丑数确保在 32 位有符整数范围内。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import heapq


class Solution:

    # 最小堆
    def nthSuperUglyNumber_1(self, n: int, primes: List[int]) -> int:
        seen = {1}
        candidates = [1]
        heapq.heapify(candidates)
        for _ in range(n-1):
            val = heapq.heappop(candidates)
            for prime in primes:
                tmp = prime * val
                if tmp not in seen:
                    seen.add(tmp)
                    heapq.heappush(candidates, tmp)
        return heapq.heappop(candidates)

    # 动态规划
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # dp[i]: 表示 第 i 个丑数
        dp = [1]
        n_primes = len(primes)
        pts = [0] * n_primes

        while len(dp) < n:
            values = [primes[idx] * dp[pts[idx]] for idx in range(n_primes)]
            min_val = min(values)
            dp.append(min_val)
            for idx in range(n_primes):
                if values[idx] == min_val:
                    pts[idx] += 1

        return dp[-1]


n, primes = 12, [2, 7, 13, 19]
print(Solution().nthSuperUglyNumber(n, primes))
