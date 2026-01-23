class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> 'TreeNode':  # Use the LeetCode TreeNode
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])  # Use LeetCode's TreeNode
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
