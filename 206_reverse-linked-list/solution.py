from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = None
        
        while head is not None:
            if reversed_head is None:
                reversed_head = ListNode(head.val, None)

            else:
                reversed_head = ListNode(head.val, reversed_head)
            
            head = head.next

        return reversed_head
