# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(start, counter):
            # reverse linked list
            prev = None
            cur = start
            while cur and counter < right:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                counter += 1
            # 3->2->1->None
            start.next = cur
            return prev

        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        counter = 0
        while curr:
            if counter + 1 == left:
                curr.next = reverse(curr.next, counter)
                break
            curr = curr.next
            counter += 1

        return dummy.next

        