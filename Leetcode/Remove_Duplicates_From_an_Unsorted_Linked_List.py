# https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1
from typing import Optional


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def removeDuplicates(self, head):
        d = set()
        prev: Optional[Node] = None
        node = head
        while node:
            if node.data not in d:
                d.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next
        return head
