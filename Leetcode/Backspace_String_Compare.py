from collections import deque


class Solution:
    # Runtime: 53 ms, faster than 39.08% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 74.96% of Python3 online submissions.
    # T : O(N + M), S : O(N + M)
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = deque()
        stack_t = deque()
        i = j = 0
        while i < len(s):
            if s[i] != "#":
                stack_s.append(s[i])
            else:
                if stack_s:
                    stack_s.pop()
            i += 1
        while j < len(t):
            if t[j] != "#":
                stack_t.append(t[j])
            else:
                if stack_t:
                    stack_t.pop()
            j += 1

        return stack_t == stack_s

    def backspaceCompareToDo(self, s: str, t: str) -> bool:
        def parse(word):
            skip = 0
            for ch in reversed(word):
                if ch == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch
            yield None  # In every iteration, we have to yield something, else zip will not work. So we return None.

        for c1, c2 in zip(parse(s), parse(t)):
            if c1 != c2:
                return False

        return True


sol = Solution()
assert sol.backspaceCompare(s="ab#c", t="ad#c")
assert sol.backspaceCompare(s="a##c", t="#a#c")


def parse(word):
    skip = 0
    for ch in reversed(word):
        if ch == "#":
            skip += 1
        elif skip:
            skip -= 1
        else:
            yield ch
    yield None


print([i for i in parse("#a#c")])
# Need to do some research on this.

# https://leetcode.com/problems/backspace-string-compare/solution/1378698
