"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.

示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import math


class Solution:

    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        dps = [0] * (n+1)
        for i in range(1, n+1):
            dps[i] = min(dps[i-square]+1 for square in squares if square <= i)
        return dps[-1]


n = 12
n = 13
print(Solution().numSquares(n))
