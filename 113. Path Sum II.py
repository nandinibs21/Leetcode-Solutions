# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def pathSum(self, root: Optional['TreeNode'], targetSum: int) -> List[List[int]]:
        res: List[List[int]] = []
        path: List[int] = []

        def dfs(node: Optional['TreeNode'], remaining: int) -> None:
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # If leaf node, check remaining
            if not node.left and not node.right:
                if remaining == 0:
                    res.append(path.copy())
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)

            # backtrack
            path.pop()

        dfs(root, targetSum)
        return res
