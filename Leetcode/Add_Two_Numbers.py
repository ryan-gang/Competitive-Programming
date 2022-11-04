from typing import Optional
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList, ListNode


class Solution:
    # Runtime: 139 ms, faster than 54.40% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 86.35% of Python3 online submissions.
    # T : O(N), S : O(N)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode(0)
        carry = 0
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            val = val1 + val2 + carry
            add, carry = val % 10, val // 10
            node.next = ListNode(add)
            node = node.next

        if carry:
            node.next = ListNode(carry)

        return head.next

    def addTwoNumbersCleaner(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = result_tail = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


if __name__ == "__main__":
    sol = Solution()
    l1, l2 = [2, 4, 3], [5, 6, 4]
    # l1, l2 = [0], [0]
    # l1, l2 = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]
    h1, h2 = arrayToListNode(l1), arrayToListNode(l2)
    prettyPrintLinkedList(sol.addTwoNumbers(h1, h2))
