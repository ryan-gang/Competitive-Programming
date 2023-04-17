class Solution:
    # Runtime: 35 ms, faster than 87.18%.
    # Memory Usage: 13.9 MB, less than 50.96%.
    # T : O(N), S : O(1)
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        out = [False] * len(candies)
        m = max(candies)
        for idx, candy in enumerate(candies):
            if candy + extraCandies >= m:
                out[idx] = True

        return out
