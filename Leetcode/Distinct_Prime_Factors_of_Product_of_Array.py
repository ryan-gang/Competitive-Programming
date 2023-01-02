from typing import List


class Solution:
    """
    Generate all primes upto 1000.
    Then for each num, find the number of primes which divide num.
    """

    # Runtime: 887 ms, faster than 57.14%.
    # Memory Usage: 15.4 MB, less than 71.43%.
    # T : O(N), S : O(N)
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        self.seive(max(nums) + 1)
        factors = set()
        for num in nums:
            for prime in self.primes:
                if num % prime == 0:
                    factors.add(prime)

        return len(factors)

    def seive(self, N):
        MAX_SIZE = 1001
        isprime = [True] * MAX_SIZE
        self.primes = []
        SPF = [None] * (MAX_SIZE)
        isprime[0] = isprime[1] = False
        for i in range(2, N):
            if isprime[i]:
                self.primes.append(i)
                SPF[i] = i
            j = 0
            while j < len(self.primes) and i * self.primes[j] < N and self.primes[j] <= SPF[i]:
                isprime[i * self.primes[j]] = False
                SPF[i * self.primes[j]] = self.primes[j]
                j += 1

    # Runtime: 359 ms, faster than 100%.
    # Memory Usage: 15.4 MB, less than 85.71%.
    # T: O(n π(sqrt m)), where m is the largest value, and π is the “prime counting function.”
    # M: O(π(m)). We store all primes less than m in a hashset.
    def distinctPrimeFactors1(self, nums: List[int]) -> int:
        """
        This solution makes use of the fact that a number, n can have
        only 1 prime number that is greater than sqrt(n).
        As the max num in nums is 1000. We manually generate all primes
        upto sqrt(1000), and then whenever we come across a large prime,
        we add it to the list.
        """
        ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        primes = set()
        for n in nums:
            for p in ps:
                if n % p == 0:
                    primes.add(p)
                    while n % p == 0:
                        n /= p
            if n != 1:
                primes.add(n)  # large prime.
        return len(primes)


if __name__ == "__main__":
    sol = Solution()
    assert sol.distinctPrimeFactors([2, 4, 3, 7, 10, 6]) == 4
    assert sol.distinctPrimeFactors([2, 4, 8, 16]) == 1
    assert sol.distinctPrimeFactors([723, 2, 4, 5, 7, 11]) == 6
