"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

示例 1：
    输入：nums1 = [1,3], nums2 = [2]
    输出：2.00000
    解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
    输入：nums1 = [1,2], nums2 = [3,4]
    输出：2.50000
    解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
    输入：nums1 = [0,0], nums2 = [0,0]
    输出：0.00000

示例 4：
    输入：nums1 = [], nums2 = [1]
    输出：1.00000

示例 5：
    输入：nums1 = [2], nums2 = []
    输出：2.00000

提示：

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 二分查找
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_size = len(nums1)
        nums2_size = len(nums2)

        def helper(in_nums1, in_nums2, target_order):
            """ 从 nums1[nums1_start : num1_end] 和 nums2[nums2_start: nums2_end] 中寻找 第 target_order 小的值 """
            in_nums1_size = len(in_nums1)
            in_nums2_size = len(in_nums2)
            if in_nums1_size == 0:
                return nums2[target_order]
            if in_nums2_size == 0:
                return nums1[target_order]

            if target_order == 0:
                return min(in_nums1[0], in_nums2[0])
            if target_order == in_nums1_size + in_nums2_size - 1:
                return max(in_nums1[-1], in_nums2[-1])

            mid = target_order // 2
            nums1_idx = mid
            nums2_idx = target_order - mid - 1

            if nums1_idx >= in_nums1_size:
                nums1_idx = in_nums1_size - 1
                nums2_idx = target_order - nums1_idx - 1
            elif nums2_idx >= in_nums2_size:
                nums2_idx = in_nums2_size - 1
                nums1_idx = target_order - nums2_idx - 1
            # print(in_nums1, nums1_idx, target_order)
            # print(in_nums2, nums2_idx, target_order)
            if in_nums1[nums1_idx] < in_nums2[nums2_idx]:
                return helper(in_nums1[nums1_idx+1:], in_nums2[:nums2_idx+1], target_order - nums1_idx - 1)
            elif in_nums1[nums1_idx] > in_nums2[nums2_idx]:
                return helper(in_nums1[:nums1_idx+1], in_nums2[nums2_idx+1:], target_order - nums2_idx - 1)
            else:
                return in_nums1[nums1_idx]

        mid = (nums1_size + nums2_size) // 2
        if mid * 2 != nums1_size + nums2_size:
            return helper(nums1, nums2, mid)
        else:
            return (helper(nums1, nums2, mid) + helper(nums1, nums2, mid-1)) / 2


nums1, nums2 = [1, 3], [2]
nums1, nums2 = [1, 2], [3, 4]
nums1, nums2 = [], [1]
nums1, nums2 = [2], []
nums1, nums2 = [1, 3], [2, 7]
print(Solution().findMedianSortedArrays(nums1, nums2))
