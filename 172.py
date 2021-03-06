"""
给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:
    输入: 3
    输出: 0
    解释: 3! = 6, 尾数中没有零。

示例 2:
    输入: 5
    输出: 1
    解释: 5! = 120, 尾数中有 1 个零.

说明: 你算法的时间复杂度应为 O(log n) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 考虑 n! 的整个因子中出现的 5 的次数
    # 因为会有多重因子出现，结果为: n // 5 + n // 25 + n // 125 + ...
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n:
            n = n // 5
            cnt += n
        return cnt


n = 25
print(Solution().trailingZeroes(n))
