class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        curr = root  # Start with the root
        
        while curr:
            # Dummy node to start the next level's linked list
            dummy = Node(0)
            tail = dummy
            
            # Traverse the current level using .next pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                # Move to the next node in the current level
                curr = curr.next
            
            # Move curr to the start of the level we just finished building
            curr = dummy.next
            
        return root