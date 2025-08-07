# 21. Merge Two Sorted Lists
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
#
# Return the head of the merged linked list.
#
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
#
# Logic: Create a new linked list with a dummy head and append nodes to the list based on looking at the 2 lists and
# seeing which of the values are smaller


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headNode = ListNode(None)
        currNode = headNode
        while list1 or list2:
            if list1 is None:
                currNode.next = list2
                return headNode.next
            if list2 is None:
                currNode.next = list1
                return headNode.next
            if list1.val < list2.val:
                currNode.next = list1
                list1 = list1.next
            else:
                currNode.next = list2
                list2 = list2.next
            currNode = currNode.next
        return headNode.next


if __name__ == "__main__":
    node1 = ListNode(1, None)
    node2 = ListNode(2, None)
    node3 = ListNode(4, None)

    node4 = ListNode(1, None)
    node5 = ListNode(3, None)
    node6 = ListNode(4, None)
    node1.next = node2
    node2.next = node3

    node4.next = node5
    node5.next = node6
    print(Solution().mergeTwoLists(node1, node4))
