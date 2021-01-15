"""
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：
    节点的左子树仅包含键 小于 节点键的节点。
    节点的右子树仅包含键 大于 节点键的节点。
    左右子树也必须是二叉搜索树。

注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/  相同

示例 1：
    输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

示例 2：
    输入：root = [0,null,1]
    输出：[1,null,1]

示例 3：
    输入：root = [1,0,2]
    输出：[3,3,2]

示例 4：
    输入：root = [3,2,4,1]
    输出：[7,9,4,10]

提示：
    树中的节点数介于 1 和 100 之间。
    每个节点的值介于 0 和 100 之间。
    树中的所有值 互不相同 。
    给定的树为二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        addition = 0

        def helper(node):
            nonlocal addition
            if node:
                helper(node.right)
                addition = node.val = addition + node.val
                helper(node.left)

        helper(root)
        return root

    # 线索二叉树


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


root = construct_tree([5, 2, 13])
print(Solution().convertBST(root))
