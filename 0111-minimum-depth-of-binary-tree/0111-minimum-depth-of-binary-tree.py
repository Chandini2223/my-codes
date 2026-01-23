class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If one of the children is None, we must go through the other
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both children exist, take the minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
