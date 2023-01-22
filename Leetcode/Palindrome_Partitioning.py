from typing import List, Set


class Solution:
    # Runtime: 650 ms, faster than 90.48%.
    # Memory Usage: 30.2 MB, less than 69.80%.
    # T : O(N^2 + 2^N), S : O(N)
    # N^2 for creating a list of all palindromes,
    # 2^N for perusing all substrings, checking for palindromes.
    def partition(self, s: str) -> List[List[str]]:
        """
        First we generate a list of all possible palindromes in the given string.
        Both odd length, and even length.
        We use a trick where we start from an index, and expand outwards while checking for matches.
        Then we iterate over the entire string, using backtracking, and check for palindromes.
        """
        n = len(s)
        palindromes: Set[str] = set()

        for idx in range(n):
            palindromes.add(s[idx])
            lo, hi = idx - 1, idx + 1
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                palindromes.add(s[lo : hi + 1])
                lo -= 1
                hi += 1

            lo, hi = idx, idx + 1
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                palindromes.add(s[lo : hi + 1])
                lo -= 1
                hi += 1

        all_seqs: List[List[str]] = []

        def dfs(seq: List[str], idx: int):
            if idx == n:
                all_seqs.append(seq[:])
                return
            for i in range(idx, n):
                if s[idx : i + 1] in palindromes:
                    seq.append(s[idx : i + 1])
                    dfs(seq, i + 1)
                    seq.pop()

        dfs([], 0)
        return all_seqs


if __name__ == "__main__":
    sol = Solution()
    assert sol.partition(s="aab") == [["a", "a", "b"], ["aa", "b"]]
    assert sol.partition(s="a") == [["a"]]
