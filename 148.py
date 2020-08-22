"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 归并排序
    def sortList(self, head: ListNode) -> ListNode:

        def merge(head1, head2):
            p = dummy = ListNode(-1)
            while head1 and head2:
                if head1.val <= head2.val:
                    p.next, head1 = head1, head1.next
                else:
                    p.next, head2 = head2, head2.next
                p = p.next
            p.next = head1 or head2
            return dummy.next

        if not (head and head.next):
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return merge(self.sortList(head), self.sortList(slow))


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


inputs = [4, 2, 1, 3]
head = construct_listnodes(inputs)
print(show_listnodes(head))
print(show_listnodes(Solution().sortList(head)))
