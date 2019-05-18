# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归
        if head is None or head.next is None:
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return new_head


class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 迭代
        cur = head
        new_head = None
        while cur:
            tmp = cur.next
            cur.next = new_head
            new_head = cur
            cur = tmp
        return new_head
