class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # If leaf node, check if remaining targetSum equals node's value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recur for left and right subtree with updated targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
