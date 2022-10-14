from typing import Optional
from StarterCode.Linked_List import ListNode


class Solution:
    # Runtime: 5163 ms, faster than 5.02% of Python3 online submissions.
    # Memory Usage: 60.7 MB, less than 11.84% of Python3 online submissions.
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = prev = head
        # Special case of a list with 1 node, have to return None.
        if not head.next:
            return head.next  # None
        # As long as fast can move 2 steps forward, run the loop.
        # But it can step on the end None node too, so the first check.
        while fast is not None and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Instead of using the prev pointer, we can start the fast node, one iteration ahead,
        # so that slow is one iteration behind, so it will be at prev is now.
        # We can do slow.next = slow.next.next
        prev.next = slow.next
        return head

    def deleteMiddleEditorial(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: return None if there is only one node.
        if head.next == None:
            return None

        # Initialize two pointers, 'slow' and 'fast'.
        slow, fast = head, head.next.next

        # Let 'fast' move forward by 2 nodes, 'slow' move forward by 1 node each step.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When 'fast' reaches the end, remove the next node of 'slow' and return 'head'.
        slow.next = slow.next.next

        # The job is done, return 'head'.
        return head
