"""
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

示例 1：
    输入：n = 16
    输出：true

示例 2：
    输入：n = 5
    输出：false

示例 3：
    输入：n = 1
    输出：true

提示：
    -2^31 <= n <= 2^31 - 1

进阶：
    你能不使用循环或者递归来完成本题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-four
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # 循环除以 4
    def isPowerOfFour_1(self, n: int) -> bool:
        while n > 1:
            n, mod = divmod(n, 4)
            if mod != 0:
                return False
        return n == 1

    # 位运算: n 的二进制表示中只出现 1 个 1，且其位置在奇数位
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1) == 0) and (n & 0x55555555 != 0)


n = 16
print(Solution().isPowerOfFour(n))
