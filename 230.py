"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:
    输入: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    输出: 1

示例 2:
    输入: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 普通做法. 未利用二叉搜索树的特性
    # 递归找到 左右子树 的 top-k 元素, 然后做合并
    def kthSmallest_1(self, root: TreeNode, k: int) -> int:
        def get_k_smallest(node):
            if not node:
                return []
            left_k_smallest = get_k_smallest(node.left)
            right_k_smallest = get_k_smallest(node.right)

            if len(left_k_smallest) == 0:
                left_k_smallest.append(node.val)
            else:
                for idx in range(len(left_k_smallest)):
                    if left_k_smallest[idx] > node.val:
                        left_k_smallest.insert(idx, node.val)
                        break
                else:
                    if len(left_k_smallest) < k:
                        left_k_smallest.append(node.val)

            # merge
            rets = []
            idx, jdx, kdx = 0, 0, 0
            while idx < len(left_k_smallest) and jdx < len(right_k_smallest):
                if left_k_smallest[idx] < right_k_smallest[jdx]:
                    rets.append(left_k_smallest[idx])
                    idx += 1
                else:
                    rets.append(left_k_smallest[idx])
                    jdx += 1
                if len(rets) > k:
                    break
            else:
                if jdx < len(right_k_smallest):
                    rets.extend(right_k_smallest[jdx: jdx + k - len(rets)])
                elif idx < len(left_k_smallest):
                    rets.extend(left_k_smallest[idx: idx + k - len(rets)])
            # print(node.val, rets, left_k_smallest, right_k_smallest)
            return rets

        rets = get_k_smallest(root)
        if len(rets) < k:
            return 0
        else:
            return rets[k-1]

    # 递归
    # 利用二叉搜索树的特性可知，中序遍历结果是升序的
    def kthSmallest_2(self, root: TreeNode, k: int) -> int:

        def in_order(node):
            return in_order(node.left) + [node.val] + in_order(node.right) if node else []
        return in_order(root)[k-1]

    # 迭代
    # 利用二叉搜索树的特性可知，中序遍历结果是升序的
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


def construct_tree(num_list):
    all_nodes = [None if num is None else TreeNode(num) for num in num_list]
    for idx, node in enumerate(all_nodes):
        if node is not None:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            node.left = all_nodes[left_child_idx] if left_child_idx < len(num_list) else None
            node.right = all_nodes[right_child_idx] if right_child_idx < len(num_list) else None
    return all_nodes[0]


root = construct_tree([3, 1, 4, None, 2])
k = 1
root = construct_tree([5, 3, 6, 2, 4, None, None, 1])
k = 3
print(Solution().kthSmallest(root, k))
