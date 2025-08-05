# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000
#
# Logic:
# We need to traverse the list to find the middle point, once the middle point is found we need to separate the lists
# into two. We will need to reverse the second list and then swap the children between the 2 lists to complete the final
# list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = end = head
        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next
        head2 = mid.next
        mid.next = None

        prevNode = None
        currNode = head2
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

        head2 = prevNode
        currNode1 = head
        currNode2 = head2
        prevNode = None
        while currNode1 and currNode2:
            nextNode1 = currNode1.next
            nextNode2 = currNode2.next
            currNode1.next = currNode2
            currNode2.next = nextNode1
            currNode1 = nextNode1
            currNode2 = nextNode2
        test = prevNode


if __name__ == "__main__":
    node1 = ListNode(1, None)
    node2 = ListNode(2, None)
    node3 = ListNode(3, None)
    node4 = ListNode(4, None)
    node5 = ListNode(5, None)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(Solution().reorderList(node1))
