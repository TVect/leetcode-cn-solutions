"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        rets = [[0] * n for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_id = 0
        pos_i, pos_j = 0, -1
        for num in range(1, n*n + 1):
            while True:
                tmp_pos_i, tmp_pos_j = pos_i + directions[direction_id][0], pos_j + directions[direction_id][1]
                if (0 <= tmp_pos_i < n) and (0 <= tmp_pos_j < n) and rets[tmp_pos_i][tmp_pos_j] == 0:
                    pos_i, pos_j = tmp_pos_i, tmp_pos_j
                    break
                else:
                    direction_id = (direction_id + 1) % 4
            rets[pos_i][pos_j] = num
        return rets


n = 4
print(Solution().generateMatrix(n))
