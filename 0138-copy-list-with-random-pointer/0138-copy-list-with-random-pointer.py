class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Insert cloned nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the lists
        curr = head
        copy_head = head.next
        copy = copy_head

        while curr:
            curr.next = curr.next.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
            copy = copy.next

        return copy_head
