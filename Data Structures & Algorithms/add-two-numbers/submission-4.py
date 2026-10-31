# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recur(l1, l2, carry):
            if l1 is None and l2 is None and carry == 0:
                return None
            # add two numbers
            val1 = l1.val if l1 else 0
            val2  = l2.val if l2 else 0
            carry, digit = divmod(val1 + val2 + carry, 10)
            
            
            # create the current digit
            current_digit = ListNode(digit)
            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None
            current_digit.next = recur(l1_next, l2_next, carry)
            return current_digit

        return recur(l1, l2, 0)





        