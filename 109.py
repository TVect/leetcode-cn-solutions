"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
    给定的有序链表： [-10, -3, 0, 5, 9],
    一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
          0
         / \
       -3   9
       /   /
     -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        count = 0

        tmp = head
        # 计算链表长度
        while tmp:
            count += 1
            tmp = tmp.next

        # 建树
        tmp = head

        def create_tree(left, right):
            if left > right:
                return None
            nonlocal tmp
            mid = (left + right) // 2
            node = TreeNode()
            node.left = create_tree(left, mid - 1)
            # 中序遍历的结果 恰好和 单链表遍历的结果 是一致的
            node.val, tmp = tmp.val, tmp.next
            node.right = create_tree(mid + 1, right)
            return node

        return create_tree(0, count-1)
