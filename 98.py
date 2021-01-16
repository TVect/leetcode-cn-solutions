"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归解法
    def isValidBST_1(self, root: TreeNode) -> bool:

        def is_in_bound(node, lower_bound, upper_bound):
            if node is None:
                return True
            return (lower_bound < node.val < upper_bound) and \
                   is_in_bound(node.left, lower_bound, node.val) and \
                   is_in_bound(node.right, node.val, upper_bound)

        return is_in_bound(root, -float('inf'), float('inf'))

    # 用迭代法做中序遍历，同时判断得到的数字是否从小到大
    def isValidBST_2(self, root: TreeNode) -> bool:
        stack = []
        last_val = -float('inf')

        current_node = root
        while current_node is not None or len(stack) > 0:
            if current_node is not None:
                stack.append(current_node)
                current_node = current_node.left
            else:
                node = stack.pop()
                if node.val <= last_val:
                    return False
                else:
                    last_val = node.val
                current_node = node.right
        return True

    # 用递归法做中序遍历，同时判断得到的数字是否从小到大
    def isValidBST(self, root: TreeNode) -> bool:

        last_node_val = -float('inf')

        def traverse(node):
            nonlocal last_node_val
            if node is not None:
                if not traverse(node.left) or node.val <= last_node_val:
                    return False
                last_node_val = node.val
                if not traverse(node.right):
                    return False
            return True

        return traverse(root)


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


root = construct_tree([5, 1, 4, None, None, 3, 6])
root = construct_tree([2, 1, 3])
root = construct_tree([10, 5, 15, None, None, 6, 20])
print(Solution().isValidBST(root))
