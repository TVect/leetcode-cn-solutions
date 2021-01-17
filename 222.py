"""
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:
    输入:
            1
           / \
          2   3
         / \  /
        4  5 6

    输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_hight, left_node = 0, root
        while left_node:
            left_node = left_node.left
            left_hight += 1

        right_hight, right_node = 0, root
        while right_node:
            right_node = right_node.right
            right_hight += 1

        if left_hight == right_hight:
            return math.pow(2, left_hight) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
