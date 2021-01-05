"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
    给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    满足要求的三元组集合为：
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_size = len(nums)

        def n_sum_target(start, end, target, n):
            rets = []
            if n == 2:
                while start < end:
                    summation = nums[start] + nums[end]
                    start_num, end_num = nums[start], nums[end]
                    if summation < target:
                        while start < end and nums[start] == start_num:
                            start += 1
                    elif nums[start] + nums[end] > target:
                        while start < end and nums[end] == end_num:
                            end -= 1
                    else:
                        rets.append([nums[start], nums[end]])
                        while start < end and nums[start] == start_num:
                            start += 1
                        while start < end and nums[end] == end_num:
                            end -= 1
            else:
                while start < end:
                    for ret in n_sum_target(start+1, end, target-nums[start], n-1):
                        rets.append([nums[start]] + ret)
                    tmp_num = nums[start]
                    while start < end and nums[start] == tmp_num:
                        start += 1
            return rets

        return n_sum_target(0, nums_size-1, 0, 3)


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
