from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    # Runtime: 104 ms, faster than 96.31%.
    # Memory Usage: 14.3 MB, less than 40.29%.
    # T : O(NLogN + QlogN), S : O(N)
    # Sort nums and Q times Binary search on nums.
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Sort input A, since we care the sum and don't care about the order.
        Calculate the prefix sum of A, since we want to know the accumulate sum.
        (If j+k+l <= N; then surely j-1+k-1+l-1 <= N, so it can be proved that always
        taking the sum from the smallest number, will lead to the optimal values.)
        Binary seach each query q in query, and the index is the result.
        return result res.
        """
        nums.sort()
        prefix = []
        add = 0
        for num in nums:
            add += num
            prefix.append(add)
        out = []
        for query in queries:
            out.append(bisect_right(prefix, query))

        return out

    def answerQueries1(self, A: List[int], queries: List[int]) -> List[int]:
        A = list(accumulate(sorted(A)))
        return [bisect_right(A, q) for q in queries]


if __name__ == "__main__":
    sol = Solution()
    assert sol.answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]) == [2, 3, 4]
    assert sol.answerQueries(nums=[2, 3, 4, 5], queries=[1]) == [0]
    assert sol.answerQueries(
        nums=[736411, 184882, 914641, 37925, 214915],
        queries=[331244, 273144, 118983, 118252, 305688, 718089, 665450],
    ) == [2, 2, 1, 1, 2, 3, 3]
