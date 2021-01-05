"""
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 迭代法做前序遍历
    def flatten_1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        rets = []
        node = root
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                rets.append(node)
                node = node.left
            node = stack.pop(-1)
            node = node.right

        tree_size = len(rets)
        for idx in range(tree_size):
            rets[idx].left = None
            if idx + 1 < tree_size:
                rets[idx].right = rets[idx+1]
            else:
                rets[idx].right = None

    # 前序遍历 + 同时做展开
    def flatten_2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stack = [root]
        prev_node = None
        while len(stack) > 0:
            node = stack.pop(-1)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if prev_node:
                prev_node.left = None
                prev_node.right = node
            prev_node = node

    # 原地操作：找到每个节点的前驱节点
    def flatten_3(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            # 找到 左子树 的最右边节点
            if node.left:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = node.right

                node.right = node.left
                node.left = None
            node = node.right

    # 递归解法
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return root
        self.flatten(root.left)
        self.flatten(root.right)

        left_node, right_node = root.left, root.right
        root.left, root.right = None, left_node
        p = root
        while p.right:
            p = p.right
        p.right = right_node


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


root = construct_tree([1, 2, 5, 3, 4, None, 6])
Solution().flatten(root)
