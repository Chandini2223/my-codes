class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)  # Use the TreeNode given by LeetCode

        idx = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])

        return root
