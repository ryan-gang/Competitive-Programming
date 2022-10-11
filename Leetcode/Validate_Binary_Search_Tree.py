import sys
from typing import Optional
from StarterCode.binary_tree import TreeNode


class Solution:
    """
    For every node and its children we calculate the range of values that will keep the BST valid.
    At the root the lower_bound and upper_bound are -inf, +inf.
    But as we go deeper on the left, we keep on decreasing the upper bound which is
    dictated by the parent node.
    Similarly for the right subtrees the lower_bound are set by the parent's value.
    More explanation in the CTCI."""

    # Runtime: 97 ms, faster than 21.37% of Python3 online submissions.
    # Memory Usage: 16.6 MB, less than 45.87% of Python3 online submissions.
    def isValidBST(self, root: Optional[TreeNode]):
        return Solution.validate(root, -sys.maxsize, sys.maxsize)

    @staticmethod
    def validate(node: Optional[TreeNode], lower_bound: int, upper_bound: int):
        if node:
            if not lower_bound < node.val < upper_bound:
                return False
            return Solution.validate(node.left, lower_bound, node.val) and Solution.validate(
                node.right, node.val, upper_bound
            )
        else:
            return True


class Solution2(object):
    """
    We create the inorder traversal of the BST, which will be a sorted array for a valid BST.
    After getting the traversal we check if all the elements are larger
    than the previous one in the array.
    """

    def isValidBST(self, root):
        output = []
        self.inorder(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True

    # Time complexity of inorder traversal is O(n)
    # Fun fact: Inorder traversal leads to a sorted array if it is
    # a Valid Binary Search. Tree.
    def inorder(self, root, output):
        if root is None:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
