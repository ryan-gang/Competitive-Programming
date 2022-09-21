from typing import List


class Solution:
    """
    The brute force would be to actually "execute" the query, alter nums array, and recalculate
    the sum every time. But that is terribly inefficient. So instead we store the initial sum,
    and then subsequently just alter this. For every query, if the previous number was even,
    we remove it from the sum. Because it was included in the sum. And then if the current is
    odd, we are done. Just pass. Else if current val (after altering) is even, we add this entire
    val into the sum. And then return. This is much easier imo. We could also handle all the
    cases individually.
    Prev, Curr, Action.
    Odd, Odd, Pass.
    Odd, Even, Add val + nums[idx] to sum.
    Even, Odd, Remove previous val from sum.
    Even, Even, Add only val to sum.
    Basically the same thing as our 2 conditions.
    """

    # 53/58 TC Passed. TLE.
    def sumEvenAfterQueriesSimulation(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        out = []
        for val, idx in queries:
            nums[idx] += val
            answer = self.generate_sum(nums)
            out.append(answer)
        return out

    # Runtime: 1734 ms, faster than 5.10% of Python3 online submissions.
    # Memory Usage: 20.3 MB, less than 97.19% of Python3 online submissions.
    # T : O(N + Q), S : O(1)
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        out = []
        answer = self.generate_sum(nums)
        for val, idx in queries:
            prev_val = nums[idx]
            nums[idx] += val
            curr_val = nums[idx]
            prev = bool(prev_val % 2)
            curr = bool(curr_val % 2)

            if not prev:  # Previously even.
                answer -= prev_val
            if not curr:  # Currently even.
                answer += curr_val
            out.append(answer)
        return out

    def generate_sum(self, nums: List[int]):
        S = 0
        for num in nums:
            if not num % 2:
                S += num
        return S


sol = Solution()
assert sol.sumEvenAfterQueries(nums=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]) == [
    8,
    6,
    2,
    4,
]
assert sol.sumEvenAfterQueries(nums=[1], queries=[[4, 0]]) == [0]
