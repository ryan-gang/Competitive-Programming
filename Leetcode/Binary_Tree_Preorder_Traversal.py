from typing import List, Optional
from StarterCode.binary_tree import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return (
            [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
            if root
            else []
        )

    # Runtime: 59 ms, faster than 30.73% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 59.45% of Python3 online submissions.
    def preorder(self, node):
        if node:
            return [node.val] + self.preorder(node.left) + self.preorder(node.right)

        return []
