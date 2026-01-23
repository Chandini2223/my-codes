class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # The last element in postorder is the root
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Find the index of root in inorder
        idx = inorder.index(root_val)

        # Build left and right subtrees
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

        return root
