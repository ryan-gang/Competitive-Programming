from typing import Optional
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList, ListNode


class Solution:
    # Runtime: 44 ms, faster than 75.06% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 75.71% of Python3 online submissions.
    # T : O(N), S : O(1)
    # Algo takes only a single pass over Linked list.
    def partitionMessy(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
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

    """
    Just create 2 new lists one with all values less than x,
    and the other with all values greater than x.
    Finally join both. And set end to None.
    """
    # Runtime: 59 ms, faster than 69.06% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 30.14% of Python3 online submissions.
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = b = ListNode(0)
        after = a = ListNode(0)
        curr = head

        while curr:
            if curr.val < x:
                b.next = curr
                b = b.next
            else:
                a.next = curr
                a = a.next
            curr = curr.next

        a.next = None
        b.next = after.next
        return before.next


if __name__ == "__main__":
    sol = Solution()
    array = [1, 2, 2, 4, 6, 3, 2, 1, 5, 2]
    # array = [1, 4, 3, 2, 5, 2]
    # array = [2, 1]
    # array = [1, 2, 3]
    # array = []

    head = arrayToListNode(array)
    prettyPrintLinkedList(head)
    prettyPrintLinkedList(sol.partition(head, x=3))
