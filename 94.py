"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # recursive
    def inorderTraversal_1(self, root: TreeNode) -> List[int]:
        rets = []

        def helper(current_node):
            if current_node is not None:
                helper(current_node.left)
                rets.append(current_node.val)
                helper(current_node.right)

        helper(root)

        return rets

    # 基于栈的遍历
    def inorderTraversal_2(self, root: TreeNode) -> List[int]:
        rets = []
        stack = []
        current_node = root
        while current_node is not None:
            # 入栈左节点直到叶节点
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left
            # 出栈：
            # 如果无右节点可以直接出栈；
            # 如果有右节点，需要在节点出栈之后，将右节点及其子节点入栈
            while len(stack) > 0:
                node = stack.pop()
                rets.append(node.val)
                if node.right is not None:
                    current_node = node.right
                    break
        return rets

    # 线索二叉树 & 莫里斯遍历
    def inorderTraversal_3(self, root: TreeNode) -> List[int]:
        rets = []
        current_node = root
        while current_node is not None:
            if current_node.left is not None:
                # 寻找左子树的最右边节点, 将current_node及其右子树挂在该节点下
                node = current_node.left
                tmp_root = current_node.left
                while node.right is not None:
                    node = node.right
                current_node.left = None
                node.right = current_node
                current_node = tmp_root
            else:
                rets.append(current_node.val)
                current_node = current_node.right
        return rets

    # 莫里斯遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        rets = []
        current_node = root
        while current_node is not None:
            if current_node.left is not None:
                # 寻找左子树的最右边节点, 将current_node及其右子树挂在该节点下
                node = current_node.left
                while node.right and node.right != current_node:
                    node = node.right
                if node.right is None:
                    node.right = current_node
                    current_node = current_node.left
                else:
                    rets.append(current_node.val)
                    node.right = None
                    current_node = current_node.right

            else:
                rets.append(current_node.val)
                current_node = current_node.right
        return rets


node = TreeNode(3)
node.right = None
node.left = None

parent_node = TreeNode(2)
parent_node.left = node
parent_node.right = None

node = parent_node
parent_node = TreeNode(1)
parent_node.left = None
parent_node.right = node

root = parent_node
print(Solution().inorderTraversal(root))
