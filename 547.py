"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

示例 1：
    输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    输出：2

示例 2：
    输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    输出：3

提示：
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] 为 1 或 0
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 广度优先做法
    def findCircleNum_1(self, isConnected: List[List[int]]) -> int:
        nums_size = len(isConnected)
        component_cnt = 0
        parsed_nums = [False] * nums_size

        def bfs(num_id):
            queue = [num_id]
            parsed_nums[num_id] = True
            while queue:
                ele = queue.pop(0)
                for idx, val in enumerate(isConnected[ele]):
                    if val and not parsed_nums[idx]:
                        queue.append(idx)
                        parsed_nums[idx] = True

        for idx in range(nums_size):
            if not parsed_nums[idx]:
                bfs(idx)
                component_cnt += 1
        return component_cnt

    # 并查集
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nums_size = len(isConnected)
        parents = list(range(nums_size))

        def union(idx, jdx):
            parents[find(idx)] = find(jdx)

        def find(idx):
            if parents[idx] == idx:
                return idx
            return find(parents[idx])

        for idx in range(nums_size):
            for jdx in range(idx + 1, nums_size):
                if isConnected[idx][jdx]:
                    union(idx, jdx)
        return sum(find(idx) == idx for idx in range(nums_size))


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(Solution().findCircleNum(isConnected))
