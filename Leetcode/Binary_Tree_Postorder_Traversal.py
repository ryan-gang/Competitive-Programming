from typing import List, Optional
from StarterCode.binary_tree import TreeNode


# This #pattern is important.
class Solution:
    # Runtime: 34 ms, faster than 90.31% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 60.82% of Python3 online submissions.
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return (
                self.postorderTraversal(root.left)
                + self.postorderTraversal(root.right)
                + [root.val]
            )

        return []
