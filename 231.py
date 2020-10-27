"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
    输入: 1
    输出: true
    解释: 20 = 1

示例 2:
    输入: 16
    输出: true
    解释: 24 = 16

示例 3:
    输入: 218
    输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def isPowerOfTwo_1(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 2:
            n, mod = divmod(n, 2)
            if mod != 0:
                return False
        return True

    # 位运算：获取二进制中最右边的 1
    def isPowerOfTwo_2(self, n: int) -> bool:
        return False if n == 0 else n & (-n) == n

    # 位运算：去除二进制中最右边的 1
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n == 0 else n & (n - 1) == 0


n = 16
print(Solution().isPowerOfTwo(n))
