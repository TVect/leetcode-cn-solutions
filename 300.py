"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 动态规划做法
    # 时间复杂度：O(n^2)
    def lengthOfLIS_1(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size == 0:
            return 0
        dp = [1] * nums_size  # dp[i] 表示以 nums[i] 为结尾的最大上升子序列长度
        for idx in range(nums_size):
            dp[idx] = max([dp[jdx] + 1 if nums[jdx] < nums[idx] else 1 for jdx in range(0, idx + 1)])
        return max(dp)

    # 二分查找
    # 时间复杂度：O(n log n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] 表示(到目前位置)长度为 l+1 的递增子串的最小后缀
        tails = []
        for num in nums:
            # 二分查找得到第一个大于 num 的数
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left >= len(tails):
                tails.append(num)
            else:
                tails[left] = num
        return len(tails)


nums = [10, 9, 2, 5, 3, 7, 101, 18, 19]
nums = []
nums = [4, 10, 4, 3, 8, 9]
print(Solution().lengthOfLIS(nums))
