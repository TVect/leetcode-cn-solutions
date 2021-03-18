"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
    输入:
           1
         /   \
        2     3
         \
          5

输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
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

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [f"{root.val}"]
        res = []
        for path in self.binaryTreePaths(root.left):
            res.append(f"{root.val}->{path}")
        for path in self.binaryTreePaths(root.right):
            res.append(f"{root.val}->{path}")
        return res

