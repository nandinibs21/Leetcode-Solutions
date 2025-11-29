class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            # Detect duplicates by checking streak of equal values
            if curr.next and curr.val == curr.next.val:
                duplicate_value = curr.val
                
                # Skip all nodes with this duplicate value
                while curr and curr.val == duplicate_value:
                    curr = curr.next
                
                # Connect prev to the first non-duplicate node
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        
        return dummy.next
