"""
给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
返回这两个区间列表的交集。

（形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。
两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

示例：
    输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

提示：
    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interval-list-intersections
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def intervalIntersection_1(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        size_A, size_B = len(A), len(B)
        idx_A, idx_B = 0, 0
        intersections = []
        while idx_A < size_A and idx_B < size_B:
            interval_A, interval_B = A[idx_A], B[idx_B]
            if interval_A[0] <= interval_B[0]:
                if interval_B[0] <= interval_A[1] < interval_B[1]:
                    intersections.append([interval_B[0], interval_A[1]])
                    idx_A += 1
                elif interval_A[1] >= interval_B[1]:
                    intersections.append(interval_B)
                    idx_B += 1
                else: # interval_A[1] < interval
                    idx_A += 1
            else: # interval_A[0] > interval_B[0]
                if interval_A[0] <= interval_B[1] < interval_A[1]:
                    intersections.append([interval_A[0], interval_B[1]])
                    idx_B += 1
                elif interval_B[1] >= interval_A[1]:
                    intersections.append(interval_A)
                    idx_A += 1
                else:
                    idx_B += 1
        return intersections

    # 简化之后的做法
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        size_A, size_B = len(A), len(B)
        idx_A, idx_B = 0, 0
        intersections = []
        while idx_A < size_A and idx_B < size_B:
            interval_A, interval_B = A[idx_A], B[idx_B]
            # 有交集：not (interval_A[1] < interval_B[0] and interval_B[1] < interval_A[0])
            if interval_A[1] >= interval_B[0] and interval_B[1] >= interval_A[0]:
                intersections.append([max(interval_A[0], interval_B[0]), min(interval_A[1], interval_B[1])])
            if interval_A[1] <= interval_B[1]:
                idx_A += 1
            else:
                idx_B += 1

        return intersections


A, B = [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]
print(Solution().intervalIntersection(A, B))
