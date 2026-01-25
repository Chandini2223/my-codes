class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with a very small number since node values can be negative
        self.max_sum = float('-inf')

        def get_gain(node):
            if not node:
                return 0

            # 1. Recursively get the max gain from left and right subtrees
            # If a gain is negative, we ignore it (take 0)
            left_gain = max(get_gain(node.left), 0)
            right_gain = max(get_gain(node.right), 0)

            # 2. Calculate the price of a path where this node is the highest point (the 'arch')
            current_path_sum = node.val + left_gain + right_gain

            # 3. Update the global maximum if this path is better
            self.max_sum = max(self.max_sum, current_path_sum)

            # 4. Return the max gain this node can offer to its parent
            # (Node value + only ONE of its children)
            return node.val + max(left_gain, right_gain)

        get_gain(root)
        return self.max_sum