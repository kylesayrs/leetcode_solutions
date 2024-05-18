from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        total_moves = 0

        def get_excess(node: Optional[TreeNode]) -> int:
            nonlocal total_moves

            if node is None:
                return 0
            
            left_excess = get_excess(node.left)
            right_excess = get_excess(node.right)

            total_moves += abs(left_excess)
            total_moves += abs(right_excess)

            return node.val + left_excess + right_excess - 1

        assert get_excess(root) == 0
        return total_moves


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(), TreeNode())
    Solution().distributeCoins(root)
