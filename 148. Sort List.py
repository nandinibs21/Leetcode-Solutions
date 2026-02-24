class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # Get length of list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        dummy = ListNode(0)
        dummy.next = head
        size = 1
        
        while size < length:
            prev = dummy
            curr = dummy.next
            
            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)
                
                merged = self.merge(left, right)
                prev.next = merged
                
                while prev.next:
                    prev = prev.next
            
            size *= 2
        
        return dummy.next
    
    def split(self, head, size):
        for i in range(size - 1):
            if head:
                head = head.next
            else:
                break
        
        if not head:
            return None
        
        second = head.next
        head.next = None
        return second
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        return dummy.next
