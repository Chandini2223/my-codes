class Solution:
    def sortedListToBST(self, head: 'Optional[ListNode]') -> 'Optional[TreeNode]':
        # Step 1: Convert linked list to array for easy access
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        # Step 2: Recursive function to build BST
        def buildBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root
        
        return buildBST(0, len(nums) - 1)
