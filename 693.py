"""
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

示例 1：
    输入：n = 5
    输出：true
    解释：5 的二进制表示是：101

示例 2：
    输入：n = 7
    输出：false
    解释：7 的二进制表示是：111.

示例 3：
    输入：n = 11
    输出：false
    解释：11 的二进制表示是：1011.

示例 4：
    输入：n = 10
    输出：true
    解释：10 的二进制表示是：1010.

示例 5：
    输入：n = 3
    输出：false

提示：
    1 <= n <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-number-with-alternating-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def hasAlternatingBits_1(self, n: int) -> bool:
        while n:
            if n & 3 != 1 and n & 3 != 2:
                return False
            n >>= 1
        return True

    def hasAlternatingBits(self, n: int) -> bool:
        # 如果 n 是01交错的形式，那么 n ^ (n>>1) 的二进制位必然全为1
        n = n ^ (n >> 1)
        return (n + 1) & n == 0


n = 4
print(Solution().hasAlternatingBits(n))
