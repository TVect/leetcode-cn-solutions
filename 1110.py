"""
给出二叉树的根节点 root，树上每个节点都有一个不同的值。
如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
返回森林中的每棵树。你可以按任意顺序组织答案。

示例：
    输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
    输出：[[1,2,null,4],[6],[7]]

提示：
    树中的节点数最大为 1000。
    每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
    to_delete.length <= 1000
    to_delete 包含一些从 1 到 1000、各不相同的值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-nodes-and-return-forest
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

    # 树的层次遍历，记录下 父节点和方向信息
    def delNodes_1(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = [] if root.val in to_delete else [root]
        # nodes: list of [node, parent_node, direction]
        nodes = [[root, None, "left"]]
        while nodes:
            node, parent, direction = nodes.pop(0)
            if not node:
                continue
            nodes.extend([[node.left, node, "left"], [node.right, node, "right"]])
            if node.val in to_delete:
                if parent:
                    setattr(parent, direction, None)
                if node.left and node.left.val not in to_delete:
                    res.append(node.left)
                if node.right and node.right.val not in to_delete:
                    res.append(node.right)
        return res

    # 后序遍历 + 记录父节点和方向信息
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = [] if root.val in to_delete else [root]

        def dfs(node, parent_node, direction):
            if not node:
                return
            dfs(node.left, node, "left")
            dfs(node.right, node, "right")
            if node.val in to_delete:
                if parent_node:
                    setattr(parent_node, direction, None)
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)

        dfs(root, None, "left")
        return res

