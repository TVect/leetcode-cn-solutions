"""
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

    输入:
        2
       / \
      1   3

    输出: 1
 

示例 2:

    输入:

            1
           / \
          2   3
         /   / \
        4   5   6
           /
          7

    输出: 7
 

注意: 您可以假设树（即给定的根节点）不为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-bottom-left-tree-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        res = None
        while queue:
            level_size = len(queue)
            res = queue[0].val
            for idx in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
