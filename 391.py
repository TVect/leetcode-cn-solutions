"""
我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。

每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 
( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。

示例 1:
    rectangles = [[1,1,3,3],
                  [3,1,4,2],
                  [3,2,4,4],
                  [1,3,2,4],
                  [2,3,3,4]]
    返回 true。5个矩形一起可以精确地覆盖一个矩形区域。

示例 2:
    rectangles = [[1,1,2,3],
                  [1,3,2,4],
                  [3,1,4,2],
                  [3,2,4,4]]
    返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。

示例 3:
    rectangles = [[1,1,3,3],
                  [3,1,4,2],
                  [1,3,2,4],
                  [3,2,4,4]]
    返回 false。图形顶端留有间隔，无法覆盖成一个矩形。

示例 4:
    rectangles = [[1,1,3,3],
                  [3,1,4,2],
                  [1,3,2,4],
                  [2,2,4,4]]
    返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 获取最终的左下角和右上角坐标
        bottom_left = [min(rectangle[0] for rectangle in rectangles),
                       min(rectangle[1] for rectangle in rectangles)]
        top_right = [max(rectangle[2] for rectangle in rectangles),
                     max(rectangle[3] for rectangle in rectangles)]
        # 条件1: 面积相等
        area_sum = sum((rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1]) for rectangle in rectangles)
        if area_sum != (top_right[0] - bottom_left[0]) * (top_right[1] - bottom_left[1]):
            return False
        # 条件2: 统计顶点的重复次数
        counter = {}
        for rectangle in rectangles:
            counter[(rectangle[0], rectangle[1])] = counter.get((rectangle[0], rectangle[1]), 0) + 1
            counter[(rectangle[2], rectangle[3])] = counter.get((rectangle[2], rectangle[3]), 0) + 1
            counter[(rectangle[0], rectangle[3])] = counter.get((rectangle[0], rectangle[3]), 0) + 1
            counter[(rectangle[2], rectangle[1])] = counter.get((rectangle[2], rectangle[1]), 0) + 1
        # 所有的非最终顶点只能出现偶数次，或者说 最终出现1次的 只能是 最终四个顶点
        for key, value in counter.items():
            if key in [(bottom_left[0], bottom_left[1]),
                       (top_right[0], top_right[1]),
                       (bottom_left[0], top_right[1]),
                       (top_right[0], bottom_left[1])]:
                if value != 1:
                    return False
            else:
                if value % 2 != 0:
                    return False
        return True


rectangles = [[1, 1, 3, 3],
              [3, 1, 4, 2],
              [3, 2, 4, 4],
              [1, 3, 2, 4],
              [2, 3, 3, 4]]
# rectangles = [[1, 1, 2, 3],
#               [1, 3, 2, 4],
#               [3, 1, 4, 2],
#               [3, 2, 4, 4]]
# rectangles = [[1, 1, 3, 3],
#               [3, 1, 4, 2],
#               [1, 3, 2, 4],
#               [3, 2, 4, 4]]
# rectangles = [[1, 1, 3, 3],
#               [3, 1, 4, 2],
#               [1, 3, 2, 4],
#               [2, 2, 4, 4]]
# rectangles = [[0, 0, 2, 2],
#               [1, 1, 3, 3],
#               [2, 0, 3, 1],
#               [0, 3, 3, 4]]

print(Solution().isRectangleCover(rectangles))
