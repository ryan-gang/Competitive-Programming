from typing import List


class Solution:
    # Runtime: 64 ms, faster than 31.35% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 76.89% of Python3 online submissions.
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def recurse(opens: int, closes: int, curr_open: int, parentheses: str) -> None:
            if (opens + closes) == 2 * n:
                out.append(parentheses)
                return
            if opens < n:
                recurse(opens + 1, closes, curr_open + 1, parentheses + "(")
            if closes < n and curr_open > 0:
                recurse(opens, closes + 1, curr_open - 1, parentheses + ")")

        recurse(0, 0, 0, "")
        return out


sol = Solution()
assert sol.generateParenthesis(n=3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
