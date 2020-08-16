"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    # 动态规划
    def maxProduct_1(self, nums: List[int]) -> int:
        dp_max = [1] * len(nums)  # dp_max[i]: 表示以 num[i-1] 为终止的最大连续乘积
        dp_min = [1] * len(nums)  # dp_min[i]: 表示以 num[i-1] 为终止的最小连续乘积
        for i, num in enumerate(nums):
            dp_max[i] = max(dp_max[i - 1] * num, dp_min[i - 1] * num, num)
            dp_min[i] = min(dp_max[i - 1] * num, dp_min[i - 1] * num, num)
        return max(max(dp_max), max(dp_min))

    # 动态规划 + 滚动数组
    def maxProduct(self, nums: List[int]) -> int:
        max_curr = 1    # max_curr 表示以当前位置为终止的最大连续乘积
        min_curr = 1    # min_curr 表示以当前位置为终止的最小连续乘积
        max_global = -float('inf')
        for num in nums:
            max_curr, min_curr = max(max_curr * num, min_curr * num, num), min(max_curr * num, min_curr * num, num)
            max_global = max(max_global, max_curr)
        return max_global


nums = [2, 3, -2, 4]
nums = [-2, 0, -1]
nums = [0, 2]
print(Solution().maxProduct(nums))
