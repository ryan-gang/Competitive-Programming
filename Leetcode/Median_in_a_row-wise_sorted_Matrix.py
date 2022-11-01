from typing import List


class Solution:
    """
    The median will have R * C / 2 elements smaller than it.
    Out strategy will be starting with a value, then finding the number of elements smaller
    than it. And based on that updating the value.
    Both operations will be using binary search.
    """

    # Ref : https://logicmojo.com/median-of-rowwise-sorted-matrix
    # This solution is still unoptimal. Median is searched in a fixed range of 1 to 2000.
    # Instead of searching values in the array.
    def count_less_than_val(self, val: int) -> int:
        count = 0
        for _, row in enumerate(self.matrix):
            lo, hi = 0, len(row) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] <= val:
                    lo = mid + 1
                else:
                    hi = mid - 1

            count += lo
        return count

    def median(self, matrix: List[List[int]], R: int, C: int) -> int:
        self.matrix = matrix
        # Constraints set by question.
        L, H = 1, 2000
        while L <= H:
            median = (L + H) // 2
            count = self.count_less_than_val(median)
            if count <= (R * C) // 2:
                L = median + 1
            else:
                H = median - 1

        return L


if __name__ == "__main__":
    sol = Solution()
    assert sol.median(matrix=[[1, 3, 5], [2, 6, 9], [3, 6, 9]], R=3, C=3) == 5
    assert sol.median([[1], [2], [3]], 3, 1) == 2
