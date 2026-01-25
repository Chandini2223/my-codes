# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        current = root
        while current:
            if current.left:
                # Find the rightmost node of the left subtree
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                # Connect it to current's right subtree
                predecessor.right = current.right
                # Move left subtree to the right
                current.right = current.left
                current.left = None
            # Move to the next node
            current = current.right
