from collections import deque


class Solution:
    # Runtime: 67 ms, faster than 55.60% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 97.60% of Python3 online submissions.
    # T : O(N), S : O(N)
    def makeGood(self, s: str) -> str:
        """
        We add all chars iteratively into a stack, if the top element in the stack is swapped_case
        of our current element, we can pop that out, and not push this in.
        This can be repeated for all the chars in the string.
        O(N) extra space required.
        In python as strings are immutable, we would need that space anyway, for any other algo.
        """
        stack = deque()
        for i in s:
            if stack and Solution.reverse_case(i, stack[-1]):
                stack.pop()
                continue
            stack.append(i)
        return "".join(stack)

    @staticmethod
    def reverse_case(char1: str, char2: str):
        if char1.swapcase() == char2:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.makeGood(s="abBAcC") == ""
    assert sol.makeGood(s="leEeetcode") == "leetcode"
    assert sol.makeGood(s="s") == "s"
