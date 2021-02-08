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

    # 动态规划 + 二分查找
    # 时间复杂度：O(n log n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 表示以长度为 i 的最大上升子序列的末尾元素的最小值
        # dp[i] 则应该是一个单调递增的序列
        dp = [nums[0]]
        for num in nums[1:]:
            if num > dp[-1]:
                dp.append(num)
            else:
                # 二分查找到 num 应该所在的位置: dp 中第一个大于 num 的数
                left_idx, right_idx = 0, len(dp) - 1
                while left_idx < right_idx:
                    mid_idx = (left_idx + right_idx) // 2
                    if num > dp[mid_idx]:
                        left_idx = mid_idx + 1
                    else:
                        right_idx = mid_idx
                dp[left_idx] = num
        return len(dp)

    # 标准的动态规划做法
    # 时间复杂度：O(n^2)
    def lengthOfLIS_1(self, nums: List[int]) -> int:
        nums_size = len(nums)
        # dp[i] 表示以 i 为结尾的最长上升子序列
        dp = [1] * nums_size
        for idx in range(nums_size):
            for jdx in range(idx):
                if nums[jdx] < nums[idx]:
                    dp[idx] = max(dp[idx], dp[jdx] + 1)
        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18, 19]
nums = []
nums = [4, 10, 4, 3, 8, 9]
print(Solution().lengthOfLIS(nums))
