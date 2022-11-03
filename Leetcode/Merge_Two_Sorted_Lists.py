from typing import Optional
from StarterCode.Linked_List_Utils import ListNode
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList


class Solution:
    # Runtime: 63 ms, faster than 40.46% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 32.84% of Python3 online submissions.
    def mergeTwoLists(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        prettyPrintLinkedList(head1)
        prettyPrintLinkedList(head2)
        if not head1:
            return head2
        if not head2:
            return head1

        curr1, curr2 = head1, head2
        if head1.val <= head2.val:
            head = head1
            curr1 = curr1.next
        else:
            head = head2
            curr2 = curr2.next

        curr = head
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        if curr1:
            curr.next = curr1
        elif curr2:
            curr.next = curr2

        prettyPrintLinkedList(head)
        return head

    # Runtime: 65 ms, faster than 44.83% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 32.73% of Python3 online submissions.
    # While both lists are still present, check for lower value, add to prev.next.
    # Increment prev and the list node.
    # Finally the list that remains, add the whole thing to the end of the sorted list.
    def merge_two_lists_clean(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node = head = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next

        # if head1 or head2:  # This condition is not required.
        node.next = head1 or head2

        return head.next


sol = Solution()
array1, array2 = [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]
array1, array2 = [1, 2, 3], [0, 3, 5]
array1, array2 = [], []
array1, array2 = [], [0]

h1 = arrayToListNode(array1)
h2 = arrayToListNode(array2)
print("Out list : ", prettyPrintLinkedList(sol.mergeTwoLists(h1, h2)))
