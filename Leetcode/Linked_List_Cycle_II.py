from typing import Optional
from StarterCode.Linked_List import ListNode


"""
Floyd's algorithm.
To find the starting point of a loop in a linked list.
1. Find if a loop is present. If fast and slow pointers meet, keep fast there.
2. Set slow pointer to head, and then start iterating again, but this time both move
one node at a time. Where the fast and slow meet, is the start of the loop.

Ref : https://www.youtube.com/watch?v=zbozWoMgKW0
https://www.youtube.com/watch?v=LUm2ABqAs1w

How the math works :
<----------m----------><-  k  ->
[] -> [] -> [] -> [] -> [] -> [X] -> [] -> [] -> [] -|
                     |    Meets here                |
                     \\___ <-      L      ->_______//
m = distance from head to start of loop.
k = distance from start of loop, where fast and slow pointer meet. (X node)
l = length of loop.

Fast pointer is "p", slow pointer is "q".
distance_p = m + (p * l) + k. (m + p times rotation around loop "l" and then finally k
(where pointers meet)).
distance_q = m + (q * l) + k
p moves at twice the speed of q. So,
distance_p = 2 x distance_q
m + pl + k = 2m + 2ql + 2k
m + k = l x (p - 2q) ; p, q are both integers, so p - 2q is an integer.
Hence m + k = Z x l. Where Z is an int.

Upto this point, "p" has come to node X and met with "q".
Now we keep "p" here, and take "q" back to head.
From here, q will move m distance to meet with "p".
But p is currently at k distance from the start of the loop.
So when p and q meet, p will have travelled m + k distance from the start of the loop.
From our previous finding, m + k = Z x l.
So p will have moved Z times around the loop, and will be at the start of the loop.
Similarly, "q" will also be at the start of the loop. We have found the start of the loop.
"""


class Solution:
    # Runtime: 42 ms, faster than 99.66% of Python3 online submissions.
    # Memory Usage: 17.3 MB, less than 94.36% of Python3 online submissions.
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # This will find if a loop is present.
        # If a loop is present, fast and slow will anyway meet at some position.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # As soon as we find a loop, we start the next part of the algo, and return.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # No loop in the linked list. Fast has reached the end of the loop ie None.
        return None
