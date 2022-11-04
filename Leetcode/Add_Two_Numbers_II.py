from typing import Optional, Tuple
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList, ListNode


class Solution:
    """
    Logic is same as in CTCI.
    First 0 pad the smaller list, so as to make them same length.
    From : [1], [9 -> 9 -> 9]
    To : [0 -> 0 -> 1], [9 -> 9 -> 9]
    Now, we write a recursive method, that takes in nodes at each "level" finds out the sum,
    with the carry from the next call, creates a new node, and sets the next call's return to
    this node's next.
    Each call returns the carry, and the node with the value set to the add.
    The node is also carefully crafted, so as this node is the head upto this point.
    All the subsequent calls are already present in this list.
    """

    # Runtime: 124 ms, faster than 72.33% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 11.61% of Python3 online submissions.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = Solution.length(l1), Solution.length(l2)
        if c1 > c2:
            l2 = Solution.pad_zeros_to_front(l2, c1 - c2)
        else:
            l1 = Solution.pad_zeros_to_front(l1, c2 - c1)

        carry, node = Solution.recurse(l1, l2)
        if carry > 0:
            head = ListNode(carry)
            head.next = node
        else:
            head = node
        return head

    @staticmethod
    def recurse(
        node1: Optional[ListNode], node2: Optional[ListNode]
    ) -> Tuple[int, Optional[ListNode]]:
        if node1 is None and node2 is None:
            return 0, None

        carry, tail = Solution.recurse(node1.next, node2.next)
        carry, add = divmod(node1.val + node2.val + carry, 10)

        node = ListNode(add)
        node.next = tail

        return carry, node

    @staticmethod
    def length(head: Optional[ListNode]) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    @staticmethod
    def pad_zeros_to_front(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = node = ListNode(0)
        for i in range(n):
            tmp = ListNode(0)
            node.next = tmp
            node = node.next

        node.next = head
        return new_head.next


if __name__ == "__main__":
    sol = Solution()
    l1, l2 = [9, 9, 9, 9, 9, 9, 9], [1]
    # l1, l2 = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9]
    # l1, l2 = [2, 4, 3], [5, 6, 4]
    # l1, l2 = [0], [0]
    h1, h2 = arrayToListNode(l1), arrayToListNode(l2)
    prettyPrintLinkedList(sol.addTwoNumbers(h1, h2))
