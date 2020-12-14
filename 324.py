"""
给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

示例 1:
    输入: nums = [1, 5, 1, 1, 6, 4]
    输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]

示例 2:
    输入: nums = [1, 3, 2, 2, 3, 1]
    输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
    说明:
        你可以假设所有输入都会得到有效的结果。

进阶:
    你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-sort-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import time


class Solution:

    # 快速选择算法：O(n) 时间找到中位数
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_size = len(nums)
        mid_id = nums_size // 2

        def find_kth(k, start_idx, end_idx):

            while start_idx < end_idx:
                left_idx, right_idx = start_idx, end_idx
                while left_idx < right_idx:
                    while nums[right_idx] >= nums[left_idx] and (right_idx > left_idx):
                        right_idx -= 1
                    nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                    while nums[left_idx] <= nums[right_idx] and (right_idx > left_idx):
                        left_idx += 1
                    nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

                if left_idx == k:
                    return nums[left_idx]
                elif left_idx < k:
                    start_idx = left_idx+1
                else:
                    end_idx = right_idx-1
            return nums[start_idx]

        """
        def find_kth(k, left_idx, right_idx):
            start_idx, end_idx = left_idx, right_idx
            while left_idx < right_idx:
                while nums[right_idx] >= nums[left_idx] and (right_idx > left_idx):
                    right_idx -= 1
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                while nums[left_idx] <= nums[right_idx] and (right_idx > left_idx):
                    left_idx += 1
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

            if left_idx - start_idx == k:
                return nums[left_idx]
            elif left_idx - start_idx > k:
                return find_kth(k, start_idx, left_idx - 1)
            else:
                return find_kth(k - (left_idx + 1 - start_idx), left_idx + 1, end_idx)
        """
        mid_element = find_kth(mid_id, 0, nums_size - 1)
        # 3-way-partition
        # 将 小于 nums[mid] 的元素放在右边, 等于 nums[mid] 的元素放在中间, 大于 nums[mid] 的元素放在右边
        left, curr, right = 0, 0, nums_size - 1
        while curr <= right:
            if nums[curr] > mid_element:
                nums[curr], nums[left] = nums[left], nums[curr]
                curr += 1
                left += 1
            elif nums[curr] < mid_element:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

        # 交叉合并: nums[right_idx, right_idx - 1, mid_idx] 和 nums[mid_idx-1, mid_idx-2, ..., 0] 进行合并
        left_idx, right_idx = 0, mid_id
        while right_idx < nums_size:
            nums.insert(left_idx, nums.pop(right_idx))
            left_idx += 2
            right_idx += 1


nums = [1, 5, 1, 1, 6, 4]
nums = [1, 3, 2, 2, 3, 1]
nums = [1]
Solution().wiggleSort(nums)
print(nums)
