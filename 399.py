"""
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:

    # 最简单的带权并查集
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parents, weights = {}, {}

        def find(var):
            """ 寻找元素 var 的根 root_var, 以及 var / root_var 的结果 """
            if parents[var] == var:
                return var, 1.0
            root_var, root_value = find(parents[var])
            return root_var, root_value * weights[var]

        for idx in range(len(equations)):
            equation = equations[idx]
            value = values[idx]
            for var in equation:
                if var not in parents:
                    parents[var] = var
                    weights[var] = 1.0

            root_var0, root_value0 = find(equation[0])
            root_var1, root_value1 = find(equation[1])
            if root_var0 != root_var1:
                # union
                parents[root_var0] = root_var1
                weights[root_var0] = value * root_value1 / root_value0
        rets = []
        for query in queries:
            if query[0] not in parents or query[1] not in parents:
                rets.append(-1.0)
            else:
                query0_root, query0_value = find(query[0])
                query1_root, query1_value = find(query[1])
                if query0_root != query1_root:
                    rets.append(-1.0)
                else:
                    rets.append(query0_value / query1_value)
        return rets


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

equations = [["a", "e"], ["b", "e"]]
values = [4.0, 3.0]
queries = [["a", "b"], ["e", "e"], ["x", "x"]]

equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
values = [3.0, 4.0, 5.0, 6.0]
queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]

equations = [["a", "b"], ["e", "f"], ["b", "e"]]
values = [3.4, 1.4, 2.3]
queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]

print(Solution().calcEquation(equations, values, queries))
