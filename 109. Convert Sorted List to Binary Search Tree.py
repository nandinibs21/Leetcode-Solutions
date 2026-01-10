# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        # Step 1: get length of the linked list
        def get_length(node: 'ListNode') -> int:
            n = 0
            while node:
                n += 1
                node = node.next
            return n

        n = get_length(head)
        self.curr = head  # pointer that advances in inorder construction

        # Step 2: inorder build of BST from list segment size "size"
        def build(size: int) -> 'TreeNode':
            if size <= 0:
                return None

            # left subtree
            left = build(size // 2)

            # root from current list node
            root = TreeNode(self.curr.val)
            root.left = left
            self.curr = self.curr.next  # advance list pointer

            # right subtree
            root.right = build(size - (size // 2) - 1)

            return root

        return build(n)
