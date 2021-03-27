"""
对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：
对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。
那么数组 A 是漂亮数组。

给定 N，返回任意漂亮数组 A（保证存在一个）。

示例 1：
    输入：4
    输出：[2,1,4,3]

示例 2：
    输入：5
    输出：[3,1,2,5,4]

提示：
    1 <= N <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/beautiful-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 观察漂亮数组的一些性质
    # 1. A是一个漂亮数组，如果对A中所有元素做同样的仿射变换 (ax+b)，那么Ａ还是一个漂亮数组。
    # 2. A是一个漂亮数组，如果删除一些A中一些元素，那么A还是一个漂亮数组。
    # 3. A是一个奇数构成的漂亮数组，B是一个偶数构成的漂亮数组，那么A + B也是一个漂亮数组
    # 比如: {1, 5, 3, 7} + {2, 6, 4, 8} = {1, 5, 3, 7, 2, 6, 4, 8} 也是一个漂亮数组。
    def beautifulArray(self, N: int) -> List[int]:
        if N == 1:
            return [1]
        # 构造一个 奇数元素的漂亮数组 和 一个偶数元素的漂亮数组，将他们 concat 之后可以仍然保证是 漂亮数组
        odd = [item * 2 - 1 for item in self.beautifulArray((N+1) // 2)]
        even = [item * 2 for item in self.beautifulArray(N // 2)]
        return odd + even


N = 4
print(Solution().beautifulArray(N))
