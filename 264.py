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
    def nthUglyNumber(self, n: int) -> int:
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


n = 10
# n = 1685
print(Solution().nthUglyNumber(n))
