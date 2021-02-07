"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
    输入：nums = [1]
    输出：1

示例 3：
    输入：nums = [0]
    输出：0

示例 4：
    输入：nums = [-1]
    输出：-1

示例 5：
    输入：nums = [-100000]
    输出：-100000

提示：
    1 <= nums.length <= 3 * 10^4
    -10^5 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 动态规划
    def maxSubArray_1(self, nums: List[int]) -> int:
        nums_size = len(nums)
        # dp[i]: 以 i 为结尾的子数组的最大和
        dp = [num for num in nums]
        for idx in range(1, nums_size):
            dp[idx] = max(dp[idx - 1] + nums[idx], nums[idx])
        return max(dp)

    # 动态规划 + 空间优化
    def maxSubArray(self, nums: List[int]) -> int:
        res, dp = -float('inf'), 0
        for num in nums:
            dp = max(dp + num, num)
            res = max(res, dp)
        return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
