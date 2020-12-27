"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
    你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 
示例 1：
    输入：nums = [5,7,7,8,8,10], target = 8
    输出：[3,4]

示例 2：
    输入：nums = [5,7,7,8,8,10], target = 6
    输出：[-1,-1]

示例 3：
    输入：nums = [], target = 0
    输出：[-1,-1]

提示：
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums 是一个非递减数组
    -10^9 <= target <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # find left bound of target
        left, right = 0, len(nums) - 1
        while left < right:
            # 希望 mid 是更靠左边的, 这样可以保证 right = mid 时能缩小搜索区间
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        left_bound = left if nums[left] == target else -1

        # find right bound of target
        left, right = 0, len(nums) - 1
        while left < right:
            # 希望 mid 是更靠右边的, 这样可以保证 left = mid 时能缩小搜索区间
            mid = left + (right - left + 1) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        right_bound = right if nums[right] == target else -1

        return [left_bound, right_bound]


nums, target = [5, 7, 7, 8, 8, 10], 8
nums, target = [], 0
nums, target = [2, 2], 3
print(Solution().searchRange(nums, target))
