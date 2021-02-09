"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例 1:
    输入:
        nums1 = [3, 4, 6, 5]
        nums2 = [9, 1, 2, 5, 8, 3]
        k = 5
    输出:
        [9, 8, 6, 5, 3]

示例 2:
    输入:
        nums1 = [6, 7]
        nums2 = [6, 0, 4]
        k = 5
    输出:
        [6, 7, 6, 0, 4]

示例 3:
    输入:
        nums1 = [3, 9]
        nums2 = [8, 9]
        k = 3
    输出:
        [9, 8, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/create-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 从 nums1 中寻找长度为 k1 的最大字串，从 nums2 中寻找长度为 k2 的最大字串，其中 k1 + k2 = k. 之后将两个串进行合并.
    # 遍历比较所有不同的 k1, k2 组合.
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        nums1_size = len(nums1)
        nums2_size = len(nums2)

        def cmp(in_nums1, in_nums2):
            in_nums1_size = len(in_nums1)
            in_nums2_size = len(in_nums2)
            for idx in range(min(in_nums1_size, in_nums2_size)):
                if in_nums1[idx] > in_nums2[idx]:
                    return 1
                elif in_nums1[idx] < in_nums2[idx]:
                    return -1
            return in_nums1_size - in_nums2_size

        def generate_max_subtring(in_nums, target_length):
            res = []
            to_delete = len(in_nums) - target_length
            for idx in range(len(in_nums)):
                while to_delete and res and res[-1] < in_nums[idx]:
                    res.pop()
                    to_delete -= 1
                res.append(in_nums[idx])
            return res[:target_length]

        def merge(in_nums1, in_nums2):
            res = []
            in_nums1_size, in_nums2_size = len(in_nums1), len(in_nums2)
            idx1, idx2 = 0, 0
            while idx1 < in_nums1_size or idx2 < in_nums2_size:
                if cmp(in_nums1[idx1:], in_nums2[idx2:]) >= 0:
                    res.append(in_nums1[idx1])
                    idx1 += 1
                else:
                    res.append(in_nums2[idx2])
                    idx2 += 1
            return res

        max_value = [0] * k
        for k1 in range(min(k + 1, nums1_size + 1)):
            k2 = k - k1
            if 0 <= k2 <= nums2_size:
                sub_nums1 = generate_max_subtring(nums1, k1)
                sub_nums2 = generate_max_subtring(nums2, k2)
                out_nums = merge(sub_nums1, sub_nums2)
                # print(sub_nums1, sub_nums2, out_nums)
                if cmp(out_nums, max_value) > 0:
                    max_value = out_nums
        return max_value


nums1, nums2, k = [3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5
nums1, nums2, k = [6, 7], [6, 0, 4], 5
nums1, nums2, k = [8, 6, 9], [1, 7, 5], 3
nums1, nums2, k = [1, 2], [], 2
nums1, nums2, k = [2, 5, 6, 4, 4, 0], [7, 3, 8, 0, 6, 5, 7, 6, 2], 15
print(Solution().maxNumber(nums1, nums2, k))
