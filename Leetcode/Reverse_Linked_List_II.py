from typing import Optional
from Leetcode.StarterCode.Linked_List import ListNode


class Solution:
    """
    Linked list : A -> B -> C -> D, and we need to reverse the list between B, C.
    Get node just before B. Get node just after C.
    Reverse B to C.
    Add proper pointers. A -> B' and C' -> D.
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        rev_head_prev = self.getNthNode(head, left - 1)
        rev_head = self.getNthNode(head, left)
        rev_tail = self.getNthNode(head, right)
        overall_tail = self.getNthNode(head, right + 1)

        rev_tail.next = None
        rev_head = self.reverseLinkedList(rev_head)
        rev_tail = self.getNthNode(rev_head, right - left + 1)
        rev_tail.next = overall_tail

        if rev_head_prev is not None:
            rev_head_prev.next = rev_head
            return head
        else:
            return rev_head

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def getNthNode(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n < 1:
            return None
        while head and n > 1:
            head = head.next
            n -= 1
        return head

    def printNode(self, node: Optional[ListNode]) -> None:
        if node is None:
            print("None")
        else:
            print(node.val)
