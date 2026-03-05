class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        res = []
        queue = [root]
        
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                
                if i == n - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res