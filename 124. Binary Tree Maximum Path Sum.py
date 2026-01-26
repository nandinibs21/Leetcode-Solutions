# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Best path that "passes through" this node (can take both sides)
            through = node.val + left_gain + right_gain
            self.best = max(self.best, through)

            # Return best downward path starting at this node (choose one side)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.best
