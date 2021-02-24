"""
f(x) 是 x! 末尾是 0 的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 ）
例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。
给定 K，找出多少个非负整数 x ，能满足 f(x) = K 。

示例 1：
    输入：K = 0
    输出：5
    解释：0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。

示例 2：
    输入：K = 5
    输出：0
    解释：没有匹配到这样的 x!，符合 K = 5 的条件。

提示：
    K 是范围在 [0, 10^9] 的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 二分法
    def preimageSizeFZF(self, K: int) -> int:

        def trailingZeroes(n: int) -> int:
            cnt = 0
            while n:
                n = n // 5
                cnt += n
            return cnt
        # 下界: k = int(x/5) + int(x/25) + ... <= x/5 + x/25 + ... = 4x/5 ，故有 x >= 5K/4 >= K
        # 上界: 10K的意思是，要有K个零，也就是最多最多就是有K个10相乘，比如 K=3，上界就是30，阶乘是30*29*28*..1肯定包含了3个10相乘
        lo, hi = K, 10 * K + 1
        while lo < hi:
            mid = (lo + hi) // 2
            num_zeros = trailingZeroes(mid)
            if num_zeros == K:
                return 5
            elif num_zeros > K:
                hi = mid
            else:
                lo = mid + 1
        return 0


K = 5
K = 0
print(Solution().preimageSizeFZF(K))
