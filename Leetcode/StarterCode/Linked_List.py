from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next

    def __str__(self):
        s = f"ListNode -> val: {self.val}, next: {self.next}."
        return s


# Definition for doubly-linked list.
class DLListNode(ListNode):
    def __init__(
        self, x: int, next: Optional["DLListNode"] = None, prev: Optional["DLListNode"] = None
    ):
        self.val = x
        self.prev, self.next = prev, next


# Util methods.
def linkedListToStringRepresentation(node: ListNode) -> str:
    out = ""
    while node and node.next:
        out += f"{str(node.val)} -> "
        node = node.next

    if node:
        out += f"{(node.val)}"
    else:
        pass

    return out


def stringToIntegerList(input: str) -> list[int]:
    return list(map(int, input.split(",")))


def arrayToListNode(numbers: list[int]) -> Optional[ListNode]:
    """
    Takes in a array of integers and creates a linked list,
    returns the head of the linked list.
    """
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToListNode(input: str) -> Optional[ListNode]:
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


def prettyPrintLinkedList(node: Optional[ListNode]) -> None:
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
