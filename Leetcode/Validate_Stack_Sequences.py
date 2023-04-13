from collections import deque


class Solution:
    # Runtime: 74 ms, faster than 55.80%.
    # Memory Usage: 13.9 MB, less than 99.86%.
    # T : O(N), S : O(N)
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Keep pushing all values into the stack, and whenever the top value
        matches with the popped array, greedily pop.
        """
        stack: deque[int] = deque()
        i, j = 0, 0
        while i < len(pushed):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            i += 1

        return not stack


if __name__ == "__main__":
    sol = Solution()
    assert sol.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
