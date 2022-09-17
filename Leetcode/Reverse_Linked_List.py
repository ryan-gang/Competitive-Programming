from typing import Optional
from StarterCode.Linked_List_Utils import ListNode


class Solution:
    # Runtime: 82 ms, faster than 6.32% of Python3 online submissions.
    # Memory Usage: 15.5 MB, less than 56.30% of Python3 online submissions.
    def reverseListClean(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, None
        next = head
        while next:
            curr = next
            next = next.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
