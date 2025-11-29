class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            # Reach the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the node
            curr = stack.pop()
            res.append(curr.val)
            
            # Explore the right subtree
            curr = curr.right
        
        return res
