# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        truncate = 0
        dummy = ListNode(-1)
        res = dummy
        while l1 or l2 or truncate:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + truncate
            val, truncate = s % 10, s // 10
            res.next = ListNode(val)
            res = res.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return dummy.next

        