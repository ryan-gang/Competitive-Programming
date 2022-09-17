from typing import List


class Solution:
    # Runtime: 51 ms, faster than 42.22% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 31.64% of Python3 online submissions.
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        out = []

        def combine(idx, word):
            if idx == len(digits):
                if idx > 0:
                    out.append(word)
                return
            digit = digits[idx]
            for i in mapping[digit]:
                combine(idx + 1, word + i)

        combine(0, "")
        return out


sol = Solution()
print(sol.letterCombinations(""))
assert sol.letterCombinations(digits="23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
