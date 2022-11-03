from typing import Optional
from StarterCode.Linked_List_Utils import ListNode, arrayToListNode, prettyPrintLinkedList


class Solution:
    """
    If len = 0, initial value of prev (None) is returned. Expected.
    If len = 1, loop runs for 1 iteration. curr.next is set to None.
    And next iteration loop exits. As expected.
    Much cleaner code.
    """

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

    """
    Explicitly handling len = 0 and len = 1 cases.
    Can be handled more gracefully by the above method.
    """
    # Runtime: 90 ms, faster than 5.46% of Python3 online submissions.
    # Memory Usage: 15.4 MB, less than 55.32% of Python3 online submissions.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node = None, head
        if not node or not node.next:
            return head
        while node:
            next = node.next
            node.next = prev
            prev, node = node, next

        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
            # Easier to understand :
            # cur.next = prev
            # prev, cur = cur, cur.next
        return prev


if __name__ == "__main__":
    sol = Solution()
    # array = []
    # array = [1]
    # array = [1, 2]
    # array = [1, 2, 3]
    # array = [1, 2, 3, 4]
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ll_head = arrayToListNode(array)
    prettyPrintLinkedList(ll_head)
    prettyPrintLinkedList(sol.reverseList(ll_head))
