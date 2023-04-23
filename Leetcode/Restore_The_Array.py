class Solution:
    # Runtime: 1680 ms, faster than 49.31%.
    # Memory Usage: 17.9 MB, less than 95.89%.
    # T : O(MLogK), S : O(M) ; where M is the length of s.
    # The inner loop for length is iterated at most log K times.
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        dp[i] is the number of ways of dividing the string from index
        "i" to the end.

        To that front, we start from the back, and work our way up. For every
        starting index in the iteration, we iterate over the possible lengths of
        the string (This is strictly bounded by k, as k < 10 ** 9 we can have at
        most 9 iterations in the inner loop for length) and check if the
        resulting number is valid or not, if valid it can be added to the
        dp[start+length] ways of dividing the string ; which in turn is the
        number of ways of dividing the string from start+length to the end.
        """
        n = len(s)
        mod = 10**9 + 7

        dp = [0] * (n + 1)
        dp[-1] = 1
        for start in range(n - 1, -1, -1):
            for length in range(1, n - start + 1):
                if s[start] == "0":  # If num starts with 0 it's invalid.
                    break
                num = int(s[start : start + length])  # Int representation of curr int.
                if num <= k:  # If num is lte k, it is valid.
                    dp[start] += dp[start + length]
                    # All the dp[start+length] ways can be extended by this int.
                    dp[start] %= mod
                else:
                    # But if num is gt k, we can break, all subsequent iterations will also be gt k.
                    break

        return dp[0]

    def numberOfArraysTLE(self, s: str, k: int) -> int:
        """
        Backtracking approach. Nothing is cached. Very un-optimal."""
        ways = 0
        n = len(s)

        def recurse(idx: int) -> None:
            if idx == n:
                nonlocal ways
                ways += 1
                return
            if s[idx] == "0":
                return
            for offset in range(1, n - idx + 1):
                num = int(s[idx : idx + offset])
                if num <= k:
                    recurse(idx + offset)

        recurse(0)
        return ways


if __name__ == "__main__":
    sol = Solution()
    assert sol.numberOfArrays(s="1317", k=2000) == 8
    assert sol.numberOfArrays(s="1234567890", k=90) == 34
    assert (
        sol.numberOfArrays(s="600342244431311113256628376226052681059918526204", k=703) == 411743991
    )
