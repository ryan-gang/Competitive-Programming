from collections import Counter


class Solution:
    # Runtime: 78 ms, faster than 24.38%.
    # Memory Usage: 14.1 MB, less than 33.95%.
    # T : O(N), S : O(N)
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = Counter(arr).values()
        return len(set(d)) == len(d)


if __name__ == "__main__":
    sol = Solution()
    assert sol.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3])
    assert not sol.uniqueOccurrences(arr=[1, 2, 1, 1, 3])
