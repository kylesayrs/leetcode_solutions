from typing import Optional, List

import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # mark first critical point
        # mark prev critical point
        # mark last critical point

        first_critical_point = None
        prev_critical_point = None
        curr_critical_point = None

        min_distance = math.inf
        max_distance = None

        # critical point variables
        prev_rising = None
        index = 0
        current = head
        # assert head is not None
        while current.next is not None:
            curr_rising = (
                True if current.next.val > current.val else
                False if current.next.val < current.val else
                None
            )
            if (
                (curr_rising == True and prev_rising == False) or
                (curr_rising == False and prev_rising == True)
            ):
                curr_critical_point = index
                if first_critical_point is None:
                    first_critical_point = curr_critical_point

                if prev_critical_point is not None:
                    min_distance = min(
                        min_distance, curr_critical_point - prev_critical_point
                    )

                prev_critical_point = curr_critical_point

            index += 1
            current = current.next
            prev_rising = curr_rising

        # accounts for cases where there are no critical points
        # and one critical point
        if curr_critical_point != first_critical_point:
            max_distance = curr_critical_point - first_critical_point
            return [min_distance, max_distance]

        else:
            return [-1, -1]
