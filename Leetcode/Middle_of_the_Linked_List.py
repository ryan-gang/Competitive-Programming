from typing import Optional
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Runtime: 38 ms, faster than 78.73% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 11.16% of Python3 online submissions.
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

    def middleNodeOptimsedCode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


sol = Solution()
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# array = [1]
head = arrayToListNode(array)
prettyPrintLinkedList(head)
prettyPrintLinkedList(sol.middleNode(head))
