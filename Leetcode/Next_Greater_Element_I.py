from collections import deque
from typing import List


class Solution:
    """
    We start iterating from the back of the array (nums2), if the stack's top element is larger
    than our current element, then this would be the 'next greater element' else we keep on popping
    values from the stack unless we get the larger than our current.
    Finally add our element on top of the stack.
    So essentially we have a monotonically decreasing stack.
    """

    # Runtime: 97 ms, faster than 62.77% of Python3 online submissions.
    # Memory Usage: 14.3 MB, less than 14.51% of Python3 online submissions.
    # T : O(N1+N2), S : O(N2)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}

        n = len(nums2)
        monotonic_stack = deque()
        for idx in range(n - 1, -1, -1):
            curr = nums2[idx]
            while monotonic_stack:
                if monotonic_stack[-1] > curr:
                    mapping[curr] = monotonic_stack[-1]
                    break
                else:
                    monotonic_stack.pop()
            monotonic_stack.append(curr)

        out = [-1] * len(nums1)
        for idx, val in enumerate(nums1):
            out[idx] = mapping.get(val, -1)
        return out


if __name__ == "__main__":
    sol = Solution()
    assert sol.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]) == [-1, 3, -1]
    assert sol.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]) == [3, -1]
