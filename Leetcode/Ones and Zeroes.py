from functools import cache


class Solution:
    # Runtime: 2576 ms, faster than 83.41%.
    # Memory Usage: 303.7 MB, less than 5.61%.
    # T : O(N), S : O(N)
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        At every index we check how the inclusion and exclusion of that
        string affects the final output.
        Once, we include that string, and recurse to the next index.
        And again we exclude it and recurse to the next index.
        Then we can choose the one which gives the max answer.
        """
        N = len(strs)

        @cache
        def count(idx: int, zeroes: int, ones: int) -> int:
            if zeroes < 0 or ones < 0:
                return -1  # invalid subset, return -1.
            if idx == N:
                return 0  # Valid subset, but length = 0.

            z, o = strs[idx].count("0"), strs[idx].count("1")

            include_idx = 1 + count(idx + 1, zeroes - z, ones - o)
            exclude_idx = count(idx + 1, zeroes, ones)

            return max(include_idx, exclude_idx)

        return max(count(0, m, n), 0)


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3) == 4
    assert sol.findMaxForm(strs=["10", "0", "1"], m=1, n=1) == 2
    assert sol.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=4, n=3) == 3
    assert sol.findMaxForm(strs=["0", "0", "1", "1"], m=2, n=2) == 4
