"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
    输入：nums = [1,1,2]
    输出：
        [[1,1,2],
         [1,2,1],
         [2,1,1]]

示例 2：
    输入：nums = [1,2,3]
    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
提示：
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrace(partial, choices):
            if not choices:
                res.append(partial)
            for choice in set(choices):
                idx = choices.index(choice)
                backtrace(partial + [choice], choices[:idx] + choices[idx+1:])

        backtrace([], nums)
        return res


nums = [1, 2, 1]
print(Solution().permuteUnique(nums))
