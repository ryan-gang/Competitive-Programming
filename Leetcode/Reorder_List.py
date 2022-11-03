from typing import Optional

from StarterCode.Linked_List_Utils import ListNode, arrayToListNode, prettyPrintLinkedList


class Solution:
    """
    1. Find middle of the linked list.
    2. Reverse the 2nd half of the linked list.
    3. Interleave both the lists, into 1.
    """

    # Ref : leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained
    # Runtime: 194 ms, faster than 47.88% of Python3 online submissions.
    # Memory Usage: 23.9 MB, less than 64.60% of Python3 online submissions.
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = Solution.find_middle_of_list(head)
        next = mid.next
        mid.next = None
        head2 = Solution.reverse_list(next)
        head1 = head
        while head1 and head2:
            head1next = head1.next
            head2next = head2.next
            head1.next = head2
            head2.next = head1next

            head1 = head1next
            head2 = head2next

        self.head = head

    @staticmethod
    def find_middle_of_list(head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = curr = None
        next = head
        while next:
            curr = next
            next = next.next
            curr.next = prev
            prev = curr
        return prev


if __name__ == "__main__":
    sol = Solution()
    array = [1, 2, 3, 4, 5]
    head = arrayToListNode(array)
    prettyPrintLinkedList(head)
    sol.reorderList(head)
    prettyPrintLinkedList(sol.head)
