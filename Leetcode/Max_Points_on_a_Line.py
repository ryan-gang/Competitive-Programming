import math
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def calc_slope(x1: int, x2: int, y1: int, y2: int) -> float:
        return ((y2 - y1) / (x2 - x1)) if x1 != x2 else float("inf")

    # Runtime: 95 ms, faster than 86.7%.
    # Memory Usage: 13.9 MB, less than 94.26%.
    # T : O(N^2), S : O(N)
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        For each point in our list, we find the slope of all the lines
        from this point to all the other points, and we see if any of
        the slopes overlap, if it is same for multiple points, that
        means they all fall on the same line. As the point is fixed,
        same slope means, same lines.
        """
        max_count = 1
        n = len(points)
        for i in range(n):
            d = defaultdict(int)
            for j in range(i + 1, n):
                slope = Solution.calc_slope(points[i][0], points[j][0], points[i][1], points[j][1])
                d[slope] += 1
                max_count = max(max_count, d[slope] + 1)

        return max_count


class Solution2:
    """Exact same thing."""

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 - x2 == 0:
                return float("inf")
            return (y1 - y2) / (x1 - x2)

        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i + 1 :]):
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1


class Solution3:
    """This one uses tan inverse instead of slope (technically the same thing.)"""

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result


if __name__ == "__main__":
    sol = Solution()
    assert (sol.maxPoints([[0, 0], [1, 1], [0, 1], [1, 2]])) == 2
    assert sol.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
