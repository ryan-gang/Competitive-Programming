# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def traverseAndNegateList(self, node):
        while node:
            node.val = -node.val
            node = node.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA, nodeB, nodeIntrsct = headA, headB, None
        self.traverseAndNegateList(nodeA)
        self.traverseAndNegateList(nodeB)
        node = nodeA
        while node.next:
            if node.val > 0:
                nodeIntrsct = node
                break
            node = node.next
        return nodeIntrsct
