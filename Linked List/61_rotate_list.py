# 61. Rotate List
#
# Given the head of a linked list, rotate the list to the right by k places.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109
#
# Logic:
# We can first iterate over the linked list to find the tail and length of the list. We can then find the k such that
# it is within the size of the list by taking k % length. We can iterate over the list till we reach the length - k - 1
# element. This will be the new head. We can then assign the tail's next value to be the original head, the next of the
# break to be None, return the new head.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return head
        first = head
        for index in range(length - k - 1):
            first = first.next
        new_head = first.next
        first.next = None
        tail.next = head
        return new_head


if __name__ == "__main__":
    list1 = ListNode(1)
    list2 = ListNode(2)
    list3 = ListNode(3)
    list4 = ListNode(4)
    list5 = ListNode(5)
    list1.next = list2
    list2.next = list3
    list3.next = list4
    list4.next = list5
    print(Solution().rotateRight(list1, 2))
