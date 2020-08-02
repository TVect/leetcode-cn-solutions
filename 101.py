"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归
    def isSymmetric_1(self, root: TreeNode) -> bool:
        def check(node1, node2):
            if (node1 is None) and (node2 is None):
                return True
            elif (node1 is None) or (node2 is None):
                return False
            else:
                return node1.val == node2.val and check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)

    # 迭代
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [[root.left, root.right]]
        while len(stack) > 0:
            node_l, node_r = stack.pop(0)
            if (node_l is None) and (node_r is None):
                continue
            elif (node_l is None) or (node_r is None):
                return False
            else:
                if node_l.val == node_r.val:
                    stack.append([node_l.left, node_r.right])
                    stack.append([node_l.right, node_r.left])
                else:
                    return False

        return True


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


root = construct_tree([1, 2, 2, 3, 4, 4, 3])
root = construct_tree([1, 2, 2, None, 3, None, 3])
print(Solution().isSymmetric(root))
