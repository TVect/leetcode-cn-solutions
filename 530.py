"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：
    输入：
       1
        \
         3
        /
       2
    输出：
        1

解释：
    最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

提示：
    树中至少有 2 个节点。
    本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        min_diff = float('inf')
        last_val = -float('inf')

        def inorder(node):
            nonlocal min_diff, last_val
            if node:
                inorder(node.left)
                min_diff = min(node.val - last_val, min_diff)
                last_val = node.val
                inorder(node.right)

        inorder(root)
        return min_diff
