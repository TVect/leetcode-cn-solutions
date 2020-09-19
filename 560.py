"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 前缀和 + 哈希表优化
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums[i, ..., j] 的连续和为 k，等价于 reduce_sum[0, ..., j] - reduce_sum[0, ..., i-1] = k
        # 所以下面的做法中只要记录前缀和即可
        prefix_sum = {0: 1}  # 到当前位置的 累加和：累加和出现的次数
        # reduce_sum: 前缀和
        # count: 累计满足条件的连续子序列长度（子序列和为k）
        reduce_sum, count = 0, 0
        for num in nums:
            reduce_sum += num
            count += prefix_sum.get(reduce_sum - k, 0)
            prefix_sum[reduce_sum] = prefix_sum.get(reduce_sum, 0) + 1
        return count


nums = [1]
k = 0
nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(Solution().subarraySum(nums, k))
