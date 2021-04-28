"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：
    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]

示例 2：
    输入：l1 = [], l2 = []
    输出：[]

示例 3：
    输入：l1 = [], l2 = [0]
    输出：[0]

提示：
    两个链表的节点数目范围是 [0, 50]
    -100 <= Node.val <= 100
    l1 和 l2 均按 非递减顺序 排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pt_l1, pt_l2 = l1, l2
        head = ListNode("dummpy")
        pt_tmp = head
        while pt_l1 and pt_l2:
            if pt_l1.val < pt_l2.val:
                pt_tmp.next = pt_l1
                pt_l1 = pt_l1.next
            else:
                pt_tmp.next = pt_l2
                pt_l2 = pt_l2.next
            pt_tmp = pt_tmp.next

        pt_tmp.next = pt_l1 if pt_l1 else pt_l2

        return head.next
