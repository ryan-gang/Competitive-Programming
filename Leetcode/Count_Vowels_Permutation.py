from typing import Dict, List


class SolutionTLE:
    # 5/43 TC passed. TLE.
    def countVowelPermutation(self, n: int) -> int:
        self.n: int = n
        # If current index is X, and current vowel is given, what will the X+1th vowel be.
        self.vowels: Dict[str, List[str]] = {
            "": ["a", "e", "i", "o", "u"],
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }
        return self.helper([]) % (1000000007)

    def helper(self, sequence: List[str]) -> int:
        prev_vowel = ""
        if len(sequence) == self.n:
            return 1
        elif len(sequence) > self.n:
            return 0
        # elif len(sequence) < self.n and len(sequence) > 0:
        else:
            # If length is equal to 0, prev_vowel will be "" only.
            if len(sequence) > 0:
                prev_vowel = sequence[-1]
            out = 0
            for vowel in self.vowels[prev_vowel]:
                out += self.helper(sequence + [vowel])

            return out


class Solution:
    # Runtime: 784 ms, faster than 43.09% of Python3 online submissions.
    # Memory Usage: 117.6 MB, less than 24.49% of Python3 online submissions.
    # T : O(N), S : O(N)
    # Space complexity can be improved, by using 2 sets of 5 variables, instead of dp array.
    def countVowelPermutation(self, n: int) -> int:
        """
        For words ending with "X", what are the options for the penultimate vowel.
        For example, words ending with "a", can only come from words ending with "e", "i" or "u".
        self.vowels: Dict[str, List[str]] = {
            "a": ["e", "i", "u"],
            "e": ["a", "i"],
            "i": ["e", "o"],
            "o": ["i"],
            "u": ["i", "o"],
        }
        sum(dp[i]) is the number of possible words formed of length (i + 1)
        dp[i][j] is the number of words formed of length i + 1 ending with vowel[j]
        """
        dp = [[0 for _ in range(5)] for __ in range(n)]
        # For length = 1, possible words for all vowels are -> 1.
        dp[0] = [1 for _ in range(5)]
        # "a" : 0, "e" : 1, "i" : 2, "o" : 3, "u" : 4
        for i in range(1, n):
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
            dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
            dp[i][3] = dp[i - 1][2]
            dp[i][4] = dp[i - 1][2] + dp[i - 1][3]
        return sum(dp[-1]) % (1000000007)

    # Ref : https://leetcode.com/problems/count-vowels-permutation/discuss/398286/Simple-Python-(With-Diagram)
    def count_vowel_permutations(n):
        # T : O(N), S : O(1)
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (1000000007)


sol = Solution()
assert (sol.countVowelPermutation(n=1)) == 5
assert (sol.countVowelPermutation(n=2)) == 10
assert (sol.countVowelPermutation(n=5)) == 68
print(sol.countVowelPermutation(n=144))
