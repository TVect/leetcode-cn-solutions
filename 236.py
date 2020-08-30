"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]


示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 若 root != p and root != q. 递归:
        # 若左右均包含 p 或 q，则返回 root
        # 若左边不包含 p 或 q，则返回 右边
        # 若右边不包含 p 或 q，则返回 左边
        if (not root) or (root.val == p.val) or (root.val == q.val):
            return root
        else:
            left_contain = self.lowestCommonAncestor(root.left, p, q)
            right_contain = self.lowestCommonAncestor(root.right, p, q)
            if left_contain and right_contain:
                return root
            if left_contain is None:
                return right_contain
            if right_contain is None:
                return left_contain

    def lowestCommonAncestor_1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 后序遍历的同时，记下是否包含指定的节点
        common = []

        def contain_target(node):
            if node is None:
                return False, False
            if len(common) != 0:
                return True, True

            contain_p_left, contain_q_left = contain_target(node.left)
            contain_p_right, contain_q_right = contain_target(node.right)
            contain_p = (node.val == p.val) or contain_p_left or contain_p_right
            contain_q = (node.val == q.val) or contain_q_left or contain_q_right

            if contain_p and contain_q:
                if len(common) == 0:
                    common.append(node)
            return contain_p, contain_q

        contain_target(root)
        return None if len(common) == 0 else common[0]


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


root = construct_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = TreeNode(5)
q = TreeNode(1)

p = TreeNode(5)
q = TreeNode(4)

print(Solution().lowestCommonAncestor(root, p, q))
