from collections import Counter


class Solution:
    # Runtime: 89 ms, faster than 53.96%.
    # Memory Usage: 15.2 MB, less than 81.15%.
    # T : O(N + KlogK), S : O(N)
    # K = 52 (len(alphabet) * 2), space might be ignored, that is the output.
    def frequencySort(self, s: str) -> str:
        """
        Sorts the counter items, based on frequency.
        """
        d = Counter(s)

        out = []
        for item in sorted(d.items(), key=lambda item: item[1], reverse=True):
            out.extend([item[0] * item[1]])

        return "".join(out)

    # T : O(N), S : O(N)
    def frequencySort1(self, s: str) -> str:
        """
        Uses counting sort, and extra O(N) space.
        """
        cnt = Counter(s)
        n = len(s)
        bucket = [[] for _ in range(n + 1)]
        for c, freq in cnt.items():
            bucket[freq].append(c)

        ans = []
        for freq in range(n, -1, -1):
            for c in bucket[freq]:
                ans.append(c * freq)
        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    assert sol.frequencySort("tree") == "eetr"
    assert sol.frequencySort("cccaaa") == "cccaaa"
    assert sol.frequencySort("Aabb") == "bbAa"
