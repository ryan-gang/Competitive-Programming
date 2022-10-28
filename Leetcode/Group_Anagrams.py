from collections import defaultdict
from typing import List


class Solution:
    # Runtime: 190 ms, faster than 65.49% of Python3 online submissions.
    # Memory Usage: 18.1 MB, less than 50.70% of Python3 online submissions.
    # T : O(NMLOGM), S : O(NM)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            key = sorted(word)
            d[tuple(key)].append(word)
        return list(d.values())

    # Runtime: 117 ms, faster than 87.35% of Python3 online submissions.
    # Memory Usage: 18.9 MB, less than 36.29% of Python3 online submissions.
    # T : O(NM), S : O(NM)
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        # No need to sort, use an Array of 26 elements, to keep track of freqs
        # map the tuple of array to string.
        d = defaultdict(list)
        for word in strs:
            array = [0] * 26
            for char in word:
                array[ord(char) - ord("a")] += 1
            d[tuple(array)].append(word)
        return list(d.values())


if __name__ == "__main__":
    sol = Solution()
    assert sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
