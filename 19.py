"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

示例 1：
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]

示例 2：
    输入：head = [1], n = 1
    输出：[]

示例 3：
    输入：head = [1,2], n = 1
    输出：[1]

提示：
    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 添加一个哑节点（dummy node），它的 next 指针指向链表的头节点。
        # 这样一来，我们就不需要对头节点进行特殊的判断了。
        node = ListNode(-1)
        node.next = head
        first = second = node
        for i in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return node.next
