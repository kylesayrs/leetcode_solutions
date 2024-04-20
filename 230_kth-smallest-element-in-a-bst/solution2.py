from typing import Optional

import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            
            heap.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        heapq.heapify(heap)

        assert k > 0
        for _ in range(k):
            result = heapq.heappop(heap)

        return result
