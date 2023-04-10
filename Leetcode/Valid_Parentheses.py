from collections import deque


class Solution:
    # Runtime: 31 ms, faster than 74.42%.
    # Memory Usage: 13.9 MB, less than 16.28%.
    # T : O(N), S : O(N)
    def isValid(self, s: str) -> bool:
        """
        For every opening parentheses we just push it to a stack, and for every
        closing parentheses we pop from the stack and check if the parentheses
        match, or if stack is empty return False.
        """
        stack: deque[str] = deque()
        mapping = {")": "(", "]": "[", "}": "{"}

        for i in s:
            # print(stack)
            if i in mapping.keys():
                if not stack or stack.pop() != mapping[i]:
                    return False
            else:
                stack.append(i)

        return not stack


if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid(s="()(((((((())))))))")
    assert not (sol.isValid(s="()((((("))
    assert not (sol.isValid(s="()))))))"))
    assert sol.isValid(s="()[]{}")
    assert not (sol.isValid(s="([{})]"))
