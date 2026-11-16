# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            # merge two linked list 
            dummy = ListNode(-1)
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 is not None else l2
            return dummy.next

        # devide and conquer
        while len(lists) > 1:
            # merge the list two by two
            merged_list = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged_list += [merge(lists[i], lists[i + 1])]
                else:
                    merged_list += [lists[i]]
            lists = merged_list

        return lists[0] if len(lists) >= 1 else None
        