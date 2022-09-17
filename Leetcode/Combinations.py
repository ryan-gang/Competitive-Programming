from typing import List


class Solution:
    # Runtime: 480 ms, faster than 64.43% of Python3 online submissions.
    # Memory Usage: 15.9 MB, less than 52.30% of Python3 online submissions.
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations = []
        self.backtrack([], 1, n, k)
        return self.combinations

    def backtrack(self, array: List[int], lo, hi, k):
        if len(array) == k:
            self.combinations.append(array)
            return
        for i in range(lo, hi + 1):
            self.backtrack(array + [i], i + 1, hi, k)


sol = Solution()
print(sol.combine(4, 2))
print(sol.combine(1, 1))
# (sol.combine(20, 10))
print(sol.combine(20, 20))
