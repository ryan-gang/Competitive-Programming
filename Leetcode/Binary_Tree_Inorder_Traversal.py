from typing import List, Optional
from StarterCode.binary_tree import TreeNode


# T : O(N), S : O(N) (Either extra stack space, or function call stack.)
class Solution:
    def __init__(self):
        self.tree = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            self.inorderTraversal(root.left)
            self.tree.append(root.val)
            self.inorderTraversal(root.right)

        return self.tree

    # One Liner. Very unoptimal.
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

    # TODO
    # MORRIS TRAVERSAL.
    # Tushar : https://www.youtube.com/watch?v=wGXB9OWhPTg
    # GFG : https://www.geeksforgeeks.org/
    # inorder-tree-traversal-without-recursion-and-without-stack/
    # Ref : https://leetcode.com/problems/binary-tree-inorder-traversal/
    # discuss/668448/Morris-Traversal

    # Takes linear time, but no extra space. Saves a lot of space in that way.
    def inorderTraversalMT(self, root: TreeNode) -> List[int]:
        res = []
        while root:
            if (
                not root.left
            ):  # if we don't have a left, this is our best in-order value at the moment.
                # add it to the list and move right.
                res.append(root.val)
                root = root.right
            else:
                pred = self.findPredecessor(root)
                # find the predecessor for the given node.
                # This is the farthest right of the first left we see.

                # if we have a right we have move on to explore this sub tree.
                # The pred.right != root check is to ensure that we're not ex
                if pred.right != root:
                    pred.right = root
                    root = root.left
                else:
                    # otherwise, we have found a pointer back to the current root and we need to
                    # rewrite the tree structure. This is basically a form of "have we seen this
                    # before?".
                    root.left = None

        return res

    def findPredecessor(self, root: TreeNode) -> TreeNode:
        curr = root.left
        while curr.right and curr.right != root:
            curr = curr.right

        return curr
