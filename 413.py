"""
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
以下数列不是等差数列。
    1, 1, 2, 5, 7
 
数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。
如果满足以下条件，则称子数组(P, Q)为等差数组：
元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。
函数要返回数组 A 中所有为等差数组的子数组个数。

示例:
    A = [1, 2, 3, 4]
    返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 2:
            return 0
        # dp[i] 表示以 i 为结尾的最长等差序列的长度
        dp = [1] + [2] * (nums_size - 1)
        res = 0
        for idx in range(2, nums_size):
            if nums[idx] + nums[idx - 2] == 2 * nums[idx - 1]:
                dp[idx] = dp[idx - 1] + 1
            res += (dp[idx] - 2)
        return res


nums = [1, 2, 3, 4]
print(Solution().numberOfArithmeticSlices(nums))
