class Solution:
    # Runtime: 570 ms, faster than 100%.
    # Memory Usage: 14.7 MB, less than 100%.
    # T : O(N), S : O(N)
    def minimumPartition(self, s: str, k: int) -> int:
        """
        Pretty simple, we keep increasing the string greedily, if it
        becomes larger than 'k' we increment `res` and set the string as
        only the last digit. As the num - the last digit was less than
        or equal to k.
        """
        res, idx, prev = 1, 1, 0
        while idx <= len(s):
            num = int(s[prev:idx])
            if num <= k:
                idx += 1
            if num > k:
                res += 1
                prev = idx - 1
                num = int(s[prev:idx])

            if num > k:
                return -1
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.minimumPartition(s="165462", k=60) == 4
    assert sol.minimumPartition(s="238182", k=5) == -1
    assert sol.minimumPartition(s="1", k=1) == 1
