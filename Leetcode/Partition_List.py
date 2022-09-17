from typing import Optional
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList, ListNode


class Solution:
    # Runtime: 44 ms, faster than 75.06% of Python3 online submissions for Partition List.
    # Memory Usage: 13.9 MB, less than 75.71% of Python3 online submissions for Partition List.
    # T : O(N), S : O(1)
    # Algo takes only a single pass over Linked list.
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        first_half_head, second_half_head = None, None
        first_half_curr, second_half_curr = None, None
        curr = head
        while curr:
            if curr.val < x:
                if not first_half_head:
                    first_half_head = curr
                    first_half_curr = curr
                else:
                    first_half_curr.next = curr
                    first_half_curr = curr
            else:
                if not second_half_head:
                    second_half_head = curr
                    second_half_curr = curr
                else:
                    second_half_curr.next = curr
                    second_half_curr = curr

            curr = curr.next

        if second_half_curr:
            second_half_curr.next = None

        if first_half_head:
            first_half_curr.next = second_half_head
        else:
            first_half_head = second_half_head

        return first_half_head


head = arrayToListNode([1, 2, 2, 4, 6, 3, 2, 1, 5, 2])
prettyPrintLinkedList(head)
sol = Solution()
first_half_head = sol.partition(head, x=3)
# first_half_head = sol.partition(arrayToListNode([1, 4, 3, 2, 5, 2]), x=3)
# first_half_head = sol.partition(arrayToListNode([2, 1]), x=2)
# first_half_head = sol.partition(arrayToListNode([1, 2, 3]), x=4)
prettyPrintLinkedList(first_half_head)
