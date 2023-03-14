from typing import Optional
from StarterCode.binary_tree import TreeNode


class Solution:
    # Runtime: 35 ms, faster than 48%.
    # Memory Usage: 13.9 MB, less than 10.80%.
    # T : O(N), S : O(H), where N is total nodes, H is height of tree
    # (stack space for recursion.)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # DFS solution.
        # Recursively traverse to all child nodes, whilst keeping track of the value till now.
        add = 0

        def traverse(node: TreeNode, num: int) -> None:
            nonlocal add
            val = num * 10 + node.val
            if not node.left and not node.right:
                add += val
            if node.left:
                traverse(node.left, val)
            if node.right:
                traverse(node.right, val)

        if root:
            traverse(root, 0)
        return add

    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], cur: int) -> int:
            if not root:
                return 0
            cur = cur * 10 + root.val
            if not root.left and not root.right:
                return cur
            return dfs(root.left, cur) + dfs(root.right, cur)

        return dfs(root, 0)
