"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

示例 1：
    输入：root = [1,null,2,3]
    输出：[1,2,3]

示例 2：
    输入：root = []
    输出：[]

示例 3：
    输入：root = [1]
    输出：[1]

示例 4：
    输入：root = [1,2]
    输出：[1,2]

示例 5：
    输入：root = [1,null,2]
    输出：[1,2]

提示：
    树中节点数目在范围 [0, 100] 内
    -100 <= Node.val <= 100

进阶：递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
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

    # 迭代算法
    def preorderTraversal_1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        node = root
        while node:
            res.append(node.val)
            if node.left:
                stack.append(node)
                node = node.left
            elif node.right:
                node = node.right
            else:
                while stack:
                    node = stack.pop()
                    if node.right:
                        node = node.right
                        break
                else:
                    break
        return res

    # 迭代算法：版本2
    def preorderTraversal_2(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    # 迭代算法：版本3
    def preorderTraversal_3(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    # 递归算法
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
