from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer, fast_pointer, prev_pointer = head, head, None
        if slow_pointer.next is None:
            return None
        while fast_pointer and fast_pointer.next is not None:
            prev_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        prev_pointer.next = prev_pointer.next.next
        return head
