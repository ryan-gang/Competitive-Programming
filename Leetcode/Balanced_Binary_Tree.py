import sys
from typing import List, Optional, Tuple
from StarterCode.binary_tree import TreeNode


class Solution:
    """
    We can find the heights of all the subtrees, and then check for the condition at every level,
    which makes the time complexity O(NLogN), if we can check the condition whilst we find
    the height, we can make this into O(N) T and O(H) S, where H is the height of the tree,
    which we require for the call stack.
    """

    # Runtime: 68 ms, faster than 79.54% of Python3 online submissions.
    # Memory Usage: 18.7 MB, less than 60.61% of Python3 online submissions.
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return Solution.get_height(root) != sys.maxsize

    @staticmethod
    def get_height(node: Optional[TreeNode]):
        if node is None:
            return 0
        left_tree = Solution.get_height(node.left)
        right_tree = Solution.get_height(node.right)
        if left_tree == sys.maxsize or right_tree == sys.maxsize:
            return sys.maxsize

        if abs(left_tree - right_tree) <= 1:
            return max(left_tree, right_tree) + 1
        else:
            return sys.maxsize

    # Traverse the tree and track the largest and smallest depth of each leaf node.
    # Then compare the largest and smallest depth.
    def is_balanced_v2(self, node):
        min_depth = 10**100
        max_depth = -(10**100)
        queue: List[Tuple[TreeNode, int]] = [(node, 0)]
        visited = [node]

        while len(queue) > 0:
            curr_node, curr_depth = queue.pop(0)

            if curr_node.left is None and curr_node.right is None:
                if curr_depth > max_depth:
                    max_depth = curr_depth
                if curr_depth < min_depth:
                    min_depth = curr_depth
            else:
                if curr_node.left and curr_node.left not in visited:
                    visited.append(curr_node.left)
                    queue.append((curr_node.left, curr_depth + 1))
                if curr_node.right and curr_node.right not in visited:
                    visited.append(curr_node.right)
                    queue.append((curr_node.right, curr_depth + 1))

        return max_depth - min_depth < 2
