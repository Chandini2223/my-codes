class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        leftmost = root
        
        # While there is a level below to connect
        while leftmost.left:
            head = leftmost
            while head:
                # Connection 1: Left child to Right child
                head.left.next = head.right
                
                # Connection 2: Right child to the next parent's Left child
                if head.next:
                    head.right.next = head.next.left
                
                # Move sideways through the "linked list" of the current level
                head = head.next
            
            # Move down to the next level
            leftmost = leftmost.left
            
        return root
        