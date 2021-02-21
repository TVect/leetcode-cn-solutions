"""
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

示例：
    输入：board = [[1,2,3],[4,0,5]]
    输出：1
    解释：交换 0 和 5 ，1 步完成

    输入：board = [[1,2,3],[5,4,0]]
    输出：-1
    解释：没有办法完成谜板

    输入：board = [[4,1,2],[5,0,3]]
    输出：5
    解释：
        最少完成谜板的最少移动次数是 5 ，
        一种移动路径:
        尚未移动: [[4,1,2],[5,0,3]]
        移动 1 次: [[4,1,2],[0,5,3]]
        移动 2 次: [[0,1,2],[4,5,3]]
        移动 3 次: [[1,0,2],[4,5,3]]
        移动 4 次: [[1,2,0],[4,5,3]]
        移动 5 次: [[1,2,3],[4,5,0]]

    输入：board = [[3,2,4],[1,5,0]]
    输出：14

提示：
    board 是一个如上所述的 2 x 3 的数组.
    board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-puzzle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import itertools


class Solution:

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        tuple_board = tuple(itertools.chain(*board))
        queue = [[tuple_board, tuple_board.index(0)]]
        visited = {tuple_board}

        step = 0
        while len(queue):
            queue_size = len(queue)
            for _ in range(queue_size):
                state, pos_zero = queue.pop(0)
                if state == (1, 2, 3, 4, 5, 0):
                    return step
                for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    swap_idx = pos_zero // 3 + direction[0]
                    swap_jdx = pos_zero % 3 + direction[1]
                    if (0 <= swap_idx < 2) and (0 <= swap_jdx < 3):
                        new_idx = swap_idx * 3 + swap_jdx
                        tmp_list = list(state)
                        tmp_list[pos_zero], tmp_list[new_idx] = tmp_list[new_idx], tmp_list[pos_zero]
                        tmp_tuple = tuple(tmp_list)
                        if tmp_tuple not in visited:
                            queue.append([tmp_tuple, new_idx])
                            visited.add(tmp_tuple)
            step += 1
        return -1


board = [[1, 2, 3], [4, 0, 5]]
board = [[1, 2, 3], [5, 4, 0]]
board = [[4, 1, 2], [5, 0, 3]]
board = [[3, 2, 4], [1, 5, 0]]
print(Solution().slidingPuzzle(board))
