"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
    1 ≤ m ≤ n ≤ 链表长度。

示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 迭代求解
    def reverseBetween_1(self, head: ListNode, m: int, n: int) -> ListNode:
        prev_node, cur_node, next_node = None, head, head.next if head else None
        range_head, range_tail = None, None
        for idx in range(0, n):
            if idx == m-1:
                range_head = prev_node
                range_tail = cur_node

            if idx >= m:
                cur_node.next = prev_node
            prev_node, cur_node, next_node = cur_node, next_node, next_node.next if next_node else None
        if range_head:
            range_head.next = prev_node
        if range_tail:
            range_tail.next = cur_node

        if m == 1:
            return prev_node
        return head

    # 迭代求解
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        successor = None

        def reverseTopN(node, n):
            """逆转最开始的N个节点"""
            global successor
            if n == 1:
                successor = node.next
                return node
            last = reverseTopN(node.next, n - 1)
            node.next.next = node
            node.next = successor
            return last

        if m == 1:
            return reverseTopN(head, n)
        else:
            head.next = self.reverseBetween(head.next, m-1, n-1)
            return head


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


head = construct_listnodes([1, 2, 3, 4, 5])
print(show_listnodes(head))
node = Solution().reverseBetween(head, 2, 4)
print(show_listnodes(node))
