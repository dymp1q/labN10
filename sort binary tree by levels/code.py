
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                nxt = root.right
                while nxt.left is not None:
                    nxt = nxt.left
                                            
                root.val = nxt.val
                root.right = self.deleteNode(root.right, nxt.val)
            return root
