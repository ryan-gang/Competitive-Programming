from typing import List


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
Output = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]


class Solution:
    # Runtime: 335 ms, faster than 8.37% of Python3 online submissionssecond.
    # Memory Usage: 14.8 MB, less than 87.53% of Python3 online submissionssecond.
    # T : O(M + N), S : O(M + N)
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        out = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            # For every pair of 2 intervals, compute the max
            # of their starts, and the min of their ends.
            # If the start and end are in order (start < end),
            # that signifies the intersection is valid.
            # We can add this to the list of intervals.
            # And the one with the earlier end, we discard and move on to the next.
            first, second = firstList[i], secondList[j]
            lo, hi = max(first[0], second[0]), min(first[1], second[1])
            if lo <= hi:
                out.append([lo, hi])

            if first[1] < second[1]:
                i += 1
            else:
                j += 1

        return out

    # Runtime: 211 ms, faster than 62.62% of Python3 online submissions.
    # Memory Usage: 14.9 MB, less than 51.17% of Python3 online submissions.
    def intervalIntersection2(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        out = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            # For every pair of 2 intervals,
            # we first check if the intervals actually intersect,
            # for the intervals to intersect,
            # A has to start before B ends, & A has to end after B starts.
            # Like -> A_start B_start A_end B_end
            # Then we find the interval, and add it to output.
            # We can add this to the list of intervals.
            # And the one with the earlier end, we discard and move on to the next.
            first, second = firstList[i], secondList[j]
            if first[1] >= second[0] and first[0] <= second[1]:
                lo, hi = max(first[0], second[0]), min(first[1], second[1])
                out.append([lo, hi])

            if first[1] < second[1]:
                i += 1
            else:
                j += 1

        return out


sol = Solution()
assert sol.intervalIntersection2(firstList, secondList) == Output
