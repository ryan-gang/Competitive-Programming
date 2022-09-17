from typing import List


class Solution:
    # Runtime: 104 ms, faster than 36.24% of Python3 online submissions.
    # Memory Usage: 14.7 MB, less than 81.32% of Python3 online submissions.
    # T : O(2 ^ N), S : O(2 ^ N)
    # where n = len(s)
    # Worst case, all chars are letters, we make 2^N calls.
    # S : O(2^N) because of storing the output, might not be counted, auxiliary stack space : O(N)
    def letterCasePermutation(self, s: str) -> List[str]:
        self.permutations = []
        self.s = s
        self.permute("", 0)
        return self.permutations

    def permute(self, string: str, i: int):
        if len(string) == len(self.s):
            self.permutations.append(string)
            return

        if self.s[i].isalpha():
            self.permute(string + self.s[i].lower(), i + 1)
            self.permute(string + self.s[i].upper(), i + 1)
        else:
            self.permute(string + self.s[i], i + 1)

    def permuteClean(self, string: str, i: int):
        if len(string) == len(self.s):
            self.permutations.append(string)
            return

        if self.s[i].isalpha():
            self.permute(string + self.s[i].swapcase(), i + 1)
        # Next call with current char always. Even if number or anything.
        # Extra call with swapped case if alphabet.
        self.permute(string + self.s[i], i + 1)


sol = Solution()
assert sol.letterCasePermutation("a1b2") == ["a1b2", "a1B2", "A1b2", "A1B2"]
assert sol.letterCasePermutation("3z4") == ["3z4", "3Z4"]
