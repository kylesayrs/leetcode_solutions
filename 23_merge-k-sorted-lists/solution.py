from typing import List, Optional

import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda a, b: a.val < b.val

        heads = []
        for head in lists:
            if head is not None:
                heapq.heappush(heads, head)
        
        merged_head = None
        merged_tail = None
        while len(heads) > 0:
            min_node = heapq.heappop(heads)
            #print(min_node.val)

            # add min_node to merged
            if merged_head is None:
                merged_head = ListNode(min_node.val)
                merged_tail = merged_head
            else:
                merged_tail.next = ListNode(min_node.val)
                merged_tail = merged_tail.next

            # add min_node.next if not None
            if min_node.next is not None:
                heapq.heappush(heads, min_node.next)

        return merged_head


if __name__ == "__main__":
    a = Solution().mergeKLists([
        ListNode(1, ListNode(5, ListNode(6))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ])

    while a is not None:
        print(a.val)
        a = a.next
    
