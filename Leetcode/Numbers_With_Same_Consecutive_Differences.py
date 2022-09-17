class SolutionWithStringConversions:
    # Runtime: 160 ms, faster than 5.32% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 94.35% of Python3 online submissions.
    def numsSameConsecDiff(self, N, k):
        self.all = []
        if N == 0:
            return 0
        elif N == 1:
            return [i for i in range(10)]
        else:
            for digit in range(1, 10):
                self.create(N, k, str(digit))
        return self.all

    def create(self, N: int, k: int, num: str) -> None:
        if len(num) == N:
            self.all.append(int(num))
            return
        for digit in range(10):
            if abs(int(num[-1]) - digit) == k:
                self.create(N, k, num + str(digit))


class Solution:
    # Runtime: 67 ms, faster than 50.83% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 94.35% of Python3 online submissions.
    # T : O(Nx(2^N)), S : O(2 ^ N)
    # T = (9 x 2 ^ (N - 1))
    # First digit has 9 possibilities, after that each digit has 2 possibilities.
    # Either prev_digit + k or prev_digit - k. For (N - 1) digits.
    # S = O(N) + O(2^N) (call stack + output list)
    def numsSameConsecDiff(self, N, k):
        self.all = []
        if N == 0:
            return 0
        elif N == 1:
            return [i for i in range(10)]
        else:
            for digit in range(1, 10):
                self.create(N, k, digit, length=1)
        return self.all

    def create(self, N: int, k: int, num: int, length: int) -> None:
        if length == N:
            self.all.append((num))
            return
        for digit in range(10):
            if abs((num % 10) - digit) == k:
                self.create(N, k, num * 10 + digit, length + 1)


sol = Solution()
assert sol.numsSameConsecDiff(N=3, k=7) == [181, 292, 707, 818, 929]
assert (sol.numsSameConsecDiff(N=2, k=1)) == [
    10,
    12,
    21,
    23,
    32,
    34,
    43,
    45,
    54,
    56,
    65,
    67,
    76,
    78,
    87,
    89,
    98,
]
print(sol.numsSameConsecDiff(N=9, k=0))

# TODO : Check BFS solution.
# Here : https://leetcode.com/problems/numbers-with-same-consecutive-differences/solution/
