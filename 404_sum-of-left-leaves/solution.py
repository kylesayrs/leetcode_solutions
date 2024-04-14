from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], left_child: bool):
            if node is None:
                return 0

            # is leaf
            if node.left is None and node.right is None:
                if left_child:
                    return node.val
                else:
                    return 0

            # recurse, marking left children
            return (
                dfs(node.left, True) +
                dfs(node.right, False)
            )

        return dfs(root, False)
