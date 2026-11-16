# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # NONE 1 2 3 4(prev) NONE(curr)
        while curr:
            temp = curr.next
            # reverse
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        