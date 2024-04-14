from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        head = None
    
        while not (list1 is None and list2 is None):
            if list1 is None:
                new_value = list2.val
                list2 = list2.next

            elif list2 is None:
                new_value = list1.val
                list1 = list1.next

            elif list1.val <= list2.val:
                new_value = list1.val
                list1 = list1.next

            else:
                new_value = list2.val
                list2 = list2.next

            if tail is None:
                tail = ListNode(new_value)
                head = tail

            else:
                tail.next = ListNode(new_value)
                tail = tail.next
        
        return head
