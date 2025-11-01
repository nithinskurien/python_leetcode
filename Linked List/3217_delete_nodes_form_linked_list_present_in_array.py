# 3217. Delete Nodes From Linked List Present in Array
#
# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list
# after removing all nodes from the linked list that have a value that exists in nums.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3], head = [1,2,3,4,5]
#
# Output: [4,5]
#
# Explanation:
#
#
#
# Remove the nodes with values 1, 2, and 3.
#
# Example 2:
#
# Input: nums = [1], head = [1,2,1,2,1,2]
#
# Output: [2,2,2]
#
# Explanation:
#
#
#
# Remove the nodes with value 1.
#
# Example 3:
#
# Input: nums = [5], head = [1,2,3,4]
#
# Output: [1,2,3,4]
#
# Explanation:
#
#
#
# No node has value 5.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# All elements in nums are unique.
# The number of nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105
# The input is generated such that there is at least one node in the linked list that has a value not present in nums.
#
# Logic:
# We can save the array into a set to do O(1) lookup. We can then initialise a dummy ListNode with the next node in
# dummy pointing to the head. We can then have 2 variables prev, curr with dummy and head as the initial values. We can
# then iterate over the list such that when the curr node has a value in the set we can set the prev node next as the
# next of the curr node. We can move to the next node and so on. We can return the next of the dummy node.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val in num_set:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next
