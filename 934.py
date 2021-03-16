"""
在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）

示例 1：
    输入：A = [[0,1],[1,0]]
    输出：1

示例 2：
    输入：A = [[0,1,0],[0,0,0],[0,0,1]]
    输出：2

示例 3：
    输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    输出：1

提示：
    2 <= A.length == A[0].length <= 100
    A[i][j] == 0 或 A[i][j] == 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-bridge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        # 找到第一个桥
        n_rows = len(A)
        n_cols = len(A[0])
        for idx in range(n_rows * n_cols):
            row_idx = idx // n_cols
            col_idx = idx % n_cols
            if A[row_idx][col_idx] == 1:
                queue = [[row_idx, col_idx]]
                A[row_idx][col_idx] = -1
                while queue:
                    coord = queue.pop(0)
                    for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        new_coord = [coord[0] + direction[0], coord[1] + direction[1]]
                        if 0 <= new_coord[0] < n_rows and 0 <= new_coord[1] < n_cols and \
                                A[new_coord[0]][new_coord[1]] == 1:
                            queue.append(new_coord)
                            A[new_coord[0]][new_coord[1]] = -1
                break

        queue1 = [[idx, jdx] for idx in range(n_rows) for jdx in range(n_cols) if A[idx][jdx] == -1]
        queue2 = [[idx, jdx] for idx in range(n_rows) for jdx in range(n_cols) if A[idx][jdx] == 1]

        step = 0
        while True:
            # 选择某个 queue，往前走一步
            queue1_size, queue2_size = len(queue1), len(queue2)
            if queue1_size < queue2_size:
                cur_queue, cur_queue_size = queue1, queue1_size
            else:
                cur_queue, cur_queue_size = queue2, queue2_size

            for _ in range(cur_queue_size):
                coord = cur_queue.pop(0)
                for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    new_coord = [coord[0] + direction[0], coord[1] + direction[1]]
                    if 0 <= new_coord[0] < n_rows and 0 <= new_coord[1] < n_cols:
                        if A[new_coord[0]][new_coord[1]] == 0:
                            A[new_coord[0]][new_coord[1]] = A[coord[0]][coord[1]]
                            cur_queue.append(new_coord)
                        elif A[new_coord[0]][new_coord[1]] + A[coord[0]][coord[1]] == 0:
                            return step
            step += 1


A = [[1, 1, 1, 1, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1]]
A = [[1, 1, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 1, 1]]

print(Solution().shortestBridge(A))
