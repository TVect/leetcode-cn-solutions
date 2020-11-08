"""
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
    输入: 4
    输出: 2

示例 2:
    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842...,
         由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:

    # 二分查找
    def mySqrt_1(self, x: int) -> int:
        left, right = 0, x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            tmp = mid * mid
            if tmp <= x:
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans

    # 袖珍计算器算法: x^{1/2} = exp(1/2 * ln x)
    def mySqrt_2(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if math.pow(ans + 1, 2) <= x else ans

    # 牛顿法: 求 关于 t 的方程 t^2 - x = 0 的根
    # t_{i+1} = 1/2 * (t_i + x/t_i)
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = x
        while True:
            tmp = 0.5 * (ans + x / ans)
            if abs(ans - tmp) < 1e-7:
                return int(ans)
            ans = tmp


print(Solution().mySqrt(6))
