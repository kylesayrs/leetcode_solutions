from collections import deque

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
        array = []

        queue = deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            
            if node is None:
                array.append("null")
            else:
                array.append(str(node.val))

                queue.append(node.left)
                queue.append(node.right)

        return "[" + ",".join(array) + "]"
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        array = data[1:-1].split(",")
        if len(array) <= 0 or array[0] == "null":
            return None
        
        array_queue = deque(array)
        parent_queue = deque()
        
        root = TreeNode(array_queue.popleft())
        parent_queue.append((root, True))
        parent_queue.append((root, False))

        while len(parent_queue) > 0:
            parent, is_left = parent_queue.popleft() 
            if parent is None:
                continue

            value = array_queue.popleft()
            
            if is_left:
                parent.left = TreeNode(value) if value != "null" else None
                parent_queue.append((parent.left, True))
                parent_queue.append((parent.left, False))
            
            else:
                parent.right = TreeNode(value) if value != "null" else None
                parent_queue.append((parent.right, True))
                parent_queue.append((parent.right, False))

        return root
        

        

# Your Codec object will be instantiated and called as such:
root = TreeNode(1,
    None,
    TreeNode(2,
        TreeNode(3),         
        TreeNode(4),         
    )
)

ser = Codec()
deser = Codec()
ans = ser.serialize(deser.deserialize(ser.serialize(root)))
