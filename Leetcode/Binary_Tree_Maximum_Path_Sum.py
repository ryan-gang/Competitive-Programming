import sys
from typing import Optional
from StarterCode.binary_tree import TreeNode


class Solution:
    """
    The idea is to do a DFS, till the leaf of a node, and from there create the optimal path.
    If the sum of a subtree is negative we can ignore it.
    At every node, we calculate the max path sum which is the left_tree + right_tree + node
    We keep a track of the max_sum, but this value can't be used to calculate the max_sum for
    the parent node of this node, because this contains both the left and right subtrees, so
    the path won't be valid anymore, so the function has to return the max of the sum of the
    one sided trees. But the total path_sum with that node is calculated and taken into
    consideration.
    """

    # Runtime: 202 ms, faster than 40.51%.
    # Memory Usage: 21.4 MB, less than 31.96%.
    # T : O(N), S : O(N)
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        max_sum = -sys.maxsize

        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_sum

            if not node:
                return 0

            gain_from_left_subtree = max(0, gain_from_subtree(node.left))
            gain_from_right_subtree = max(0, gain_from_subtree(node.right))
            # max_path_sum with left_tree, right_tree and root node.
            max_sum = max(gain_from_left_subtree + gain_from_right_subtree + node.val, max_sum)

            # But we only return the max sum for a path starting at the root of subtree
            # taking one side of the tree, not both sides.
            return max(gain_from_left_subtree, gain_from_right_subtree) + node.val

        gain_from_subtree(root)
        return max_sum
