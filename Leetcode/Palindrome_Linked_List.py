from collections import deque
from typing import Optional
from StarterCode.Linked_List import ListNode, arrayToListNode


class Solution:
    """
    Using hare and tortoise method, push the first half of the linked list into a stack.
    Then compare values with the next half of the list.
    Extra space used for the stack.
    """

    # Runtime: 1983 ms, faster than 31.28% of Python3 online submissions.
    # Memory Usage: 47 MB, less than 21.90% of Python3 online submissions.
    # T : O(N), S : O(N)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        stack: deque[int] = deque()
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast:  # If the lenght of the linked list is odd, we need to skip the middle element.
            slow = slow.next

        while slow:
            val = stack.pop()
            if val != slow.val:
                return False
            slow = slow.next
        return True

    # T : O(N), S : O(1).
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        # Reverse the first half of the linked list.
        while fast and fast.next:
            fast = fast.next.next  # For finding the middle.
            rev, rev.next, slow = slow, rev, slow.next  # Reverse.
            # ListNode* tmp = rev; rev = slow; slow = slow -> next; rev -> next = tmp;

        if fast:  # If the lenght of the linked list is odd, we need to skip the middle element.
            slow = slow.next

        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        # At the end rev goes to the "None" dummy head. Else return False.
        return not rev


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(arrayToListNode(numbers=[1, 2, 3, 4, 3, 2, 1]))
    assert sol.isPalindrome(arrayToListNode(numbers=[1, 2, 3, 4, 4, 3, 2, 1]))
    assert sol.isPalindrome(arrayToListNode(numbers=[1]))
    assert sol.isPalindrome(arrayToListNode(numbers=[1, 2, 1]))
    assert not (sol.isPalindrome(arrayToListNode(numbers=[1, 7, 2, 3, 4, 3, 2, 1])))
    assert not (sol.isPalindrome(arrayToListNode(numbers=[1, 7, 2, 3, 4, 4, 3, 2, 1])))
    assert not (sol.isPalindrome(arrayToListNode(numbers=[1, 7])))
    assert not (sol.isPalindrome(arrayToListNode(numbers=[1, 7, 2, 1])))
