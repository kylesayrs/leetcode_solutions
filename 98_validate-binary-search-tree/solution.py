from typing import Optional

import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(node: Optional[TreeNode], _min: int, _max: int):
        if node is None:
            return True
        
        if node.val <= _min or node.val >= _max:
            return False
        
        if node.left is not None and node.left.val >= node.val:
            return False
        
        if node.right is not None and node.right.val <= node.val:
            return False

        return (
            Solution.dfs(node.left, _min, min(node.val, _max)) and
            Solution.dfs(node.right, max(node.val, _min), _max)
        )


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution.dfs(root, -math.inf, math.inf)


if __name__ == "__main__":
    assert Solution().isValidBST(
        TreeNode(1,
            None,
            TreeNode(3,
                TreeNode(2),
                None
            )
        )
    ) == True

    assert Solution().isValidBST(
        TreeNode(1,
            None,
            TreeNode(3,
                TreeNode(-10),
                None
            )
        )
    ) == False
