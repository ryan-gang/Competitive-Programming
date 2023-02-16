from StarterCode.binary_tree import TreeNode
from collections import deque
from typing import Optional


class Solution:
    # Runtime: 55 ms, faster than 18.76%.
    # Memory Usage: 15.2 MB, less than 98.15%.
    # T : O(Nodes), S : O(Nodes)
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth, max_depth = 0, 1
        queue = deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop()
                if not node.left and not node.right:
                    max_depth = max(max_depth, depth)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

        return max_depth

    # Runtime: 36 ms, faster than 94.60%.
    # Memory Usage: 16.2 MB, less than 49.77%.
    # T : O(Nodes), S : O(Nodes)
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        max_depth = [0]

        def dfs(node: TreeNode, depth: int) -> None:
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
            if not node.left and not node.right:
                max_depth[0] = max(depth, max_depth[0])

        if root:
            dfs(root, 1)
            return max_depth[0]
        else:
            return 0
