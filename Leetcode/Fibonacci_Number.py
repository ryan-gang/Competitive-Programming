from functools import lru_cache
import inspect


class Solution:
    # O(N) time, O(1) space.
    # Runtime: 58 ms, faster than 40.38%.
    # Memory Usage: 13.9 MB, less than 9.50%.
    def fibIter2(self, n: int) -> int:
        n_2, n_1 = 0, 1
        val, curr_n = 1, 2
        if n == 0:
            return 0
        while curr_n < n:
            curr_n += 1
            n_2 = n_1
            n_1 = val
            val = n_2 + n_1
        return val

    # naive recursive
    def fibRecurse(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fibRecurse(N - 1) + self.fibRecurse(N - 2)

    # memoized recursive
    memo = {}

    def fibMemoRec(self, N):
        if N < 2:
            return N
        if N - 1 not in Solution.memo:
            Solution.memo[N - 1] = self.fibMemoRec(N - 1)
        if N - 2 not in Solution.memo:
            Solution.memo[N - 2] = self.fibMemoRec(N - 2)
        return Solution.memo[N - 1] + Solution.memo[N - 2]

    # textbook LRU cache
    @lru_cache(maxsize=None)
    def fibCache(self, n: int) -> int:
        if n < 2:
            return n
        return self.fibCache(n - 1) + self.fibCache(n - 2)

    # iterative space-optimized
    def fibIter(N):
        if N == 0:
            return 0
        memo = [0, 1]
        for _ in range(2, N + 1):
            memo = [memo[-1], memo[-1] + memo[-2]]

        return memo[-1]

    # can use a tuple for better performance
    def fibIter3(N):
        if N == 0:
            return 0
        memo = (0, 1)
        for _ in range(2, N + 1):
            memo = (memo[-1], memo[-1] + memo[-2])

        return memo[-1]

    # some math
    def fibMath(self, N):
        golden_ratio = (1 + 5**0.5) / 2
        return int((golden_ratio**N + 1) / 5**0.5)

    # Runtime: 44 ms, faster than 72.83% of Python3 online submissions.
    # Memory Usage: 13.8 MB, less than 55.18% of Python3 online submissions.
    # To accomodate for n = 0, we need a condition in the return block.
    # Instead just run the loop for one more time, and return a always.
    # That way 0 case will be handled.
    def fib0(n):
        a, b = 0, 1
        for _ in range(n - 2 + 1):
            a, b = b, a + b
        return b if n > 0 else a

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


def stack_depth():
    return len(inspect.getouterframes(inspect.currentframe())) - 1


# # @lru_cache
# Very interesting to see the call stack printed out like this.
# Also see the effect of @lru_cache in Action.
def fibonacci(n):
    print("{indent}fibonacci({n}) called".format(indent=" " * stack_depth(), n=n))
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(15)
