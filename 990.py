"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。
在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

示例 1：
    输入：["a==b","b!=a"]
    输出：false
    解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
示例 2：
    输入：["b==a","a==b"]
    输出：true
    解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
示例 3：
    输入：["a==b","b==c","a==c"]
    输出：true
示例 4：
    输入：["a==b","b!=c","c==a"]
    输出：false
示例 5：
    输入：["c==c","b==d","x!=z"]
    输出：true

提示：
    1 <= equations.length <= 500
    equations[i].length == 4
    equations[i][0] 和 equations[i][3] 是小写字母
    equations[i][1] 要么是 '='，要么是 '!'
    equations[i][2] 是 '='


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/satisfiability-of-equality-equations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    class UF(object):

        def __init__(self, size):
            self.parent = []
            self.rank = []
            self.count = size
            for i in range(0, size):
                self.parent.append(i)
                self.rank.append(0)

        def find(self, i):
            # with path compression
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

            # another impl
            # root = i
            # while root != self.parent[root]:
            #     self.parent[root] = self.parent[self.parent[root]]
            #     root = self.parent[root]
            # return root

        def connected(self, i, j):
            return self.find(i) == self.find(j)

        def union(self, i, j):
            p = self.find(i)
            q = self.find(j)
            if p == q: return
            if self.rank[p] < self.rank[q]:
                self.parent[p] = q
            elif self.rank[p] > self.rank[q]:
                self.parent[q] = p
            else:
                self.parent[q] = p
                self.rank[p] += 1
            self.count -= 1

    # 利用 并查集
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UF(26)

        for equation in equations:
            if equation[1] == "=":
                uf.union(ord(equation[0])-ord('a'), ord(equation[-1])-ord('a'))

        for equation in equations:
            if equation[1] == "!":
                if uf.connected(ord(equation[0])-ord('a'), ord(equation[-1])-ord('a')):
                    return False
        return True


