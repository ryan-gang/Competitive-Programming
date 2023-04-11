from collections import deque


class Solution:
    # Runtime: 220 ms, faster than 86.64%.
    # Memory Usage: 15.6 MB, less than 77.42%.
    # T : O(N), S : O(N)
    def removeStars(self, s: str) -> str:
        stack: deque[str] = deque()
        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()

        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeStars(s="leet**cod*e") == "lecoe"
    assert sol.removeStars(s="erase*****") == ""
