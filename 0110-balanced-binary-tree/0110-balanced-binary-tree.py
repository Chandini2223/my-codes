class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function returns (isBalanced, height)
        def check(node):
            if not node:
                return True, 0
            
            left_balanced, left_height = check(node.left)
            right_balanced, right_height = check(node.right)
            
            # Node is balanced if left and right subtrees are balanced
            # and their heights differ by at most 1
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            
            return balanced, height
        
        result, _ = check(root)
        return result
