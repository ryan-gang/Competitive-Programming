from StarterCode.Linked_List_Utils import arrayToListNode, prettyPrintLinkedList

head = arrayToListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
prettyPrintLinkedList(head)

left = 3
right = 7

"""
curr = head
count = left - 2
while count > 0:
    curr = curr.next
    count -= 1

pre_left = curr

curr = head
count = right
while count > 0:
    curr = curr.next
    count -= 1

post_right = curr

N = (right - left + 1) - 1
curr = pre_left.next
curr_next = curr.next
while N > 0:
    post_curr_next = curr_next.next
    curr_next.next = curr
    curr = curr_next
    curr_next = post_curr_next
    N -= 1
rev_head = curr

pre_left.next.next = post_right
pre_left.next = rev_head

prettyPrintLinkedList(head)
"""

curr = head
index = 1

while curr:
    if index == left - 1:
        pass