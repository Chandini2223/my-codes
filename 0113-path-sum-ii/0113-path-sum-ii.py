from typing import List, Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, remaining):
            if not node:
                return
            # Include current node in path
            path.append(node.val)
            
            # If leaf and sum matches, add to result
            if not node.left and not node.right and remaining == node.val:
                res.append(list(path))
            else:
                # Recur for left and right
                dfs(node.left, path, remaining - node.val)
                dfs(node.right, path, remaining - node.val)
            
            # Backtrack
            path.pop()
        
        dfs(root, [], targetSum)
        return res
