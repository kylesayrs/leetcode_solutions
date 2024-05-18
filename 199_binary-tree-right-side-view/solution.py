from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []

        def dfs(node: Optional[TreeNode], level: int):
            nonlocal view
            
            if node is None:
                return
            
            if len(view) <= level:
                assert len(view) == level
                view.append(node.val)
            
            else:
                view[level] = node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return view
