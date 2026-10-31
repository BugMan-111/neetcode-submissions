# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(-5002, None)
        result = dummy
        while curr:
            # find a pos for dummy
            temp = curr.next
            result_curr = dummy
            inserted_flag = False
            while result_curr and result_curr.next:
                if result_curr.val <= curr.val <= result_curr.next.val:
                    # insert the curr between result_curr and 
                    inserted_flag = True
                    temp_result_curr = result_curr.next
                    result_curr.next = curr
                    curr.next = temp_result_curr
                    break
                else:
                    result_curr = result_curr.next
            if not inserted_flag:
                result_curr.next = curr
                curr.next = None
            curr = temp
        return dummy.next