class Solution:
    # Runtime: 63 ms, faster than 99.30% of Python3 online submissions.
    # Memory Usage: 14.2 MB, less than 59.01% of Python3 online submissions.
    def firstUniqChar(self, s: str) -> int:
        multi = set()
        single = set()

        for char in s:
            if char not in multi:
                if char not in single:
                    single.add(char)
                else:
                    single.remove(char)
                    multi.add(char)

        for idx, char in enumerate(s):
            if char in single:
                return idx

        return -1

    # Runtime: 182 ms, faster than 47.51% of Python3 online submissions.
    # Memory Usage: 14 MB, less than 96.20% of Python3 online submissions.
    def firstUniqChar2(self, s: str) -> int:
        array = [0 for _ in range(26)]

        for char in s:
            idx = ord(char) - ord("a")
            array[idx] += 1

        for idx, char in enumerate(s):
            char_idx = ord(char) - ord("a")
            if array[char_idx] == 1:
                return idx

        return -1


sol = Solution()
assert sol.firstUniqChar(s="leetcode") == 0
assert sol.firstUniqChar(s="loveleetcode") == 2
assert sol.firstUniqChar(s="aabb") == -1
