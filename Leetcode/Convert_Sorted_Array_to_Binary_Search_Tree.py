from typing import Optional, List
from StarterCode.binary_tree import TreeNode


class Solution:
    # Runtime: 162 ms, faster than 15.73% of Python3 online submissions.
    # Memory Usage: 15.6 MB, less than 82.55% of Python3 online submissions.
    def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:
        return Solution.insert(nums, 0, len(nums) - 1)

    @staticmethod
    def insert(array: List[int], start: int, end: int) -> Optional[TreeNode]:
        # Base case.
        # When there are no valid subarrays left, we will hit this, and return None.
        if start < end:
            return None
        else:
            # We recursively find the middle element, create the root node,
            # and then call the same method, to create the 2 subarrays on left and right.
            mid = (start + end) // 2
            node = TreeNode(array[mid])
            node.left = Solution.insert(array, start, mid - 1)
            node.right = Solution.insert(array, mid + 1, end)

            return node


class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node],
            self.sortedArrayToBST(nums[:mid_node]),
            self.sortedArrayToBST(nums[mid_node + 1:]),
        )
