"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。
少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。
相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:
    输入: [1,7,4,9,2,5]
    输出: 6
    解释: 整个序列均为摆动序列。

示例 2:
    输入: [1,17,5,10,13,15,10,5,16,8]
    输出: 7
    解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。

示例 3:
    输入: [1,2,3,4,5,6,7,8,9]
    输出: 2

进阶:
    你能否用 O(n) 时间复杂度完成此题?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 动态规划
    def wiggleMaxLength_1(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size < 2:
            return nums_size
        # dp[i][0] 表示以nums[i] 为结尾的最长摆动序列长度, 最后为上升
        # dp[i][1] 表示以nums[i] 为结尾的最长摆动序列长度, 最后为下降
        dp = [[1, 1] for _ in range(nums_size)]
        for idx in range(1, nums_size):
            dp[idx][0] = max([dp[jdx][1] + 1 for jdx in range(idx) if nums[idx] > nums[jdx]], default=1)
            dp[idx][1] = max([dp[jdx][0] + 1 for jdx in range(idx) if nums[idx] < nums[jdx]], default=1)
        return max(max(dp[idx]) for idx in range(nums_size))

    # 贪心算法1. 找到有几个波峰+波谷即可
    def wiggleMaxLength_2(self, nums: List[int]) -> int:
        nums_size = len(nums)
        prev = nums[0]
        res = 1
        for idx in range(1, nums_size):
            # 找到第一个与 nums[0] 不同的元素
            if nums[idx] != prev:
                curr = nums[idx]
                res = 2
                for num in nums[idx + 1:]:
                    # 贪心的找摆动元素
                    if (num - curr) * (curr - prev) < 0:
                        prev, curr = curr, num
                        res += 1
                    else:
                        curr = num
                break
        return res

    # 贪心算法2. 找到有几个波峰+波谷即可
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size < 2:
            return nums_size

        prev_diff = nums[1] - nums[0]
        res = 1 if prev_diff == 0 else 2
        for idx in range(2, nums_size):
            diff = nums[idx] - nums[idx-1]
            if (diff > 0 >= prev_diff) or (diff < 0 <= prev_diff):
                res += 1
                prev_diff = diff
        return res


nums = [1, 7, 4, 9, 2, 5]
nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Solution().wiggleMaxLength(nums))
