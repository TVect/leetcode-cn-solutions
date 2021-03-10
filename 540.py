"""
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:
    输入: [1,1,2,3,3,4,4,8,8]
    输出: 2

示例 2:
    输入: [3,3,7,7,10,11,11]
    输出: 10

注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def singleNonDuplicate(self, nums: List[int]) -> int:
        nums_size = len(nums)
        left, right = 0, nums_size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid - 1]:
                if (mid - left + 1) % 2 == 0:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] == nums[mid + 1]:
                if (mid - left + 1) % 2 == 0:
                    right = mid - 1
                else:
                    left = mid
            else:
                return nums[mid]
        return nums[left]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
nums = [3, 3, 7, 7, 10, 11, 11]
print(Solution().singleNonDuplicate(nums))
