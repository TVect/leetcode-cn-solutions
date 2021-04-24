"""
如果正整数可以被 A 或 B 整除，那么它是神奇的。
返回第 N 个神奇数字。由于答案可能非常大，返回它模 10^9 + 7 的结果。

示例 1：
    输入：N = 1, A = 2, B = 3
    输出：2

示例 2：
    输入：N = 4, A = 2, B = 3
    输出：6

示例 3：
    输入：N = 5, A = 2, B = 4
    输出：10

示例 4：
    输入：N = 3, A = 6, B = 4
    输出：8

提示：
    1 <= N <= 10^9
    2 <= A <= 40000
    2 <= B <= 40000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nth-magical-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # 计算 a, b 的最小公倍数
        min_val, max_val = min(a, b), max(a, b)
        while min_val:
            min_val, max_val = max_val % min_val, min_val
        lcm = a * b // max_val

        # 小于 k 的神奇数的个数为: k // a + k // b - k // lcm
        left, right = 1, min(a, b) * n
        while left < right:
            mid = left + (right - left) // 2
            mid_order = mid // a + mid // b - mid // lcm
            if mid_order < n:
                left = mid + 1
            elif mid_order >= n:
                right = mid
        return left % (pow(10, 9) + 7)


N, A, B = 1, 2, 3
N, A, B = 4, 2, 3
N, A, B = 5, 2, 4
N, A, B = 3, 6, 4
print(Solution().nthMagicalNumber(N, A, B))
