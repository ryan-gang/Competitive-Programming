"""
Given an array of numbers a[1...n], find a sub-array a[l...r] with the maximal sum.
"""

from itertools import accumulate


class MaxSubarraySum:
    """
    Let s[] be a prefix sum array, where s[i] = sum(a[0:i])
    From the prefix sum array, we need to find our 2 indices, r and l.
    Such that a[r] - a[l] is maximised. If r is fixed, we need the
    smallest value in [0,r-1] for a[l]. By simply storing the current minimum
    we can access this in O(1) time. And simply update this for every iteration.
    We can optimise this further, by not storing the prefix array and
    generating the last element on the fly.
    """

    @staticmethod
    # Simple.
    def max_subarray_sum(a: list[int]) -> int:
        prefix = list(accumulate(a))  # prefix sum.
        min_sum = ans = 0
        for val in prefix:
            min_sum = min(min_sum, val)
            ans = max(ans, val - min_sum)
            # Where val - min_sum is the max sub-array sum upto this index.

        return ans

    @staticmethod
    # No prefix array stored, val created on the fly.
    def max_subarray_sum1(a: list[int]) -> int:
        ans, sum, min_sum = a[0], 0, 0
        for r in range(len(a)):
            sum += a[r]
            ans = max(ans, sum - min_sum)
            min_sum = min(min_sum, sum)

        return ans

    @staticmethod
    # Also gets the boundaries of the maximal subarray.
    def max_subarray_sum_with_boundaries(a: list[int]) -> tuple[int, int, int]:
        ans, min_pos = a[0], -1
        ans_l = ans_r = sum = min_sum = 0

        for r in range(len(a)):
            sum += a[r]
            cur = sum - min_sum
            if cur > ans:
                ans = cur
                ans_l = min_pos + 1
                ans_r = r
            if sum < min_sum:
                min_sum = sum
                min_pos = r

        return ans_l, ans_r, ans


class MaxSubarraySumKadane:
    """
    Kadane's algorithm. Proposed by Jay Kadane in 1984.

    Let's go through the array and accumulate the current prefix sum in some
    variable s. If at some point s is negative, we just assign s = 0. It is
    argued that the maximum of all the values that the variable s is assigned to
    during the algorithm will be the answer to the problem.

    Proof:

    Consider the first index when the sum of s becomes negative. This means that
    starting with a zero partial sum, we eventually obtain a negative partial
    sum — so this whole prefix of the array, as well as any suffix, has a
    negative sum. Therefore, this subarray never contributes to the partial sum
    of any subarray of which it is a prefix, and can simply be dropped.

    However, this is not enough to prove the algorithm. In the algorithm, we are
    actually limited in finding the answer only to such segments that begin
    immediately after the places when s<0 happened.

    But, in fact, consider an arbitrary segment [l, r], and l is not in such a
    "critical" position (i.e. l > p+1, where p is the last such position, in
    which s<0). Since the last critical position is strictly earlier than in
    l-1, it turns out that the sum of a[p+1 ... l-1] is non-negative. This means
    that by moving l to position p+1, we will increase the answer or, in extreme
    cases, we will not change it.

    One way or another, it turns out that when searching for an answer, you can
    limit yourself to only segments that begin immediately after the positions
    in which s<0 appeared. This proves that the algorithm is correct.
    """

    @staticmethod
    # Kadane's algo.
    def max_subarray_sum_kadane(a: list[int]) -> int:
        add = ans = 0
        for val in a:
            add += val
            ans = max(ans, add)
            add = max(add, 0)

        return ans

    @staticmethod
    # Also gets the boundaries of the maximal subarray, using Kadane's algo.
    def max_subarray_sum_kadane_with_boundaries(a: list[int]) -> tuple[int, int, int]:
        ans, minus_pos = a[0], -1
        ans_l = ans_r = sum = 0

        for r in range(len(a)):
            sum += a[r]
            if sum > ans:
                ans = sum
                ans_l = minus_pos + 1
                ans_r = r

            if sum < 0:
                sum = 0
                minus_pos = r

        return ans_l, ans_r, ans
