from collections import deque
from typing import Optional
from StarterCode.binary_tree import TreeNode


class Solution:
    # Runtime: 44 ms, faster than 16.39%.
    # Memory Usage: 14 MB, less than 52.29%.
    # T : O(N), S : O(N) where N is the number of nodes.
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Add all values for a specific level in a queue.
        Then match values from start and end, if they differ return False.
        Make sure to also include "None" values in this queue.
        """
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)

            lo = 0
            hi = len(queue) - 1
            while lo < hi:
                l, h = "None", "None"
                if queue[lo]:
                    l = queue[lo].val
                if queue[hi]:
                    h = queue[hi].val
                if l != h:
                    return False
                lo += 1
                hi -= 1
        return True

    # Runtime: 39 ms, faster than 43.16%.
    # Memory Usage: 13.9 MB, less than 90.34%.
    # T : O(N), S : O(N)
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        def is_symmetric_helper(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False

            return is_symmetric_helper(left.left, right.right) and is_symmetric_helper(
                left.right, right.left
            )

        return root is None or is_symmetric_helper(root.left, root.right)
