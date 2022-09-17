import time


class Solution:
    # Runtime: 31 ms, faster than 92.53%.
    # Memory Usage: 13.8 MB, less than 96.38%.
    # T : O(N), S : O(N)
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        if n >= 2:
            dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    # Runtime: 32 ms, faster than 90.00%.
    # Memory Usage: 13.9 MB, less than 57.17%.
    # T : O(N), S : O(1)
    def climb(self, n: int) -> int:
        a, b = 1, 2
        if n < 3:
            return n
        for i in range(2, n):
            a, b = b, a + b

        return b

    """The state of `n` only depends on the state of `n-1` and `n-2`, We can count all the ways
    to climb n stairs, by adding the ways we can climb n-1 stairs and n-2 stairs. Because we can
    just add a `1` and a `2` at the end of those 2 sequences, and we will get our required list
    of sequences. """
    # Runtime: 60 ms, faster than 16.96% of Python3 online submissions.
    # Memory Usage: 13.7 MB, less than 99.78% of Python3 online submissions.
    def stairs(self, n: int) -> int:
        a, b = 1, 2
        for _ in range(n - 1):
            a, b = b, a + b

        return a


class SolutionBacktracking:
    # T : O(2^N), S : O(1)
    # 2^N function calls, O(N) stack space used.
    # 10/45 TC passed. TLE.
    def climbStairs(self, n: int) -> int:
        self.permutations = 0
        self.N = n
        self.climb(0)
        return self.permutations

    def climb(self, n: int) -> None:
        if n == self.N:
            self.permutations += 1
            return
        for i in range(1, 3):
            if n + i <= self.N:
                self.climb(n + i)


sol = SolutionBacktracking()
print(sol.climbStairs(30))
assert sol.climbStairs(3) == 3
assert sol.climbStairs(2) == 2

for _ in range(1, 41):
    start = time.time()
    val = sol.climbStairs(_)
    end = time.time()
    print(f"i : {_}, val : {val}, time : {round((end - start), 3)}")
