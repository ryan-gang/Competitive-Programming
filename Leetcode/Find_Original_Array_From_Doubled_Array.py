from collections import Counter
from typing import List


class Solution:
    # 127/178 TC Passed. Wrong answer.
    # Failed on changed=[0,0,0,0]
    def findOriginalArrayWrong(self, changed: List[int]) -> List[int]:
        out = []
        s = set(changed)
        changed.sort()
        for i in changed:
            double = i * 2
            if double in s and i in s and i != double:
                s.remove(double)
                s.remove(i)
                out.append(i)

        return out if len(s) == 0 else []

    # Runtime: 1408 ms, faster than 96.19% of Python3 online submissions.
    # Memory Usage: 32.7 MB, less than 49.63% of Python3 online submissions.
    def findOriginalArray(self, changed):
        c = Counter(changed)
        # If odd number of 0's, return False.
        if c[0] % 2:
            return []
        # Start iterating the list, starting from the lowest element.
        for x in sorted(c):
            # If the smaller number, is present more than the doubled number,
            # there is no way this is legit. Return false.
            if c[x] > c[2 * x]:
                return []
            # Else, reduce the count of x from 2x.
            # But if x is 0, reduce
            if x != 0:
                c[2 * x] -= c[x]
            else:
                # If x == 0, c[2x] -= c[x] will give all 0. So we half it.
                c[2 * x] = c[x] // 2
            # c[2 * x] -= c[x] if x else c[x] // 2 # One liner.
        return list(c.elements())


sol = Solution()

assert sol.findOriginalArray(changed=[1, 3, 4, 2, 6, 8]) == [1, 3, 4]
assert sol.findOriginalArray(changed=[6, 3, 0, 1]) == []
assert sol.findOriginalArray(changed=[1]) == []
assert sol.findOriginalArray(changed=[0, 0, 0, 0]) == [0, 0]
assert sol.findOriginalArray(changed=[0, 0, 0, 0, 0, 0]) == [0, 0, 0]
