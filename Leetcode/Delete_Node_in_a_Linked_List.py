from StarterCode.Linked_List import ListNode


class Solution:
    """
    We can copy all the next K nodes values to this node and the next K-1 nodes.
    A -> B -> C -> D -> E ; we can "delete" B by copying C to B, D to C, E to D.
    A -> C -> D -> E.
    """

    def deleteNode(self, node: ListNode) -> None:
        next_node = node.next
        while node.next.next:
            node.val = next_node.val
            node = next_node
            next_node = next_node.next

        node.val = next_node.val
        node.next = None

    """
    That is unimaginably stupid. JUST COPY THE NEXT NODE TO THIS NODE.
    And then "delete" the next node by skipping it.
    """
    # Runtime: 77 ms, faster than 52.72% of Python3 online submissions.
    # Memory Usage: 14.3 MB, less than 54.16% of Python3 online submissions.
    def deleteNode1(self, node: ListNode) -> None:
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        del next_node
