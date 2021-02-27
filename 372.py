"""
你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1：
    输入：a = 2, b = [3]
    输出：8

示例 2：
    输入：a = 2, b = [1,0]
    输出：1024

示例 3：
    输入：a = 1, b = [4,3,3,8,5,2]
    输出：1

示例 4：
    输入：a = 2147483647, b = [2,0,0]
    输出：1198

提示：
    1 <= a <= 2^31 - 1
    1 <= b.length <= 2000
    0 <= b[i] <= 9
    b 不含前导 0


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-pow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def superPow_1(self, a: int, b: List[int]) -> int:
        # pow(a, [b0, b1, ..., bk]) = pow(a, b0 * 10^{k}) * ... * pow(a, bk)
        #                           = pow(a, b0) ^ {10^k} * ... * pow(a, bk)
        # (x * y) % 1337 = (x % 1337) (y % 1337) % 1337
        res = 1
        for val in b:
            res = (pow(res, 10) % 1337) * (pow(a % 1337, val) % 1337) % 1337
        return res

    # 不使用系统函数
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1

        def mypow(x, y, base):
            if y == 0:
                return 1
            x = x % base
            if y % 2 == 1:
                return (mypow(x, y - 1, base) * x) % base
            else:
                sub = mypow(x, y // 2, base)
                return (sub * sub) % base

        last = b.pop(-1)
        part1 = mypow(a, last, 1337)
        part2 = mypow(self.superPow(a, b), 10, 1337)

        return (part1 * part2) % 1337


a, b = 2, [3]
a, b = 2, [1, 0]
a, b = 1, [4, 3, 3, 8, 5, 2]
a, b = 2147483647, [2, 0, 0]
print(Solution().superPow(a, b))
