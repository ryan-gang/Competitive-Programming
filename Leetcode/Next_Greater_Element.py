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

    # T : O(N), S : O(N)
    def nextLargerElement(self, arr: List[int], n: int) -> List[int]:
        out = [-1] * n
        monotonic_stack = deque()
        for idx in range(n - 1, -1, -1):
            curr = arr[idx]
            while monotonic_stack:
                if monotonic_stack[-1] > curr:
                    out[idx] = monotonic_stack[-1]
                    break
                else:
                    monotonic_stack.pop()
            monotonic_stack.append(curr)

        return out


if __name__ == "__main__":
    sol = Solution()
    assert sol.nextLargerElement([1, 3, 2, 4], 4) == [3, 4, 4, -1]
    assert sol.nextLargerElement([6, 8, 0, 1, 3], 5) == [8, -1, 1, 3, -1]
    assert (sol.nextLargerElement(arr=[5, 5, 4, 7, 8, 9, 3, 2, 5, 2, 9, 9, 5, 1, 1], n=10)) == [
        7,
        7,
        7,
        8,
        9,
        -1,
        5,
        5,
        -1,
        -1,
    ]
