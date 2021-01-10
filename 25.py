"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
    给你这个链表：1->2->3->4->5
    当 k = 2 时，应当返回: 2->1->4->3->5
    当 k = 3 时，应当返回: 3->2->1->4->5

说明：
    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 迭代法
    def reverseKGroup_1(self, head: ListNode, k: int) -> ListNode:

        def reverse_top_n(node, n):
            """逆转前面 n 个元素"""
            prev_node, cur_node, next_node = None, node, node.next if head else None
            for idx in range(n):
                cur_node.next = prev_node
                prev_node, cur_node, next_node = cur_node, next_node, next_node.next if next_node else None
            return prev_node

        new_head, last_tail = None, None
        start_node, next_start_node = head, None
        while start_node:
            next_start_node = start_node
            tmp_head = start_node
            for i in range(k):
                if next_start_node is None:
                    break
                next_start_node = next_start_node.next
            else:
                tmp_head = reverse_top_n(start_node, k)

            if last_tail:
                last_tail.next = tmp_head
            else:
                new_head = tmp_head
            last_tail = start_node

            start_node = next_start_node

        return new_head

    # 递归法
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse_top_n(node, n):
            """逆转前面 n 个元素"""
            prev_node, cur_node, next_node = None, node, node.next if head else None
            for idx in range(n):
                cur_node.next = prev_node
                prev_node, cur_node, next_node = cur_node, next_node, next_node.next if next_node else None
            return prev_node

        if head is None:
            return None

        tmp_node = head
        for _ in range(k):
            if tmp_node is None:
                return head
            tmp_node = tmp_node.next

        new_head = reverse_top_n(head, k)
        head.next = self.reverseKGroup(tmp_node, k)
        return new_head


def construct_listnodes(inputs):
    nodes = [ListNode(val) for val in inputs]
    for node1, node2 in zip(nodes[:-1], nodes[1:]):
        node1.next = node2
    return nodes[0]


def show_listnodes(head):
    rets = []
    pt = head
    while pt:
        rets.append(pt.val)
        pt = pt.next
    return rets


head = construct_listnodes([1, 2])
print(show_listnodes(head))
node = Solution().reverseKGroup(head, 2)
print(show_listnodes(node))
