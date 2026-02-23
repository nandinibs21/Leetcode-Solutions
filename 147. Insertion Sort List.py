class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # Sorted list dummy head
        current = head
        
        while current:
            prev = dummy
            next_node = current.next
            
            # Find insertion position
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current
            
            # Move to next node
            current = next_node
        
        return dummy.next
