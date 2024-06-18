from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        linked_list = []
        current = head
        while (current is not None):
            linked_list.append(current)
            current = current.next

        left = 0
        right = len(linked_list) - 1
        left_to_right = True
        while (left < right):  # TODO: check
            if (left_to_right):
                linked_list[left].next = linked_list[right]
                left += 1
                left_to_right = not left_to_right


            else:
                linked_list[right].next = linked_list[left]
                right -= 1
                left_to_right = not left_to_right

        #assert left == right
        if len(linked_list) > 0:
            linked_list[left].next = None
