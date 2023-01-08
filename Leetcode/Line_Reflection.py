from collections import defaultdict
from typing import List


class Solution:
    # T : O(NLogN), S : O(N)
    # Worst case, at single Y coordinate we have all X coordinates. Need to sort entire list.
    def getMirror(self, points: List[List[int]]) -> bool:
        d = defaultdict(list)
        for x, y in points:
            d[y].append(x)

        mirror = None
        for y in d:
            if len(d[y]) % 2 == 1:
                return False
            else:
                xs = sorted(d[y])
                lo, hi = 0, len(xs) - 1
                while lo < hi:
                    dist = xs[hi] - xs[lo]
                    mirror_x = xs[lo] + dist
                    if mirror:
                        if mirror != mirror_x:
                            return False
                    lo += 1
                    hi -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.getMirror(
        points=[[1, 1], [-1, 1], [2, 3], [-2, 3], [2, 4], [-2, 4], [7, 1], [-7, 1]]
    )
    assert sol.getMirror(points=[[2, 1], [0, 1], [3, 3], [-1, 3], [3, 4], [-1, 4], [8, 1], [-6, 1]])
    assert sol.getMirror(points=[[1, 1], [-1, 1]])
    assert sol.getMirror(points=[[1, 1], [1, 1]])
    assert not sol.getMirror(points=[[1, 1], [-1, -1]])
