from typing import List
from StarterCode.decorators import timeit


class Solution:
    # Runtime: 65 ms, faster than 11.29% of Python3 online submissions.
    # Memory Usage: 13.9 MB, less than 16.36% of Python3 online submissions.
    # T : O(N^2), S : O(N)
    @timeit
    def getRow(self, numRows: int) -> List[int]:
        first_row = [1]
        prev_row = first_row
        for i in range(numRows):
            curr_row = self.create_next_row(prev_row)
            prev_row = curr_row

        return prev_row

    def create_next_row(self, prev_row: List[int]):
        curr_row = []
        curr_row.append(prev_row[0])
        lo = 0
        while lo < len(prev_row) - 1:
            hi = lo + 1
            val = prev_row[lo] + prev_row[hi]
            curr_row.append(val)
            lo += 1

        curr_row.append(prev_row[-1])
        return curr_row


sol = Solution()
print(sol.getRow(3))
