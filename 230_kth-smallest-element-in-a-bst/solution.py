from typing import Optional

import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def heapify(root: Optional[TreeNode]):
        if root is None:
            return

        min_node = None

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return

            if min_node is None or node.val < min_node.val:
                min_node = node

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        assert min_node is not None
        tmp = root.val
        root.val = min_node.val
        min_node.val = tmp


    def swap(node1: TreeNode, node2: TreeNode):
        node1.val, node2.val = node2.val, node1.val


    def heapify_down(root: Optional[TreeNode]):
        left_child_value = root.left.val if root.left is not None else math.inf
        right_child_value = root.right.val if root.right is not None else math.inf

        if root.val < left_child_value and left_child_value <= right_child_value:
            Solution.swap(root, root.left)
            Solution.heapify_down(root.left)
            return

        if root.val < right_child_value and right_child_value <= left_child_value:
            Solution.swap(root, root.right)
            Solution.heapify_down(root.right)
            return
        
        assert root >= left_child_value and root >= right_child_value


    def heappop(root: Optional[TreeNode]) -> int:
        assert root is not None

        

        
        

        


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
