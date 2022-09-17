from typing import Optional
from StarterCode.Linked_List_Utils import ListNode
from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prettyPrintLinkedList(head)
        fast = slow = head
        while fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return head


sol = Solution()
array = [1, 2, 2, 1]

head = arrayToListNode(array)
print(sol.isPalindrome(head))


# Submitted : Copied from Stephan.
# def isPalindrome(self, head):
#     rev = None
#     slow = fast = head
#     while fast and fast.next:
#         fast = fast.next.next
#         rev, rev.next, slow = slow, rev, slow.next
#     if fast:
#         slow = slow.next
#     while rev and rev.val == slow.val:
#         slow = slow.next
#         rev = rev.next
#     return not rev
