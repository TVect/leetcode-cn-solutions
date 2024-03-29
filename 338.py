"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
输入: 2
输出: [0,1,1]

示例 2:
输入: 5
输出: [0,1,1,2,1,2]

进阶:
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def countBits(self, num: int) -> List[int]:
        k = 0
        rets = [0] * (num + 1)
        while (1 << k) < num + 1:
            # rets[i+b] = rets[x]+1, b=2^m > i
            for idx in range(min(1 << k, num + 1 - (1 << k))):
                rets[idx + (1 << k)] = 1 + rets[idx]
            k += 1
        return rets

    # 动态规划做法
    def countBits_1(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for idx in range(1, num+1):
            # 如果 idx % 2 == 1, 则 dp[idx] = dp[idx-1]
            # 如果 idx % 2 == 0, 则 dp[idx] = dp[idx >> 1]
            dp[idx] = dp[idx-1] + 1if idx & 1 else dp[idx >> 1]
        return dp


num = 5
print(Solution().countBits(num))
