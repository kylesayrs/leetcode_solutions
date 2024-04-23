from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)

            nodes.append(node.val)

        dfs(root)
        return nodes
