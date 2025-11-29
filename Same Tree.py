from collections import deque

class Solution:
    def isSameTree(self, p, q):
        queue = deque([(p, q)])
        
        while queue:
            n1, n2 = queue.popleft()
            
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        
        return True
