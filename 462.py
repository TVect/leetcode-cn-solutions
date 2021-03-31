"""
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:
    输入: [1,2,3]
    输出: 2

说明：
    只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 动态规划
    def minMoves2_1(self, nums: List[int]) -> int:
        nums.sort()
        nums_size = len(nums)
        # left[i] 记录 nums[:i] 移动到 统一数字 nums[i] 需要的步骤
        left = [0] * nums_size
        for idx in range(1, nums_size):
            left[idx] = left[idx-1] + idx * (nums[idx] - nums[idx-1])
        # right 记录 nums[i:] 移动到 统一数字 nums[i] 需要的步骤
        right = 0
        for idx in range(nums_size-2, -1, -1):
            right = right + (nums_size - idx - 1) * (nums[idx+1] - nums[idx])
            left[idx] += right

        return min(left)

    # 寻找中位数
    # 设 a <= x <= b，将 a 和 b 都变化成 x 为最终目的，则需要步数为 x - a + b - x = b - a，
    # 即两个数最后相等的话步数一定是他们的差，x 在 a 和 b 间任意取；
    # 所以最后剩的其实就是中位数；
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        nums_size = len(nums)
        # 方法一：
        # mid = nums_size // 2
        # return sum(abs(num - nums[mid]) for num in nums)

        # 方法二：
        left, right = 0, nums_size - 1
        res = 0
        while left < right:
            res += (nums[right] - nums[left])
            left += 1
            right -= 1
        return res


nums = [1, 2, 3]
print(Solution().minMoves2(nums))
