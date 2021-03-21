"""
树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。
给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），
其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。
在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
 
示例 1：
    输入：n = 4, edges = [[1,0],[1,2],[1,3]]
    输出：[1]
    解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。

示例 2：
    输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    输出：[3,4]

示例 3：
    输入：n = 1, edges = []
    输出：[0]

示例 4：
    输入：n = 2, edges = [[0,1]]
    输出：[0,1]
 
提示：
    1 <= n <= 2 * 10^4
    edges.length == n - 1
    0 <= ai, bi < n
    ai != bi
    所有 (ai, bi) 互不相同
    给定的输入 保证 是一棵树，并且 不会有重复的边

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 朴素 BFS, 会超时
    def findMinHeightTrees_1(self, n: int, edges: List[List[int]]) -> List[int]:
        list_of_status = [[[idx], set([idx])] for idx in range(n)]
        neighbors = {}
        for edge in edges:
            if edge[0] not in neighbors:
                neighbors[edge[0]] = []
            neighbors[edge[0]].append(edge[1])
            if edge[1] not in neighbors:
                neighbors[edge[1]] = []
            neighbors[edge[1]].append(edge[0])

        empty_queue = []
        while len(empty_queue) == 0:
            for idx, status in enumerate(list_of_status):
                queue, visited = status
                queue_size = len(queue)
                for _ in range(queue_size):
                    node = queue.pop(0)
                    for neighbor in neighbors.get(node, []):
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                if len(queue) == 0:
                    empty_queue.append(idx)

        return empty_queue

    # 带记忆的 DFS：会超过递归深度
    def findMinHeightTrees_2(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = {}
        for edge in edges:
            if edge[0] not in neighbors:
                neighbors[edge[0]] = []
            neighbors[edge[0]].append(edge[1])
            if edge[1] not in neighbors:
                neighbors[edge[1]] = []
            neighbors[edge[1]].append(edge[0])

        memo = {}

        def dfs(root, node):
            """ 表示前一个节点为 root, 以 node 为根的树的深度 """
            if (root, node) in neighbors:
                return memo[(root, node)]
            height = 1 + max([dfs(node, child) for child in neighbors.get(node, []) if child != root], default=-1)
            memo[(root, node)] = height
            return height

        heights = [dfs(-1, idx) for idx in range(n)]
        min_height = min(heights)
        return [idx for idx in range(n) if heights[idx] == min_height]

    # 拓扑排序
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = {idx: set([]) for idx in range(n)}
        indegree = [0] * n
        for edge in edges:
            neighbors[edge[0]].add(edge[1])
            neighbors[edge[1]].add(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1

        nodes_to_remove = []
        while neighbors:
            nodes_to_remove = [node for node in neighbors if 0 <= indegree[node] <= 1]
            for node in nodes_to_remove:
                for neighbor in neighbors[node]:
                    indegree[neighbor] -= 1
                del neighbors[node]
        return nodes_to_remove


n, edges = 4, [[1, 0], [1, 2], [1, 3]]
n, edges = 6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(Solution().findMinHeightTrees(n, edges))
