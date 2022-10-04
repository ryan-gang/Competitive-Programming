from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Runtime: 76 ms, faster than 50.85% of Python3 online submissions for Path Sum.
    # Memory Usage: 15 MB, less than 91.98% of Python3 online submissions.
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.flag = False
        self.targetSum = targetSum

        def dfs(node: Optional[TreeNode], currSum: int) -> bool:
            # If current node is valid, process it.
            # This hasn't been processed yet.
            if node:
                # We add the current node's value inside the function, and then check with target.
                currSum += node.val
                if currSum == self.targetSum:
                    # Along with adding up to target, the path also has to end in a leaf node.
                    if node.left is None and node.right is None:
                        self.flag = True
                if not self.flag:
                    dfs(node.left, currSum)
                    dfs(node.right, currSum)
                else:
                    # If we already found our answer, no more function calls required.
                    # Included only for some tail calls being ignored.
                    return

        if not root:
            return False
        dfs(root, 0)
        return self.flag

    # BRILLIANT.
    # Ref: https://leetcode.com/problems/path-sum/discuss/36360/Short-Python-recursive-solution-O(n)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and self.root == targetSum:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )
