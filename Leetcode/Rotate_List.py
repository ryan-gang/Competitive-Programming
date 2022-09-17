# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 58 ms, faster than 34.46% of Python3 online submissions.
# Memory Usage: 13.9 MB, less than 31.89% of Python3 online submissions.
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = test = head
        # Calculate the length of the linked list, n = len(linked list).
        n = 1
        while test and test.next:
            test = test.next
            n += 1
        # if k > n, then k can be taken as k modulo n.
        k = k % n
        _ = k
        # Move the fast pointer to the Kth node.
        while _ > 0:
            fast = fast.next
            _ -= 1
        # Move the fast pointer to the Nth node, and slow pointer to (K-N)th node
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # The slow pointer will be the last node in our rotated list.
        # So the next of slow will be None, to signify END.
        # But the node next to the slow pointer here, will be our new head.
        # And our fast pointer needs to be joined to our current head.
        if fast and slow:
            fast.next = head
            out = slow.next
            slow.next = None
            return out
        else:
            return head
