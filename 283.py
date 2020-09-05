"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 双指针
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt_zero = 0
        for pt in range(len(nums)):
            # (刚开始的运行情况除外) nums[0 ... pt_zero-1] 均不为0, nums[pt_zero, ..., pt-1] 均为 0
            if nums[pt] != 0:
                if pt_zero != pt:
                    nums[pt_zero], nums[pt] = nums[pt], nums[pt_zero]
                pt_zero += 1

    # 双指针 更清晰的版本
    def moveZeroes_1(self, nums: List[int]) -> None:
        pt_zero = None
        for pt in range(len(nums)):
            # nums[0...pt_zero - 1] 均不为0, nums[pt_zero, ..., pt - 1] 均为 0
            if nums[pt] == 0:
                if pt_zero is None:
                    pt_zero = pt
            elif pt_zero is not None:
                nums[pt_zero], nums[pt] = nums[pt], nums[pt_zero]
                pt_zero += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
