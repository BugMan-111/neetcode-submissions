# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list1, list2):
            dummy = ListNode(-1)
            curr = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2= list2.next
                curr = curr.next
            curr.next = list1 or list2
            return dummy.next

        while len(lists) > 1:
            # for every iter try to combine two lists
            curr_iter = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                curr_iter += [merge_two_lists(list1, list2)]
            lists = curr_iter

        return lists[0] if len(lists) > 0 else None
        

        