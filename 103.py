"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
    给定二叉树 [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    返回锯齿形层次遍历如下：
    [
      [3],
      [20,9],
      [15,7]
    ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
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

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack, ret = [root], []
        level = 0
        while len(stack) > 0:
            if level % 2 == 0:
                ret.append([node.val for node in stack])
            else:
                ret.append([node.val for node in stack[::-1]])
            num_nodes = len(stack)
            for _ in range(num_nodes):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            level += 1
        return ret


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
root = construct_tree([1, 2, 3, 4, None, None, 5])

print(Solution().zigzagLevelOrder(root))
