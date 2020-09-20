"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:
输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

说明 :
输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 排序比较法
    def findUnsortedSubarray_1(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        distincts = [idx for idx in range(len(nums)) if nums[idx] != sorted_nums[idx]]
        return distincts[-1] - distincts[0] + 1 if distincts else 0

    # 两次遍历
    # 第一次从左向右，找到右边界 （违反升序的最大值应该所在的位置）
    # 第二次从右向左，找到左边界
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_size = len(nums)
        right_bound, max_value = 0, -float("inf")
        for idx in range(nums_size):
            if nums[idx] >= max_value:
                max_value = nums[idx]
            else:
                right_bound = idx
        print(right_bound, max_value)

        left_bound, min_value = nums_size-1, float("inf")
        for idx in range(nums_size-1, -1, -1):
            if nums[idx] <= min_value:
                min_value = nums[idx]
            else:
                left_bound = idx
        print(left_bound, min_value)
        return right_bound - left_bound + 1 if left_bound < right_bound else 0


nums = [2, 6, 4, 8, 10, 9, 15]
nums = [1, 2, 3, 4]
nums = [1, 2, 3, 3, 3]
nums = [1, 3, 5, 4, 2]
print(Solution().findUnsortedSubarray(nums))
