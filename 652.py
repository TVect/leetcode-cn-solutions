"""
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-duplicate-subtrees
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

    # 序列化二叉树 或者 给二叉树一个唯一标示
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        all_nodes = {}
        rets = []

        def traverse(node):
            if node is not None:
                # 后序遍历，给每个节点一个唯一标示
                # node_id = {"left": traverse(node.left),
                #            "right": traverse(node.right),
                #            "val": node.val}
                node_uid = (node.val, traverse(node.left), traverse(node.right))
                if all_nodes.get(node_uid, 0) == 1:
                    rets.append(node)
                all_nodes[node_uid] = all_nodes.get(node_uid, 0) + 1
                return node_uid
            else:
                return "#"

        traverse(root)
        return rets


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


root = construct_tree(
    [1, 2, 3, 4, None, 2, 4, None, None, None, None, 4, None, None, None, None])
print(Solution().findDuplicateSubtrees(root))
