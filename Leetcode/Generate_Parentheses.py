from typing import List


class Solution:
    # Runtime: 64 ms, faster than 31.35% of Python3 online submissions.
    # Memory Usage: 14.1 MB, less than 76.89% of Python3 online submissions.
    def generateParenthesis2(self, n: int) -> List[str]:
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

    # Runtime: 73 ms, faster than 33.65%.
    # Memory Usage: 14.3 MB, less than 41.12%.
    # T : O(4**n/sqrt(n)), S : O(4**n/sqrt(n))
    # Ref : https://leetcode.com/problems/generate-parentheses/solution/
    # loose T : O(n x (2 ** 2n))
    # 2 ^ 2n possible paren sequences, and for each sequence, we copy to out so n time.
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Same idea as the prev implementation.
        We keep a track of open parens, because if there are no opens, we can't add a closed one.
        We also keep a track of all open parens, this count can go above n.
        That's it, ending criteria is that the length of the sequence will be 2n.
        """
        out = []

        def recurse(sequence: List[str], unclosed_opens: int, total_opens: int) -> None:
            if len(sequence) == 2 * n:
                out.append("".join(sequence))
            if unclosed_opens > 0:
                sequence.append(")")
                recurse(sequence[:], unclosed_opens - 1, total_opens)
                sequence.pop()
            if total_opens < n:
                sequence.append("(")
                recurse(sequence[:], unclosed_opens + 1, total_opens + 1)
                sequence.pop()

        recurse([], 0, 0)
        return out


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.generateParenthesis(n=3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )
