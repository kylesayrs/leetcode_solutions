from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return -1
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        self.diameter = max(self.diameter, left_height + right_height + 2)

        return max(left_height, right_height) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.get_height(root)

        return self.diameter
