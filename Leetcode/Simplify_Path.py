from collections import deque


class Solution:
    # Runtime: 34 ms, faster than 66.29%.
    # Memory Usage: 14 MB, less than 28.25%.
    # T : O(N), S : O(N)
    def simplifyPath(self, path: str) -> str:
        """
        We keep on pushing and popping every directory onto a stack, if we need
        to go back a directory, pop else push. All other conditions can be
        ignored.
        """
        parts = path.split("/")
        stack: deque[str] = deque()
        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    assert sol.simplifyPath(path="/a/./b/../../c/") == "/c"
    assert sol.simplifyPath(path="/../../../../../a") == "/a"
    assert sol.simplifyPath(path="/a/./b/./c/./d/") == "/a/b/c/d"
    assert sol.simplifyPath(path="/a/../.././../../.") == "/"
    assert sol.simplifyPath(path="/a//b//c//////d") == "/a/b/c/d"
