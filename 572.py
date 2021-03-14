"""
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。
s 也可以看做它自身的一棵子树。

示例 1:
    给定的树 s:
             3
            / \
           4   5
          / \
         1   2
    给定的树 t：
           4
          / \
         1   2
    返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
    给定的树 s：
             3
            / \
           4   5
          / \
         1   2
            /
           0
    给定的树 t：
           4
          / \
         1   2
    返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def is_same(tree1, tree2):
            """ 判断两棵树是否相同 """
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            return tree1.val == tree2.val and is_same(tree1.left, tree2.left) and is_same(tree1.right, tree2.right)

        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return is_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
