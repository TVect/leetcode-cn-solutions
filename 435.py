"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:
    可以认为区间的终点总是大于它的起点。
    区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:
    输入: [ [1,2], [2,3], [3,4], [1,3] ]
    输出: 1
    解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例 2:
    输入: [ [1,2], [1,2], [1,2] ]
    输出: 2
    解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

示例 3:
    输入: [ [1,2], [2,3] ]
    输出: 0
    解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 贪心算法
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[1])
        # print(intervals)
        left_bound = -float('inf')
        res = 0
        for interval in intervals:
            if interval[0] >= left_bound:
                # 与之前选出的那个 interval 是不相交的
                left_bound = interval[1]
            else:
                # 与之前选出的那个 interval 是相交的
                res += 1
        return res

    # 动态规划算法
    def eraseOverlapIntervals_1(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        # print(intervals)
        intervals_cnt = len(intervals)
        # dp[i] 表示以 intervals[i] 作为最后一个区间时，可以选出的不相交区间的个数
        dp = [1] * intervals_cnt
        for idx in range(intervals_cnt):
            dp[idx] = max([dp[jdx] + 1 for jdx in range(0, idx) if intervals[jdx][1] <= intervals[idx][0]],
                          default=1)
        return intervals_cnt - dp[-1]


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(Solution().eraseOverlapIntervals(intervals))
