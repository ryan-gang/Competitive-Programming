from collections import deque
from typing import Deque, List


class Solution:
    """
    Naive implementation using stack.
    Each time checking last k elements, if they are dupes.
    TLE.
    """

    def removeDuplicatesTLE(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= k and stack[-k:] == [char] * k:
                for _ in range(k):
                    stack.pop()
        return "".join(stack)

    """
    Same logic, but instead of splicing, using loops.
    """

    def removeDuplicatesTLE2(self, s: str, k: int) -> str:
        stack = deque()
        for char in s:
            stack.append(char)
            while len(stack) >= k:
                remove = True
                for i in range(1, k + 1):
                    if stack[-i] != char:
                        remove = False
                        break
                if remove:
                    for _ in range(k):
                        (stack.pop())
                        if stack:
                            char = stack[-1]
                else:
                    break
        return "".join(stack)

    """
    Stack also keeps track of the count of the duplicate elements.
    Though we keep all the dupes, so we have all k duplicate elements.
    Popping is tedious, pop all k occurences.
    """
    # Runtime: 294 ms, faster than 47.73%.
    # Memory Usage: 25.6 MB, less than 6.92%.
    # T : O(N), S : O(N)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        prev = None
        for char in s:
            new_count = 1
            if stack:
                prev, count = stack[-1]
                if prev == char:
                    new_count = count + 1

            stack.append((char, new_count))

            while stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()

        return "".join(entry[0] for entry in stack)

    """
    Stack keeps track of running count of current char.
    If count goes up to "k", then we pop the top element.
    We also append only 1 out of the duplicated elements.
    So popping is also done to only 1 element.
    """
    # T : O(N), S : O(N)
    def removeDuplicatesClean(self, s: str, k: int) -> str:
        stack: Deque[List[str, int]] = deque([["#", 0]])
        # List can only contain 1 datatype, so Py thinks 2nd element is supposed to be str.
        for char in s:
            if stack[-1][0] == char:
                # Instead of appending dupe again, we are updating count in prev element.
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        return "".join(c * k for c, k in stack)

    """
    Ref : discuss/392933/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
    List, initially contains all the chars from "s".
    Another list "count" keeps a running count of repeated chars.
    If this count goes to "k", then we reduce i by k, and set count to 1.
    This will overwrite prev chars, and is similar to popping. O(1) time.
    """

    def removeDuplicates2P(self, s: str, k: int) -> str:
        i, n = 0, len(s)
        stack, count = list(s), [0] * n
        for j in range(n):
            stack[i] = stack[j]
            if i > 0 and stack[i - 1] == stack[j]:
                count[i] = count[i - 1] + 1
            else:
                count[i] = 1
            if count[i] == k:
                i -= k
            i += 1
        return "".join(stack[0:i])


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeDuplicatesClean(s="deeedbbcccbdaa", k=3) == "aa"
    assert sol.removeDuplicatesClean(s="pbbcggttciiippooaais", k=2) == "ps"
    assert sol.removeDuplicatesClean(s="abcd", k=2) == "abcd"
    assert sol.removeDuplicatesClean(s="yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", k=4) == "ybth"
