"""
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
在完成所有删除操作后，请你返回列表中剩余区间的数目。

示例：
    输入：intervals = [[1,4],[3,6],[2,8]]
    输出：2
    解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。

提示：​​​​​​
    1 <= intervals.length <= 1000
    0 <= intervals[i][0] < intervals[i][1] <= 10^5
    对于所有的 i != j：intervals[i] != intervals[j]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-covered-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def removeCoveredIntervals_1(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: [item[0], -item[1]])
        right_bound, keep_cnt = 0, 0
        for interval in intervals:
            if interval[1] <= right_bound:
                pass
            else:
                right_bound = interval[1]
                keep_cnt += 1
        return keep_cnt

    # 更细致的区分为 3 中情况进行讨论
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: [item[0], -item[1]])
        left, right = 0, 0
        cnt = 0
        for interval in intervals:
            if interval[0] <= right:
                if interval[1] <= right:
                    # Case1. 新的区间完全包含在老的区间中
                    cnt += 1
                else:
                    # Case2. 新的区间和老的区间有重叠
                    right = interval[1]
            else:
                # Case3. 新的区间和老的区间完全没有重合
                left, right = interval[0], interval[1]
        return len(intervals) - cnt


intervals = [[1, 4], [3, 6], [2, 8]]
intervals = [[1, 2], [1, 4], [3, 4]]
print(Solution().removeCoveredIntervals(intervals))
