"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1。

示例 2:
    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
    说明: 你可以假设 n 不小于 2 且不大于 58。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def integerBreak(self, n: int) -> int:
        if n == 1:
            return 0
        dp = [0] * (n+1)
        for i in range(2, n+1):
            # 假定第一个拆出来的数字为 j，剩下的 i - j 可以选择拆或者不拆
            dp[i] = max(max(j * dp[i-j] for j in range(1, i)),
                        max(j * (i-j) for j in range(1, i)))
        return dp[-1]


n = 2
n = 10
n = 3
n = 4
print(Solution().integerBreak(n))
