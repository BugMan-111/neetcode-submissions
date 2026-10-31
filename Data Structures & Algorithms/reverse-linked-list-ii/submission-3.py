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
            curr = start
            while curr and counter < right:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                counter += 1
            # 3->2->1->None
            start.next = curr
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

        