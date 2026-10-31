# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy_least, dummy_max = ListNode(-5005, None), ListNode(5005, None)
        dummy_least.next = dummy_max
        while curr:
            # find a pos for dummy
            temp = curr.next
            result_curr = dummy_least
            while result_curr and result_curr.next:
                if result_curr.val <= curr.val <= result_curr.next.val:
                    # insert the curr between result_curr and 
                    temp_result_curr = result_curr.next
                    result_curr.next = curr
                    curr.next = temp_result_curr
                    break
                else:
                    result_curr = result_curr.next
            curr = temp
        curr = dummy_least
        while curr and curr.next and curr.next.next:
            curr = curr.next
        curr.next = None
        return dummy_least.next