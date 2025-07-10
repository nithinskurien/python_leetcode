from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pair_sum = 0
        twin_head = self.splitList(head)
        reversed_head = self.reverseList(twin_head)
        next_node, next_split_reversed_node = head, reversed_head
        if head.next is None:
            pair_sum = head.val + reversed_head.val
        while next_node is not None:
            pair_sum = max(pair_sum, next_node.val + next_split_reversed_node.val)
            next_node = next_node.next
            next_split_reversed_node = next_split_reversed_node.next
        return pair_sum

    def splitList(self, split: Optional[ListNode]) -> ListNode:
        slow_pointer = fast_pointer = prev_pointer = split
        while fast_pointer and fast_pointer.next is not None:
            prev_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        twin_head = prev_pointer.next
        prev_pointer.next = None
        return twin_head

    def reverseList(self, reverse: Optional[ListNode]) -> ListNode:
        curr_node, prev_node = reverse, None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node


if __name__ == "__main__":
    solution = Solution()
   # head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
   # head = ListNode(1, ListNode(1000))
    head = ListNode(7,
    ListNode(57,
        ListNode(13,
            ListNode(31,
                ListNode(17,
                    ListNode(65,
                        ListNode(32,
                            ListNode(3,
                                ListNode(97,
                                    ListNode(22,
                                        ListNode(7,
                                            ListNode(20,
                                                ListNode(69,
                                                    ListNode(35,
                                                        ListNode(69,
                                                            ListNode(75,
                                                                ListNode(13,
                                                                    ListNode(33,
                                                                        ListNode(50,
                                                                            ListNode(80,
                                                                                ListNode(64,
                                                                                    ListNode(71,
                                                                                        ListNode(15,
                                                                                            ListNode(28,
                                                                                                ListNode(2,
                                                                                                    ListNode(27,
                                                                                                        ListNode(39,
                                                                                                            ListNode(48,
                                                                                                                ListNode(13,
                                                                                                                    ListNode(22,
                                                                                                                        ListNode(84,
                                                                                                                            ListNode(5,
                                                                                                                                ListNode(51,
                                                                                                                                    ListNode(46,
                                                                                                                                        ListNode(26,
                                                                                                                                            ListNode(78,
                                                                                                                                                ListNode(56,
                                                                                                                                                    ListNode(63)
)))))))))))))))))))))))))))))))))))))

    print(solution.pairSum(head))