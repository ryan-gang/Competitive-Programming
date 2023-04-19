from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Runtime: 699 ms, faster than 5.13%.
    # Memory Usage: 62.6 MB, less than 19.5%.
    # T : O(N), S : O(N) ; Visits each node twice, and stores recursion stack, + dp.
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        dp: dict[int, dict[str, int]] = defaultdict(dict)

        def zig_zag_dfs(node: TreeNode, direction: str) -> int:
            """
            Given a node and the direction to move to, the function returns the
            longest path it can traverse.
            """
            val = 0
            if not node:
                return 0

            if (id(node)) not in dp or direction not in dp[id(node)]:
                if direction == "right" and node.right:
                    _ = zig_zag_dfs(node.right, "left") + 1
                    dp[id(node)]["right"] = _
                    val = max(val, _)

                if direction == "left" and node.left:
                    _ = zig_zag_dfs(node.left, "right") + 1
                    dp[id(node)]["left"] = _
                    val = max(val, _)
            else:
                val = dp[id(node)][direction]
            return val

        max_val = 0
        queue: deque[TreeNode] = deque()
        queue.append(root)
        # As the dfs method, doesn't traverse paths, but only follows whats given.
        # We need to visit each node, and start the dfs from that node taken as root.
        # To not visit a node multiple times, we store the max path length in a dp.
        while queue:
            # BFS to traverse all nodes, and start dfs from it.
            node = queue.popleft()
            val = max(zig_zag_dfs(node, "left"), zig_zag_dfs(node, "right"))
            max_val = max(val, max_val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return max_val


class Solution1:
    # Runtime: 572 ms, faster than 9.52%.
    # Memory Usage: 61.4 MB, less than 47.62%.
    # T : O(N), S : O(N) ; Visits each node once, and stores recursion stack.
    def __init__(self):
        self.max_step = 0

    def longest_zig_zag(self, root: Optional[TreeNode]):
        self.dfs(root, True, 0)
        self.dfs(root, False, 0)
        return self.max_step

    def dfs(self, root: Optional[TreeNode], is_left: bool, step: int) -> None:
        """
        This dfs, continues the path even if it hits a dead-end.
        If it hits a dead-end it breaks the zig-zag and starts afresh with length = 0.
        Else, at every node, it continues the zig-zag and increments length by 1.
        """
        if not root:
            return
        self.max_step = max(self.max_step, step)  # update max step so far
        if is_left:
            self.dfs(root.left, False, step + 1)  # keep going from root to left
            self.dfs(root.right, True, 1)  # restart going from root to right
        else:
            self.dfs(root.right, True, step + 1)  # keep going from root to right
            self.dfs(root.left, False, 1)  # restart going from root to left
