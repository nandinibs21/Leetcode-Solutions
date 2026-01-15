# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: 'TreeNode') -> None:
        """
        Do not return anything, modify root in-place instead.
        Time: O(n), Space: O(1) extra
        """
        cur = root
        while cur:
            if cur.left:
                # Find rightmost node of left subtree
                pred = cur.left
                while pred.right:
                    pred = pred.right

                # Rewire pointers
                pred.right = cur.right
                cur.right = cur.left
                cur.left = None

            cur = cur.right
