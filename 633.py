"""
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。

示例 1：
    输入：c = 5
    输出：true
    解释：1 * 1 + 2 * 2 = 5

示例 2：
    输入：c = 3
    输出：false

示例 3：
    输入：c = 4
    输出：true

示例 4：
    输入：c = 2
    输出：true

示例 5：
    输入：c = 1
    输出：true

提示：
    0 <= c <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-square-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            summation = left * left + right * right
            if summation == c:
                return True
            elif summation > c:
                right -= 1
            else:
                left += 1
        return False


c = 2
print(Solution().judgeSquareSum(c))
