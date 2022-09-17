from typing import Optional
from StarterCode.Linked_List_Utils import ListNode
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList


# Runtime: 59 ms, faster than 63.19% of Python3 online submissions.
# Memory Usage: 14 MB, less than 30.17% of Python3 online submissions.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        pre, curr = sentinel, head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                pre.next = curr.next
            else:
                pre = pre.next

            curr = curr.next

        return sentinel.next


sol = Solution()
array = [1, 2, 3, 3, 3, 3, 4, 4, 5]
head = arrayToListNode(array)
prettyPrintLinkedList(sol.deleteDuplicates(head))
