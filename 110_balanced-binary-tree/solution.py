from typing import Optional

import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mark_height(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        node.height = max(
            Solution.mark_height(node.left),
            Solution.mark_height(node.right),
        ) + 1

        return node.height
    

    def is_balanced_helper(node: Optional[TreeNode]):
        if node is None:
            return True
        
        left_height = node.left.height if node.left is not None else 0
        right_height = node.right.height if node.right is not None else 0

        if abs(right_height - left_height) >= 2:
            return False
        
        return (
            Solution.is_balanced_helper(node.left) and
            Solution.is_balanced_helper(node.right)
        )
    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        Solution.mark_height(root)

        return Solution.is_balanced_helper(root)
