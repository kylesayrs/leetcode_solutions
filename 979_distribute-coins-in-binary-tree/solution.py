from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distribute_child(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        if node.val > 0:
            return node.val - 1
        
        elif node.val < 0:
            return abs(node.val) + 1
        
        else:
            return 1

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_subtree = self.distributeCoins(root.left)
        right_subtree = self.distributeCoins(root.right)

        left_distribute = self.distribute_child(root.left)
        right_distribute = self.distribute_child(root.right)

        left_val = root.left.val - 1 if root.left is not None else 0
        right_val = root.right.val - 1 if root.right is not None else 0

        root.val = root.val + left_val + right_val

        return left_subtree + right_subtree + left_distribute + right_distribute
