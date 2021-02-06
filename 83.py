"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
    输入: 1->1->2
    输出: 1->2

示例 2:
    输入: 1->1->2->3->3
    输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pt_slow, pt_fast = head, head
        while pt_fast:
            if pt_fast.val != pt_slow.val:
                pt_slow.next = pt_fast
                pt_slow = pt_slow.next
            pt_fast = pt_fast.next
        if pt_slow:
            pt_slow.next = None
        return head
