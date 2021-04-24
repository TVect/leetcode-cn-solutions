"""
给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。
丑数是可以被 a 或 b 或 c 整除的 正整数 。

示例 1：
    输入：n = 3, a = 2, b = 3, c = 5
    输出：4
    解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。

示例 2：
    输入：n = 4, a = 2, b = 3, c = 4
    输出：6
    解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。

示例 3：
    输入：n = 5, a = 2, b = 11, c = 13
    输出：10
    解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。

示例 4：
    输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
    输出：1999999984

提示：
    1 <= n, a, b, c <= 10^9
    1 <= a * b * c <= 10^18
    本题结果在 [1, 2 * 10^9] 的范围内

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 容斥原理
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def lcm(x, y):
            # Least Common Multiple
            min_val, max_val = min(x, y), max(x, y)
            while min_val:
                max_val, min_val = min_val, max_val % min_val
            return x * y // max_val

        # <= k 的丑数个数: k // a + k //b + k // c - k // lcm(a, b) - k // lcm(a, c) - k // lcm(b, c) + k // lcm(a, b, c)
        lcm_ab = lcm(a, b)
        lcm_bc = lcm(b, c)
        lcm_ac = lcm(a, c)
        lcm_abc = lcm(lcm_ab, c)

        left, right = 1, min(a, b, c) * n
        while left < right:
            mid = left + (right - left) // 2
            mid_order = mid // a + mid // b + mid // c - mid // lcm_ab - mid // lcm_ac - mid // lcm_bc + mid // lcm_abc
            if mid_order >= n:
                right = mid
            else:
                left = mid + 1
        return left


n, a, b, c = 3, 2, 3, 5
n, a, b, c = 4, 2, 3, 4
n, a, b, c = 5, 2, 11, 13
n, a, b, c = 1000000000, 2, 217983653, 336916467
print(Solution().nthUglyNumber(n, a, b, c))
