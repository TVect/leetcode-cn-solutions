"""
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:
    输入: [[1,1],[2,2],[3,3]]
    输出: 3
    解释:
        ^
        |
        |        o
        |     o
        |  o  
        +------------->
        0  1  2  3  4

示例 2:
    输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    输出: 4
    解释:
        ^
        |
        |  o
        |     o        o
        |        o
        |  o        o
        +------------------->
        0  1  2  3  4  5  6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        points_size = len(points)

        def get_points_in_a_line(pt_idx):
            # 经过 pt_idx 的直线上有多少个点
            points_cnt = {}
            duplicates = 1
            for pt_jdx in range(pt_idx+1, points_size):
                if points[pt_idx] == points[pt_jdx]:
                    # 两个点重复
                    duplicates += 1
                elif points[pt_idx][0] == points[pt_jdx][0]:
                    # 两个点在同一条垂直线上
                    points_cnt["vertical"] = points_cnt.get("vertical", 0) + 1
                else:
                    # 两个点可以计算斜率
                    # TODO 浮点数精确性保证
                    slope = (points[pt_jdx][1] - points[pt_idx][1]) / (points[pt_jdx][0] - points[pt_idx][0])
                    points_cnt[slope] = points_cnt.get(slope, 0) + 1
            return duplicates + max(points_cnt.values(), default=0)

        return max(get_points_in_a_line(idx) for idx in range(points_size))


points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(Solution().maxPoints(points))
