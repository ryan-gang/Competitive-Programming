from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Recursively travel to all the nodes, keeping track of the depth of the current node, if it
    matches with our required depth, just add a new node, with the given val, and the subtree as
    its subtree. To make the depth=1 case much easier to handle, we can add a dummy node which is a
    parent of root, and then perform the operation on top of this dummy,
    and finally just return dummy.left"""

    # Runtime: 125 ms, faster than 13.33% of Python3 online submissions.
    # Memory Usage: 17.5 MB, less than 15.91% of Python3 online submissions.
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy_root = TreeNode(val=None, left=root, right=None)
        self.depth = depth
        self.val = val

        def recurse(depth, node):
            if depth == self.depth:
                left_tmp = node.left
                right_tmp = node.right

                node.left = TreeNode(val=self.val, left=left_tmp)
                node.right = TreeNode(val=self.val, right=right_tmp)
                return

            if node.left:
                recurse(depth + 1, node.left)
            if node.right:
                recurse(depth + 1, node.right)

        recurse(depth=1, node=dummy_root)
        return dummy_root.left
