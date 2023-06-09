from collections import deque
from typing import Deque


class Solution:
    # Runtime: 51 ms, faster than 22.21%.
    # Memory Usage: 16.2 MB, less than 62.96%.
    # T : O(N + M), S : O(N + M)
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str):
            stack: Deque[str] = deque()
            i = 0
            while i < len(s):
                if s[i] == "#" and stack:
                    stack.pop()
                elif s[i] != "#":
                    stack.append(s[i])
                i += 1
            return stack

        return build(s) == build(t)

    # T : O(N + M), S : O(1)
    def backspaceCompare1(self, s: str, t: str) -> bool:
        # Iterate through the string in reverse. If we see a backspace character,
        # the next non-backspace character is skipped. If a character isn't skipped,
        # it is part of the final answer.
        def parse(word: str):
            skip = 0
            for ch in reversed(word):
                if ch == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch
            yield None
            # In every iteration, we have to yield something, else zip will not
            # work. So we return None.

        for c1, c2 in zip(parse(s), parse(t)):
            if c1 != c2:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.backspaceCompare(s="ab#c", t="ad#c")
    assert sol.backspaceCompare(s="a##c", t="#a#c")
    assert not sol.backspaceCompare(s="a#c", t="b")
    assert sol.backspaceCompare(s="bxj##tw", t="bxo#j##tw")
    assert not sol.backspaceCompare(s="bxj##tw", t="bxj###tw")
    assert not sol.backspaceCompare(s="bbbextm", t="bbb#extm")
    assert not sol.backspaceCompare(s="hd#dp#czsp#####", t="hd#dp#czsp#######")
    assert not sol.backspaceCompare(s="aaa###a", t="aaaa###a")
    assert not sol.backspaceCompare(s="a#c###", t="ad#c")
    assert sol.backspaceCompare("y#fo##f", "y#f#o##f")
