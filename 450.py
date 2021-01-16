"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：
    首先找到需要删除的节点；
    如果找到了，删除它。

说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:
    root = [5,3,6,2,4,null,7]
    key = 3

        5
       / \
      3   6
     / \   \
    2   4   7

    给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

    一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

        5
       / \
      4   6
     /     \
    2       7

    另一个正确答案是 [5,2,6,null,4,null,7]。

        5
       / \
      2   6
       \   \
        4   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deleteNode_1(self, root: TreeNode, key: int) -> TreeNode:
        # find the node
        parent, node = None, root
        while node and node.val != key:
            parent = node
            node = node.left if node.val > key else node.right
        if not node:
            return root

        # delete the node
        # 待删除的节点没有子节点
        if not node.left and not node.right:
            if not parent:
                return None
            if parent.left == node:
                parent.left = None
            elif parent.right == node:
                parent.right = None
            return root
        # 待删除的节点有两个子节点
        elif node.left and node.right:
            # 寻找左子树的最大值或者右子树的最小值. 这里是寻找右子树的最小值
            tmp_node_parent, tmp_node = node, node.right
            while tmp_node.left:
                tmp_node_parent = tmp_node
                tmp_node = tmp_node.left
            if tmp_node_parent.left == tmp_node:
                tmp_node_parent.left = tmp_node.right
            else:
                tmp_node_parent.right = tmp_node.right
            node.val = tmp_node.val
            return root
        # 待删除的节点有且仅有一个子节点
        else:
            new_node = node.left if node.left else node.right
            if not parent:
                return new_node
            if parent.left == node:
                parent.left = new_node
            elif parent.right == node:
                parent.right = new_node
            return root

    # 递归法
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if root.val == key:
            if root.left is None and root.right is None:
                # 待删除的节点为叶子节点
                return None
            elif root.left and root.right:
                # 待删除的节点有两个子节点
                # 获取右子树的最小值
                tmp_node = root.right
                while tmp_node.left:
                    tmp_node = tmp_node.left
                root.val = tmp_node.val
                root.right = self.deleteNode(root.right, tmp_node.val)
            else:
                # 待删除的节点有且仅有一个子节点
                return root.left if root.left else root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
