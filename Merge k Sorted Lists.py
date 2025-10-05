from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        
        heap = []
        
        # Step 1: Add head of each list to heap
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        # Step 2: Pop smallest and push its next
        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
