# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
# Follow up: Could you do this in one pass?

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currNode = head
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reverseNode = self.reverseList(head)
        prevNode = None
        deleteNode = reverseNode
        while n > 1:
            nextNode = deleteNode.next
            prevNode = deleteNode
            deleteNode = nextNode
            n -= 1
        if deleteNode is None:
            return None
        if prevNode is None:
            return self.reverseList(deleteNode.next)
        nextNode = deleteNode.next
        prevNode.next = nextNode
        deleteNode.next = None
        return self.reverseList(reverseNode)


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
    print(Solution().removeNthFromEnd(node1, 2))
