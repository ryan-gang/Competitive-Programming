from typing import Optional
from StarterCode.Linked_List_Utils import ListNode


"""
Hare and tortoise algo.
fast node moves two nodes at a time, slow node moves one node at a time.
If there is a loop present, at some point, they are bound to meet.
When that happens, return True.
Or if linked list ends, return False."""


class Solution:
    # Runtime: 123 ms, faster than 15.55% of Python3 online submissions.
    # Memory Usage: 17.6 MB, less than 30.66% of Python3 online submissions.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
