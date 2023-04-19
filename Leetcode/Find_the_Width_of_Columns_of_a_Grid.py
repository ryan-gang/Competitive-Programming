class Solution:
    # T : O(N), S : O(1)
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        out = [0] * len(grid[0])
        for _, row in enumerate(grid):
            for c, val in enumerate(row):
                out[c] = max(out[c], len(str(val)))

        return out

    def findColumnWidth1(self, grid: list[list[int]]) -> list[int]:
        return [max(len(str(a)) for a in r) for r in zip(*grid)]
