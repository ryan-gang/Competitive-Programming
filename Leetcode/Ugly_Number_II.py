from heapq import heappush, heappop


class Solution:
    # T : O(N), S : O(N)
    def nthUglyNumber(self, N: int) -> int:
        """
        At every iteration, we multiply the smallest number with the primes, and
        put them all in a heap. From there we get the smallest at every stage.
        """
        heap = [1]
        primes = [2, 3, 5]

        for _ in range(N - 1):
            smallest = heappop(heap)
            for prime in primes:
                val = smallest * prime
                if val not in heap:
                    heappush(heap, val)

        return heappop(heap)

    # T : O(N), S : O(N)
    def nthUglyNumber1(self, N: int) -> int:
        """
        Every ugly number is another ugly number multiplied by 2, 3 or 5. The
        `starts` array contains the indexes of ugly numbers, that when
        multiplied by 2, 3 or 5 respectively, produces the smallest ugly number
        that is larger than the current overall maximum. Ref :
        https://leetcode.com/problems/ugly-number-ii/solutions/718879/python-o-n-universal-dp-solution-explained/
        """
        uglies = [1]
        factors = [2, 3, 5]
        k = 3
        starts = [0] * k
        for _ in range(N - 1):
            candidates = [x * uglies[y] for x, y in zip(factors, starts)]
            new = min(candidates)
            uglies.append(new)
            for idx in range(k):
                if candidates[idx] == new:
                    starts[idx] += 1
        return uglies[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.nthUglyNumber(N=1) == 1
    assert sol.nthUglyNumber(N=10) == 12
    assert sol.nthUglyNumber(N=11) == 15
    assert sol.nthUglyNumber(N=1690) == 2123366400
