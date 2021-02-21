"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
    输入: n = 4, k = 2
    输出:
        [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrace(partial):
            if len(partial) == k:
                res.append(partial)

            possible_choice_start = partial[-1]+1 if partial else 1
            for val in range(possible_choice_start, n+1):
                backtrace(partial+[val])

        backtrace([])
        return res


n, k = 4, 2
print(Solution().combine(n, k))
