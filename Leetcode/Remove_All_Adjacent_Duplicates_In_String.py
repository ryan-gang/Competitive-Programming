from collections import deque


class Solution:
    # Runtime: 211 ms, faster than 40.85% of Python3 online submissions.
    # Memory Usage: 14.9 MB, less than 52.58% of Python3 online submissions.
    # Push all chars into stack, check if prev same as curr, if so pop prev,
    # and dont push curr, else push curr.
    # T : O(N), S : O(N)
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
                continue
            stack.append(char)

        return "".join(stack)

    # Runtime: 118 ms, faster than 80.10% of Python3 online submissions.
    # Memory Usage: 14.9 MB, less than 18.64% of Python3 online submissions.
    # In python, strings are immutable, so we create a list out of it to edit,
    # we overwrite the list with the proper deduped chars, i idx is the top,
    # if same as i + 1 ie curr, we pop as in i -= 2, which will overwrite the list later on.
    # T : O(N), S : O(N)
    def removeDuplicates2(self, s: str) -> str:
        list_s = list(s)
        i, j, n = 0, 0, len(list_s)
        for j in range(n - 1):
            i += 1
            j += 1
            list_s[i] = list_s[j]
            if list_s[i] == list_s[i - 1] and i > 0:
                i -= 2

        return "".join(list_s[: i + 1])


if __name__ == "__main__":
    sol = Solution()
    assert sol.removeDuplicates2(s="abbaca") == "ca"
    assert sol.removeDuplicates2(s="azxxzy") == "ay"
    assert sol.removeDuplicates2(s="z") == "z"
