"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−2^31, 2^31− 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
    输入：x = 123
    输出：321

示例 2：
    输入：x = -123
    输出：-321

示例 3：
    输入：x = 120
    输出：21

示例 4：
    输入：x = 0
    输出：0

提示：
    -2^31 <= x <= 2^31 - 1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import math


class Solution:

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        ret = 0
        while x:
            x, residue = divmod(x, 10)
            ret = ret * 10 + residue
        ret *= sign
        return ret if -1 * math.pow(2,31) <= ret <= math.pow(2,31) - 1 else 0


x = 123
print(Solution().reverse(x))
