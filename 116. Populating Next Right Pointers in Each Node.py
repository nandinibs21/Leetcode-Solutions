# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        level_start = root  # leftmost node of current level

        # since it's a perfect binary tree, check left child to move levels
        while level_start.left:
            cur = level_start

            # traverse nodes in the current level using next pointers
            while cur:
                # connect left -> right
                cur.left.next = cur.right

                # connect right -> next parent's left
                if cur.next:
                    cur.right.next = cur.next.left

                cur = cur.next

            level_start = level_start.left  # move to next level

        return root
