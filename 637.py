"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：
    输入：
        3
       / \
      9  20
        /  \
       15   7
    输出：[3, 14.5, 11]
    解释：
    第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

提示：
    节点值的范围在32位有符号整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        res = []
        while queue:
            level_size = len(queue)
            addition = 0
            for _ in range(level_size):
                node = queue.pop(0)
                addition += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(addition / level_size)
        return res
