from typing import Optional
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Runtime: 24 ms, faster than 99.35% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 55.55% of Python3 online submissions.
    # T : O(N), S : O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            fast = fast.next
            slow = slow.next

        return slow

    """
    Each time, slow go 1 steps while fast go 2 steps.
    When fast arrives at the end, slow will arrive right in the middle. No need to think about
    fast always being valid, let it be None. Slow is anyway behind,
    it will come to the appropriate position."""

    def middleNodeOptimsedCode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


sol = Solution()
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array = [1]
head = arrayToListNode(array)
prettyPrintLinkedList(head)
prettyPrintLinkedList(sol.middleNode(head))
