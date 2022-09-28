from typing import Optional
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Runtime: 56 ms, faster than 40.71% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 98.06% of Python3 online submissions.
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            # Take fast node to the nth index.
            fast = fast.next
        if not fast:
            # If n == len(linked_list)
            # fast will come to the 'None' node after the last node.
            # If that is the case, we cam just return the head.next
            # Because if n == len(linked_list) we have to remove the head node itself.
            return slow.next
        while fast.next:
            # While fast reaches last index, slow will reach last - n index.
            # Because fast started n indices ahead.
            fast = fast.next
            slow = slow.next
        # Just bypass the required node.
        slow.next = slow.next.next

        return head

    """
    Exact same concept as the previous one.
    Take node, to n - 1 places ahead.
    Then while node is a valid, take both node and curr to next.
    Finally bypass the current required (curr) node, for that we use a prev node."""
    # Runtime: 56 ms, faster than 51.20% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 97.95% of Python3 online submissions.
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        while n > 1:
            node = node.next
            n -= 1

        prev, curr = None, head
        while node.next:
            node = node.next
            prev = curr
            curr = curr.next

        if prev is not None:
            # prev has come ahead by atleast 1 node. ie n != len(list)
            # Just bypass curr node.
            prev.next = curr.next
            return head
        else:
            # If prev is none, that means n == len(list), prev is still at the beginning dummy.
            # Just return head.next (Bypass head node)
            return head.next


sol = Solution()
array, n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2
# array, n = [1, 2, 3, 4, 5], 2
# array, n = [1], 1
# array, n = [1, 2], 1
# array, n = [1, 2], 2
head = arrayToListNode(array)
prettyPrintLinkedList(head)
prettyPrintLinkedList(sol.removeNthFromEnd(head, n))
