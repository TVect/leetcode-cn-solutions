"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 
提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 排序 + 双指针
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums_size = len(nums)
        closest_summation = float('inf')
        for idx in range(nums_size):
            if idx > 0 and (nums[idx] == nums[idx-1]):
                continue
            pt_left = idx + 1
            pt_right = nums_size - 1
            while pt_left < pt_right:
                summation = nums[pt_left] + nums[pt_right] + nums[idx]
                if abs(summation - target) < abs(closest_summation - target):
                    closest_summation = summation
                if summation > target:
                    pt_right -= 1
                elif summation < target:
                    pt_left += 1
                else:
                    return target
        return closest_summation


nums = [-1, 2, 1, -4]
target = 1
nums = [0, 2, 1, -3]
target = 1
print(Solution().threeSumClosest(nums, target))
