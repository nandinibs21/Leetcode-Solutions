# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # 1) Interleave copied nodes with originals: A->B becomes A->A'->B->B'...
        cur = head
        while cur:
            copy = Node(cur.val, cur.next, None)
            cur.next = copy
            cur = copy.next

        # 2) Assign random pointers for copies
        cur = head
        while cur:
            copy = cur.next
            copy.random = cur.random.next if cur.random else None
            cur = copy.next

        # 3) Detach the copied list from the interleaved list
        dummy = Node(0)
        copy_cur = dummy
        cur = head
        while cur:
            copy = cur.next
            nxt = copy.next

            copy_cur.next = copy
            copy_cur = copy

            cur.next = nxt
            cur = nxt

        return dummy.next
