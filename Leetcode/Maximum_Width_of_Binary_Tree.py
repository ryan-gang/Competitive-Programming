from collections import deque
from StarterCode.binary_tree import TreeNode


class Solution:
    # Runtime: 44 ms, faster than 77.5%.
    # Memory Usage: 14.8 MB, less than 39.48%.
    # T : O(N), S : O(N)
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        We give a number to every node, if we had to convert the tree into a
        list or a heap, this number would've been it's index. So accordingly for
        each node (`num`), it's left child is numbered as `2 * num`, and right
        child is numbered as `2 * num + 1`.
        Ex : https://imgur.com/a/v7QEiSy
        Now, we traverse the tree in a
        level order fashion, and based on the numberings find the width between
        leftmost and rightmost node.
        """
        ans = 0
        queue: deque[tuple[TreeNode, int]] = deque()
        queue.append((root, 0))

        while queue:
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)

            for _ in range(len(queue)):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return ans
