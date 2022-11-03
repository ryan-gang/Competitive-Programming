from typing import List, Optional
from StarterCode.Linked_List_Utils import ListNode, arrayToListNode, prettyPrintLinkedList
from heapq import heappush, heappop


class Solution:
    """
    We will create a new head, to which we will keep on adding nodes from the other linked lists.
    At every iteration we need to find the lowest value from the "k" heads.
    And then add this head to our new list, and set this head to its head.next.
    """

    # Runtime: 213 ms, faster than 61.03% of Python3 online submissions.
    # Memory Usage: 18.2 MB, less than 38.58% of Python3 online submissions.
    # Insertions into the heap with at most K items will be O(log K), this is repeated
    # for NxK times. No extra space for new linked list, at most O(K) space for heap.
    # T : O(N x K x log K), S : O(K)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = curr = ListNode(0)
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, idx))

        while heap:
            lowest_val, idx = heappop(heap)
            head = lists[idx]
            headnext = head.next
            curr.next = head
            curr = curr.next
            head = headnext
            lists[idx] = head
            if headnext:
                heappush(heap, (headnext.val, idx))

        return new_head.next


if __name__ == "__main__":
    sol = Solution()
    arrays = [[1, 4, 5, 5, 5, 5, 10], [1, 3, 4, 5, 6, 8, 11], [2, 6, 7, 8, 8, 10, 11]]
    # arrays = [[]]
    # arrays = []
    lists = []
    for array in arrays:
        head = arrayToListNode(array)
        lists.append(head)
        prettyPrintLinkedList(head)

    prettyPrintLinkedList(sol.mergeKLists(lists))
