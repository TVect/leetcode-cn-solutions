"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
    输入: [1,2,3]
    输出:
        [ [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1] ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        rets = []

        def backtrack(res_nums, cur_nums):
            if len(res_nums) == 0:
                rets.append(cur_nums)
            else:
                for i in range(len(res_nums)):
                    backtrack(res_nums[:i] + res_nums[i+1:], cur_nums + [res_nums[i]])

        backtrack(nums, [])
        return rets


nums = [1, 2, 3]
print(Solution().permute(nums))
