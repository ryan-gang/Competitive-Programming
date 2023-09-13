from typing import Optional
from StarterCode.Linked_List import ListNode
from StarterCode.Linked_List import arrayToListNode, prettyPrintLinkedList


class Solution:
    """
    To find the intersecting node, we need to "align" the two linked lists.
    One way of doing it is moving the head forwards in the longer tree.
    Or we can also concatenate the lists, end to end (In the next solution).
    Here we move the head forward in one of the list, to align them, and then
    iterate until we find the intersection.
    Both the solutions take 2 passes over the list, and no extra space.
    """

    # Runtime: 132 ms, faster than 49.46%.
    # Memory Usage: 31.46 MB, less than 86.21%.
    # T : O(N), S : O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA, nodeB = headA, headB
        lenA = self.getLength(nodeA)
        lenB = self.getLength(nodeB)

        if lenA >= lenB:
            diff = lenA - lenB
            nodeA = self.getNthNode(nodeA, diff + 1)
        else:
            diff = lenB - lenA
            nodeB = self.getNthNode(nodeB, diff + 1)

        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next
        return None

    def getNthNode(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n < 1:
            return None
        while head and n > 1:
            head = head.next
            n -= 1
        return head

    def getLength(self, node: Optional[ListNode]) -> int:
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    """
    The idea is if you switch head, the possible difference between length
    would be countered. On the second traversal, they either hit or miss. if
    they meet, p1 or p2 would be the node we are looking for, if they didn't
    meet, they will hit the end at the same iteration, p1 == p2 == None,
    return either one of them is the same.
        headA :  1 -> 2 -> 3 -> \
                                 -> 5 -> 6
        headB :            4 -> /
    Traversal by p1 : 1, 2, 3, 5, 6, 4, 5, 6
    Traversal by p2 : 4, 5, 6, 1, 2, 3, 5, 6
    Notice how they both end up at number 5 together after 7 steps.
    """
    # T : O(N), S : O(1)
    def getIntersectionNode1(
        self, headA: Optional[ListNode], headB: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            # If either pointer hits the end, switch head and continue the second traversal,
            # else just move on to next node.
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        return p1


if __name__ == "__main__":
    sol = Solution()
    array = [1, 2, 3, 4, 3, 2, 1]
    headA = arrayToListNode(array)
    headB = ListNode(0, next=ListNode(10, next=headA))

    prettyPrintLinkedList(headA)
    prettyPrintLinkedList(headB)

    if headA:
        intersection_node = sol.getIntersectionNode(headA, headB)
        prettyPrintLinkedList(intersection_node)
