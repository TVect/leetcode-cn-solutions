"""
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

提示：
    输出坐标的顺序不重要
    m 和 n 都小于150

示例：
    给定下面的 5x5 矩阵:
      太平洋 ~   ~   ~   ~   ~
           ~  1   2   2   3  (5) *
           ~  3   2   3  (4) (4) *
           ~  2   4  (5)  3   1  *
           ~ (6) (7)  1   4   5  *
           ~ (5)  1   1   2   4  *
              *   *   *   *   * 大西洋

    返回:
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        n_rows, n_cols = len(matrix), len(matrix[0])

        def find_avaliable_coord(start_coords):
            """返回所有可以流到 start_coords 中的坐标"""
            visited = set(start_coords)
            while start_coords:
                coord = start_coords.pop(0)
                for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    new_coord = (coord[0] + direction[0], coord[1] + direction[1])
                    if 0 <= new_coord[0] < n_rows and 0 <= new_coord[1] < n_cols and new_coord not in visited:
                        if matrix[new_coord[0]][new_coord[1]] >= matrix[coord[0]][coord[1]]:
                            start_coords.append(new_coord)
                            visited.add(new_coord)
            return visited

        # 所有可以流到太平洋的坐标点
        visited1 = find_avaliable_coord(
            [(0, i) for i in range(n_cols)] + [(i, 0) for i in range(1, n_rows)])
        # 所有可以流到大西洋的坐标点
        visited2 = find_avaliable_coord(
            [(n_rows-1, i) for i in range(n_cols)] + [(i, n_cols-1) for i in range(n_rows-1)])
        return visited1 & visited2
