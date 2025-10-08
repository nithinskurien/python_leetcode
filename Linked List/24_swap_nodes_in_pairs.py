# 24. Swap Nodes in Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without
# modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4]
#
# Output: [2,1,4,3]
#
# Explanation:
#
#
#
# Example 2:
#
# Input: head = []
#
# Output: []
#
# Example 3:
#
# Input: head = [1]
#
# Output: [1]
#
# Example 4:
#
# Input: head = [1,2,3]
#
# Output: [2,1,3]
#
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        root = head.next
        prev = None
        curr = head
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            if prev:
                prev.next = temp
            prev = curr
            curr = curr.next

        return root
