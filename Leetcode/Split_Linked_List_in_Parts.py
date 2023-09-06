from StarterCode.Linked_List import ListNode
from typing import Optional


class Solution:
    def get_list_length(self, head: Optional[ListNode]) -> int:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        return length

    def get_nth_node_from_head(self, node: Optional[ListNode], n: int) -> Optional[ListNode]:
        while n > 1 and node:
            node = node.next
            n -= 1
        return node

    # T : O(N+K), S : O(K)
    # Time for get_length, and for severing edges.
    # Space only for k pointers.
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        length = self.get_list_length(head)
        base_length = length // k
        remaining_nodes = length - (base_length * k)
        out: list[Optional[ListNode]] = [None] * k
        node, idx = head, 0

        while idx < k:
            l = base_length
            if remaining_nodes > 0:
                l += 1
                remaining_nodes -= 1
            out[idx] = node
            tail = self.get_nth_node_from_head(node, l)
            if tail is None:
                break
            next_head = tail.next
            tail.next = None
            node = next_head
            idx += 1
        return out
