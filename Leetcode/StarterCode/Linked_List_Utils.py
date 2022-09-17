import json
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = f"ListNode -> val: {self.val}, next: {self.next}."
        return s


def linkedListToStringRepresentation(node):
    out = ""
    while node and node.next:
        out += f"{str(node.val)} -> "
        node = node.next

    if node:
        out += f"{(node.val)}"
    else:
        pass

    return out


def stringToIntegerList(input):
    return json.loads(input)


def arrayToListNode(numbers: List[int]) -> ListNode:
    """Takes in a array of integers and creates a linked list,
    returns the head of the linked list."""
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end="")
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


def inputListPrintLinkedList():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip("\n")

    lines = readlines()
    while True:
        try:
            line = next(lines)
            node = stringToListNode(line)
            prettyPrintLinkedList(node)
        except StopIteration:
            break
