class Solution:
    def partition(self, head, x):
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less_tail = less_head
        greater_tail = greater_head
        
        current = head
        
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next
        
        # End the greater list
        greater_tail.next = None
        
        # Connect partitions
        less_tail.next = greater_head.next
        
        return less_head.next
