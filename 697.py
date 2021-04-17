"""
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1：
    输入：[1, 2, 2, 3, 1]
    输出：2
    解释：
        输入数组的度是2，因为元素1和2的出现频数最大，均为2.
        连续子数组里面拥有相同度的有如下所示:
        [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
        最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2：
    输入：[1,2,2,3,1,4,2]
    输出：6

提示：
    nums.length 在1到 50,000 区间范围内。
    nums[i] 是一个在 0 到 49,999 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import collections


class Solution:

    # 滑动窗口法
    def findShortestSubArray_1(self, nums: List[int]) -> int:
        degree = max(collections.Counter(nums).values())
        min_size, nums_size = float("inf"), len(nums)
        left_idx, right_idx = 0, 0
        tmp_cnt = {}
        while right_idx < nums_size:
            # right_idx 扩张
            while right_idx < nums_size and max(tmp_cnt.values(), default=0) < degree:
                tmp_cnt[nums[right_idx]] = tmp_cnt.get(nums[right_idx], 0) + 1
                right_idx += 1
            # left_idx 收缩
            while left_idx < right_idx and max(tmp_cnt.values(), default=0) >= degree:
                min_size = min(min_size, right_idx - left_idx)
                tmp_cnt[nums[left_idx]] -= 1
                left_idx += 1
        return min_size

    # hash 表，记录位置法
    # 记原数组中出现次数最多的数为 x，
    # 那么和原数组的度相同的最短连续子数组，必然包含了原数组中的全部 x，且两端恰为 x 第一次出现和最后一次出现的位置。
    def findShortestSubArray(self, nums: List[int]) -> int:
        # key: num
        # value: [num 在 nums 中出现的次数，num 在 nums 中首次出现的位置, num 在 nums 中最后一次出现的位置]
        cnt = {}
        for idx, num in enumerate(nums):
            if num not in cnt:
                cnt[num] = [1, idx, idx]
            else:
                cnt[num][0] = cnt[num][0] + 1
                cnt[num][-1] = idx
        degree, min_size = 0, 0
        for key, value in cnt.items():
            if value[0] > degree:
                degree = value[0]
                min_size = value[2] - value[1] + 1
            elif value[0] == degree:
                min_size = min(min_size, value[2] - value[1] + 1)
        return min_size


nums = [1, 2, 2, 3, 1]
nums = [1, 2, 2, 3, 1, 4, 2]
print(Solution().findShortestSubArray(nums))
