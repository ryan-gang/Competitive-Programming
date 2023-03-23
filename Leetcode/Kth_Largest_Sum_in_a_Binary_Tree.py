import heapq
from collections import deque
from typing import Optional
from StarterCode.binary_tree import TreeNode


class Solution:
    # T : O(E), S : O(E) ; Where E is the number of edges.
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        heap = []
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            heapq.heappush(heap, level_sum)

        out: list[int] = heapq.nlargest(k, heap)
        if len(out) != k:
            return -1
        else:
            return out[-1]
