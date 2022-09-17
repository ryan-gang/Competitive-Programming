from typing import List


class Solution:
    # Runtime: 69 ms, faster than 5.82%.
    # Memory Usage: 14 MB, less than 17.88%.
    # T : O(N^2), S : O(N^2)
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = []
        first_row = [1]
        pascals_triangle.append(first_row)
        prev_row = first_row
        for i in range(numRows - 1):
            curr_row = self.create_next_row(prev_row)
            prev_row = curr_row
            pascals_triangle.append(curr_row)

        return pascals_triangle

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
