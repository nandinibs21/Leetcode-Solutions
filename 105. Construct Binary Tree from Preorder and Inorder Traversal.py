# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        idx = {v: i for i, v in enumerate(inorder)}
        self.pre_i = 0

        def build(in_left, in_right):
            # build subtree from inorder[in_left : in_right+1]
            if in_left > in_right:
                return None

            root_val = preorder[self.pre_i]
            self.pre_i += 1
            root = TreeNode(root_val)

            mid = idx[root_val]  # root position in inorder

            root.left = build(in_left, mid - 1)
            root.right = build(mid + 1, in_right)
            return root

        return build(0, len(inorder) - 1)
