"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：true

示例 2：
    输入：root = [1,2,2,3,3,null,null,4,4]
    输出：false

示例 3：
    输入：root = []
    输出：true
 
提示：
    树中的节点数在范围 [0, 5000] 内
    -10^4 <= Node.val <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:

        def helper(node):
            '''
            :return: balance or not, height
            '''
            if not node:
                return True, 0
            left_balance, left_height = helper(node.left)
            right_balance, right_height = helper(node.right)
            if left_balance and right_balance and abs(right_height - left_height) <= 1:
                return True, max(right_height, left_height) + 1
            else:
                return False, max(right_height, left_height) + 1

        return helper(root)[0]
