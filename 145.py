"""
给定一个二叉树，返回它的 后序 遍历。

示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3
    输出: [3,2,1]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
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

    # 递归解法
    def postorderTraversal_1(self, root: TreeNode) -> List[int]:
        res = []

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                res.append(node.val)

        postorder(root)
        return res

    # 栈迭代
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        node, last_node = root, None
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            if node.right and node.right != last_node:
                # 该节点有右子节点，且右子节点未被访问
                stack.append(node)
                node = node.right
            else:
                # 该节点没有右子节点, 或者 右子节点已被访问
                res.append(node.val)
                last_node = node
                node = None
        return res

    # Morris 迭代
    def postorderTraversal_2(self, root: TreeNode) -> List[int]:
        pass


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


root = construct_tree([3, 9, 20, None, None, 15, 7])
print(Solution().postorderTraversal(root))

