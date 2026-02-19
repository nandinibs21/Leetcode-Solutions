# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1) Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half
        prev = None
        curr = slow.next
        slow.next = None  # cut
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev  # head of reversed half

        # 3) Merge alternating
        first = head
        while second:
            n1 = first.next
            n2 = second.next

            first.next = second
            second.next = n1

            first = n1
            second = n2
