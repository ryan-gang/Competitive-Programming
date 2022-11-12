from math import sqrt

# TODO : https://www.geeksforgeeks.org/sieve-eratosthenes-0n-time-complexity/
# More optimized solution.


class Solution:
    # Base implementation of sieve of eratosthenes. No optimizations.
    # TLE. 62/66.
    def countPrimes(self, n: int) -> int:
        sieve = [1] * (n + 1)
        rootn = round(sqrt(n))

        for i in range(rootn + 1):
            if i <= 1:
                sieve[i] = 0
            elif sieve[i]:
                for j in range(i, (n // i) + 1):
                    sieve[i * j] = 0
        return sieve[:-1].count(1)

    """
    The trick to make the code faster is, instead of iterating over the array and flipping
    every single composite number to 0, do it in one go, using list splicing (?).
    sieve[i * i : n : i] = [0] * len(sieve[i * i : n : i])
    i = 2, n = 10
    From i * i (= 4) to 9, we set all multiples of 2 to [0, 0, 0]
    Makes the code very fast.
    Another thing to notice we are not iterating from i to n, we are doing i * i to n.
    Because the multiples of i below i * i will already be covered by numbers less than i.
    Ref for TimeComplexity : https://www.geeksforgeeks.org/
    how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/
    """
    # Runtime: 2084 ms, faster than 85.53% of Python3 online submissions.
    # Memory Usage: 92 MB, less than 26.18% of Python3 online submissions.
    # T : O(N * log(log(N))), S : O(N)
    def countPrimesFaster(self, n: int) -> int:
        if n < 3:
            return 0

        sieve = [1] * (n)
        sieve[0] = sieve[1] = 0

        for i in range(int(n**0.5) + 1):
            if sieve[i]:
                sieve[i * i : n : i] = [0] * len(sieve[i * i : n : i])
        return sum(sieve)


if __name__ == "__main__":
    sol = Solution()
    assert sol.countPrimesFaster(10) == 4
    assert sol.countPrimesFaster(0) == 0
    assert sol.countPrimesFaster(1) == 0
    assert sol.countPrimesFaster(2) == 0
    assert sol.countPrimesFaster(959831) == 75604
    assert sol.countPrimesFaster(5000000) == 348513
