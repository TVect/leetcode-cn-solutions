"""
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

示例 1：
    输入：root = [1,3,null,null,2]
    输出：[3,1,null,null,2]
    解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

示例 2：
    输入：root = [3,1,4,null,null,2]
    输出：[2,1,4,null,null,3]
    解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。

提示：
    树上节点的数目在范围 [2, 1000] 内
    -2^31 <= Node.val <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 显式中序遍历
    # 如果有两对错误顺序 a_{i} >= a_{i+1}, a_{j} >= a_{j+1}  (i+1<j). 表明 a_{i} 和 a_{j+1} 这两个节点是被错误的交换了的
    # 如果只有一对错误顺序 a_{i} >= a_{i+1}. 表明 a_{i} 和 a_{i+1} 这两个节点是被错误的交换了的
    def recoverTree_1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        last_node = None
        err_pairs = []

        def inorder(node):
            nonlocal last_node
            if node is None:
                # 其他优化：错误对 最多只有两对，如果找到了就可以提前退出
                return

            inorder(node.left)
            if last_node and node.val <= last_node.val:
                err_pairs.append([last_node, node])
            last_node = node
            inorder(node.right)

        inorder(root)
        if len(err_pairs) == 2:
            # swap err_pairs[0][0] & err_pairs[1][1]
            err_pairs[0][0].val, err_pairs[1][1].val = err_pairs[1][1].val, err_pairs[0][0].val
        elif len(err_pairs) == 1:
            # swap err_pairs[0][0] & err_pairs[0][1]
            err_pairs[0][0].val, err_pairs[0][1].val = err_pairs[0][1].val, err_pairs[0][0].val

    # Morris 中序遍历
    def recoverTree(self, root: TreeNode) -> None:
        node = root
        last_node, err_pairs = None, []
        while node:
            if node.left:
                # 如果右左孩子，找到左孩子的最右侧叶子节点
                most_right = node.left
                while most_right.right and most_right.right != node:
                    most_right = most_right.right

                if most_right.right is None:
                    # 最右侧叶子节点的 right 指针为 空. 表明是第一次访问到 node 节点
                    most_right.right = node
                    node = node.left
                else:
                    # 如果最右侧叶子节点的 right 指针不为空. 表明是第二次访问到 node 节点
                    if last_node and node.val <= last_node.val:
                        err_pairs.append([last_node, node])
                    last_node = node
                    most_right.right = None
                    node = node.right
            else:
                # 如果没有左孩子，则向右移动
                if last_node and node.val <= last_node.val:
                    err_pairs.append([last_node, node])
                last_node = node
                node = node.right
        if len(err_pairs) == 2:
            # swap err_pairs[0][0] & err_pairs[1][1]
            err_pairs[0][0].val, err_pairs[1][1].val = err_pairs[1][1].val, err_pairs[0][0].val
        elif len(err_pairs) == 1:
            # swap err_pairs[0][0] & err_pairs[0][1]
            err_pairs[0][0].val, err_pairs[0][1].val = err_pairs[0][1].val, err_pairs[0][0].val


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


def inorder(root):
    res = []

    def helper(node):
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)

    helper(root)
    return res


root = construct_tree([1, 3, None, None, 2])
Solution().recoverTree(root)
print(inorder(root))
