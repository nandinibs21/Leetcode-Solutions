class Solution:
    def recoverTree(self, root):
        first = second = prev = None
        prev = TreeNode(float('-inf'))
        curr = root
        
        while curr:
            if not curr.left:
                # Check violation
                if curr.val < prev.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # Find predecessor
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                
                # Thread creation
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    # Thread removal
                    pred.right = None
                    if curr.val < prev.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right
        
        # Swap the incorrect nodes
        first.val, second.val = second.val, first.val
