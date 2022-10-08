from collections import deque
from typing import Optional, List
from StarterCode.binary_tree import TreeNode


class Solution:
    # Runtime: 74 ms, faster than 19.13% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 83.93% of Python3 online submissions.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        queue = deque([root])
        while queue:
            next_level = []
            level_out = []
            current_level = queue
            # At every iteration, we exhaust the current level of nodes, in the queue.
            # Before adding the next level, which is in next_level.
            while current_level:
                node = current_level.popleft()
                if node:
                    level_out.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)

            if level_out:
                result.append(level_out)
            queue.extend(next_level)

        return result

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, result = deque([root]), []

        while queue:
            level = []
            # Here also, we only iterate over all the single level nodes, before moving on.
            # Once the loop starts, the values are frozen, and we do not go over the entire queue.
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
