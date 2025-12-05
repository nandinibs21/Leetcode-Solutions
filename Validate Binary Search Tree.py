class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            
            # Current node's value must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # Left subtree: values < node.val
            # Right subtree: values > node.val
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float("-inf"), float("inf"))
