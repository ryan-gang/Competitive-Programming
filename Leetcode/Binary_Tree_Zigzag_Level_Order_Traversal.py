from collections import deque
from typing import Optional
from StarterCode.binary_tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        We use a queue, and use its functionality to pop, and append to both sides,
        to achieve the zig-zag output.
        For zig -> popleft, append, left to right.
        For zag -> pop, appendleft, right to left.
        """
        if not root:
            return []
        out: list[list[int]] = []
        l2r = True
        queue: deque[TreeNode] = deque([root])
        while queue:
            inner: list[int] = []
            for _ in range(len(queue)):
                if l2r:
                    val = queue.popleft()
                    if val.left:
                        queue.append(val.left)
                    if val.right:
                        queue.append(val.right)
                else:
                    val = queue.pop()
                    if val.right:
                        queue.appendleft(val.right)
                    if val.left:
                        queue.appendleft(val.left)
                inner.append(val.val)
            out.append(inner)
            l2r = not l2r
        return out
