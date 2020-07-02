"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 深度优先
    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        rets = []

        def helper(cur_items, cur_idx):
            rets.append(cur_items)
            for idx in range(cur_idx, len(nums)):
                tmp_items = [nums[idx]] + cur_items
                helper(tmp_items, idx+1)

        helper([], 0)
        return rets

    # 广度优先
    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        rets = []
        task_queue = [[[], 0]]
        while len(task_queue):
            items, cur_idx = task_queue.pop(0)
            rets.append(items)
            for idx in range(cur_idx, len(nums)):
                tmp_items = [nums[idx]] + items
                task_queue.append([tmp_items, idx+1])

        return rets

    # 迭代
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rets = [[]]
        for num in nums:
            rets.extend([ret+[num] for ret in rets])
        return rets


nums = [1, 2, 3]
print(Solution().subsets(nums))
