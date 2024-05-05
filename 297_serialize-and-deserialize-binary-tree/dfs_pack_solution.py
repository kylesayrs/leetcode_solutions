from typing import Optional, List, Tuple


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return None
        
        return (root.val, self.serialize(root.left), self.serialize(root.right))


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        
        node = TreeNode(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])

        return node


serialization = Codec().serialize(
    TreeNode(1, 
        TreeNode(2),
        TreeNode(3,
            TreeNode(4),
            TreeNode(5),
        ),
    )
)

print(serialization)


        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
