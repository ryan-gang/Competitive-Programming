from typing import List


class Solution:
    # Runtime: 370 ms, faster than 45.5%.
    # Memory Usage: 14.8 MB, less than 25.26%.
    # T : O(MxN), S : O(M) ; where M is the length of a string, and N is the count of all strings.
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Space usage can be reduced, by just iterating the strings, columnwise.
        Keep a count of unsorted columns.
        """
        dp = list(strs[0])
        for string in strs[1:]:
            for idx, char in enumerate(string):
                if dp[idx] == "#":
                    continue
                elif dp[idx] <= char:
                    dp[idx] = char
                else:
                    dp[idx] = "#"

        return dp.count("#")

    # Runtime: 412 ms, faster than 37.8%.
    # Memory Usage: 14.7 MB, less than 25.26%.
    # T : O(MxN), S : O(1)
    def minDeletionSize1(self, strs: List[str]) -> int:
        col = count = 0
        rows, cols = len(strs), len(strs[0])
        while col < cols:
            for row in range(1, rows):
                print(row, col)
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break
            col += 1

        return count

    def minDeletionSize2(self, strs: List[str]) -> int:
        """
        >>> strs=["rrjk", "furt", "guzm"]
        >>> list(zip(*strs))
        [('r', 'f', 'g'), ('r', 'u', 'u'), ('j', 'r', 'z'), ('k', 't', 'm')]
        """
        return sum(list(col) != sorted(col) for col in zip(*strs))


if __name__ == "__main__":
    sol = Solution()
    assert sol.minDeletionSize1(strs=["cba", "daf", "ghi"]) == 1
    assert sol.minDeletionSize1(strs=["a", "b"]) == 0
    assert sol.minDeletionSize1(strs=["zyx", "wvu", "tsr"]) == 3
    assert sol.minDeletionSize1(strs=["rrjk", "furt", "guzm"]) == 2
