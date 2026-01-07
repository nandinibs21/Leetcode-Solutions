# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map value -> index in inorder for O(1) splits
        idx = {v: i for i, v in enumerate(inorder)}
        
        # We'll consume postorder from the end (root comes last in postorder)
        self.p = len(postorder) - 1

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            # build subtree using inorder boundaries [in_left, in_right]
            if in_left > in_right:
                return None

            root_val = postorder[self.p]
            self.p -= 1
            root = TreeNode(root_val)

            mid = idx[root_val]

            # IMPORTANT: build right first (because we are moving backward in postorder)
            root.right = helper(mid + 1, in_right)
            root.left = helper(in_left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
