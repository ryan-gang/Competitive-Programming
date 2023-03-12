from typing import Optional
from StarterCode.Linked_List_Utils import ListNode, arrayToListNode, prettyPrintLinkedList
from heapq import heappush, heappop


class Solution:
    """
    We create a new head, onto which we keep on adding nodes from the other linked lists.
    At every iteration we find the lowest value from the "k" heads, add this head to our
    new list, and update this head to its head.next.
    To find out the min value from the "k" heads, we use a min heap.
    """

    # Runtime: 107 ms, faster than 67.65%.
    # Memory Usage: 17.8 MB, less than 46.85%.
    # Insertions into the heap with at most K items will be O(log K), this is repeated
    # for NxK times. No extra space for new linked list, at most O(K) space for heap.
    # T : O(N x K x log K), S : O(K)
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = curr = ListNode(0)
        heap: list[tuple[int, int]] = []
        for idx, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, idx))

        while heap:
            _, idx = heappop(heap)  # We fetch the smallest value.
            # And add this node from its list to our output.
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
    lists: list[Optional["ListNode"]] = []
    for array in arrays:
        head = arrayToListNode(array)
        lists.append(head)
        prettyPrintLinkedList(head)

    prettyPrintLinkedList(sol.mergeKLists(lists))
