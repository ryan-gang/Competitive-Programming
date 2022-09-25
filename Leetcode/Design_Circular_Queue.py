# from StarterCode.Linked_List_Utils import prettyPrintLinkedList


# Ref : https://leetcode.com/problems/design-circular-queue/
# discuss/172230/Python3-with-a-single-list-beats-100
# Runtime: 120 ms, faster than 46.13% of Python3 online submissions.
# Memory Usage: 14.4 MB, less than 98.10% of Python3 online submissions.
class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return True

    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Ref : https://leetcode.com/problems/design-circular-queue/
# discuss/148837/Python-short-and-simple-AC-doubly-linked-list-solution
class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None


class MyCircularQueueDLLSol:
    def __init__(self, k):
        self.size = k
        self.curSize = 0
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        if self.curSize < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            node.pre.next = node.next.pre = node
            self.curSize += 1
            return True
        return False

    def deQueue(self):
        if self.curSize > 0:
            node = self.head.next
            node.pre.next = node.next
            node.next.pre = node.pre
            self.curSize -= 1
            return True
        return False

    def Front(self):
        return self.head.next.val

    def Rear(self):
        return self.tail.pre.val

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size


####################################################################################################
# Self implementation using a single list.
class MyCircularQueueList:
    def __init__(self, k: int):
        self.max_length = k
        self.start = 0
        self.end = -1
        self.length = 0
        self.queue = [None] * self.max_length

    def enQueue(self, value: int) -> bool:
        if self.validate_length() and self.validate_end_index():
            # Cannot add new elements to the end of the queue.
            self.end += 1
            self.queue[self.end] = value
            self.length += 1
            return True
        elif self.validate_length() and self.validate_start_index():
            if self.end == self.max_length - 1:
                self.end = 0
            else:
                self.end += 1
            self.queue[self.end] = value
            self.length += 1
            return True

        return False

    def deQueue(self) -> bool:
        if self.length > 0:
            if self.start == self.max_length:
                self.start = 0
            self.queue[self.start] = None
            self.start += 1
            self.length -= 1
            return True
        return False

    def Front(self) -> int:
        if self.length == 0:
            return -1
        else:
            return self.queue[self.start]

    def Rear(self) -> int:
        if self.length == 0:
            return -1
        else:
            return self.queue[self.end]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return not self.validate_length()

    def validate_length(self) -> bool:
        return self.length < self.max_length

    def validate_end_index(self) -> bool:
        return (self.end + 1) < self.max_length

    def validate_start_index(self) -> bool:
        return (self.start - 1) >= 0


####################################################################################################
# Definition for doubly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        s = f"ListNode -> val: {self.val}, next: {self.next}."
        return s


# Self implementation, with doubly linked list.
class MyCircularQueueDLL:
    def __init__(self, k: int):
        head = ListNode(1)
        prev = head
        for _ in range(2, k + 1):
            node = ListNode(_, next=prev)
            prev = node
        # loop creation. From tail to head.
        head.next = prev

        self.tail = head
        self.head = prev

        node = self.head
        for _ in range(k):
            node.next.prev = node
            node = node.next

        self.length = 0
        self.max_length = k

    def enQueue(self, value: int) -> bool:
        if self.length < self.max_length:
            self.head.val = value
            self.head = self.head.next
            self.length += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.length > 0:
            self.tail.val = None
            self.tail = self.tail.prev
            self.length -= 1
            return True
        return False

    def Front(self) -> int:
        if self.length > 0:
            return self.tail.next.val
        return -1

    def Rear(self) -> int:
        if self.length > 0:
            return self.head.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.max_length


####################################################################################################
obj = MyCircularQueue(k=3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())
print(obj.isFull())
# print(obj.length, obj.max_length)
print(obj.deQueue())
print(obj.enQueue(4))
# print(obj.queue)
print(obj.Rear())


obj = MyCircularQueue(k=2)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.deQueue())
print(obj.enQueue(3))
print(obj.deQueue())
print(obj.enQueue(3))
print(obj.deQueue())
print(obj.enQueue(3))
print(obj.queue)
print(obj.deQueue())
print(obj.queue)
print(obj.start, obj.end)
print(obj.Front())


obj = MyCircularQueue(k=3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())
print(obj.isFull())
# print(obj.length, obj.max_length)
print(obj.deQueue())
print(obj.enQueue(4))
# print(obj.queue)
print(obj.Rear())


obj = MyCircularQueue(k=2)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.deQueue())
print(obj.enQueue(3))
print(obj.deQueue())
print(obj.enQueue(3))
print(obj.deQueue())
print(obj.enQueue(3))
print(obj.deQueue())
print(obj.Front())


obj = MyCircularQueue(k=8)
print(obj.enQueue(3))
print(obj.enQueue(9))
print(obj.enQueue(5))
print(obj.enQueue(0))
print(obj.deQueue())
print(obj.deQueue())
print(obj.length, obj.max_length)
print(obj.isEmpty())
print(obj.isEmpty())
print(obj.Rear())
print(obj.Rear())
print(obj.deQueue())
